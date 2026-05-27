#ADE V2.2

ADE_VERSION = "ade_v2.2"

from datetime import datetime
from audit_core.utils import debug

def _extract_target_event(ev):
    name = (ev.get("name") or "").lower()
    category = str(ev.get("category") or "").upper()

    if category == "RACE_A":
        priority = "A"
    elif category == "RACE_B":
        priority = "B"
    elif category == "RACE_C":
        priority = "C"
    else:
        return None

    if "climb" in name:
        training_bias = "durability"
    elif "tt" in name or "threshold" in name:
        training_bias = "ftp"
    elif "vo2" in name:
        training_bias = "anaerobic"
    elif "sprint" in name:
        training_bias = "neuromuscular"
    else:
        training_bias = "mixed"

    date_raw = ev.get("start_date_local") or ev.get("date")

    if not date_raw:
        return None

    try:
        dt = datetime.fromisoformat(str(date_raw)[:10])
    except:
        return None

    return {
        "priority": priority,
        "training_bias": training_bias,
        "dt": dt
    }

def _score_ade_base_decision(
    operational_state,
    risk_flag,
    fatigue_class,
    load_trend,
    system_state,
    taper_state,
    days_to_event,
    nutrition_status,
    nutrition_conf,
    hrv_ratio=None,
):
    score = 100
    penalties = []
    drivers = []

    def penalise(points, reason):
        nonlocal score
        score -= points
        penalties.append({
            "points": points,
            "reason": reason
        })

    def support(reason):
        drivers.append(reason)

    # --------------------------------------------------
    # Operational state
    # --------------------------------------------------
    if operational_state == "recovery_priority":
        penalise(30, "Operational state is recovery_priority")
    elif operational_state == "load_accepting":
        support("Operational state is load_accepting")
    elif operational_state:
        penalise(10, f"Operational state is {operational_state}")
    else:
        penalise(10, "Operational state missing")

    # --------------------------------------------------
    # Risk flag
    # --------------------------------------------------
    if risk_flag == "high":
        penalise(30, "Risk flag is high")
    elif risk_flag == "moderate":
        penalise(15, "Risk flag is moderate")
    elif risk_flag == "normal":
        support("Risk flag is normal")
    else:
        penalise(8, "Risk flag missing or unknown")

    # --------------------------------------------------
    # Forecast context
    # --------------------------------------------------
    if fatigue_class == "red":
        penalise(25, "Forecast fatigue class is red")
    elif fatigue_class == "amber":
        penalise(12, "Forecast fatigue class is amber")
    elif fatigue_class in ("green", "transition"):
        support(f"Forecast context is {fatigue_class}")
    elif fatigue_class:
        penalise(5, f"Forecast context is {fatigue_class}")
    else:
        penalise(5, "Forecast context missing")

    # --------------------------------------------------
    # Load trend
    # --------------------------------------------------
    if load_trend == "increasing":
        penalise(8, "Forecast load trend is increasing")
    elif load_trend in ("stable", "declining"):
        support(f"Forecast load trend is {load_trend}")
    elif load_trend:
        penalise(4, f"Forecast load trend is {load_trend}")

    # --------------------------------------------------
    # HRV / physiology guardrail
    # --------------------------------------------------
    if hrv_ratio is not None:
        try:
            hrv = float(hrv_ratio)

            if hrv < 0.90:
                penalise(8, f"HRV ratio suppressed at {hrv:.2f}")
            elif hrv >= 1.00:
                support(f"HRV ratio stable at {hrv:.2f}")
            else:
                penalise(3, f"HRV ratio mildly reduced at {hrv:.2f}")

        except Exception:
            penalise(3, "HRV ratio unavailable or invalid")

    # --------------------------------------------------
    # Event / taper context
    # --------------------------------------------------
    if taper_state == "taper" and days_to_event is not None:
        if days_to_event <= 10 and load_trend == "increasing":
            penalise(20, "Increasing load inside taper window")
        else:
            support("Taper context present")

    elif taper_state == "pre_taper":
        support("Pre-taper context active")

    elif taper_state and taper_state != "none":
        support(f"Target event context is {taper_state}")

    # --------------------------------------------------
    # Nutrition is supplementary only
    # --------------------------------------------------
    if nutrition_conf in ("moderate", "high"):
        if nutrition_status == "severely_underfuelled":
            penalise(15, "Supplementary nutrition signal: severely underfuelled")
        elif nutrition_status == "underfuelled":
            penalise(8, "Supplementary nutrition signal: underfuelled")
        elif nutrition_status == "overfuelled":
            penalise(5, "Supplementary nutrition signal: overfuelled")
        elif nutrition_status == "balanced":
            support("Nutrition signal balanced")

    # --------------------------------------------------
    # Adaptation state light-touch only
    # --------------------------------------------------
    if system_state in ("maladaptation", "strained", "decline"):
        penalise(10, f"Adaptation state is {system_state}")

    elif system_state == "mixed_adaptation":
        penalise(
            5,
            "Adaptation focus is mixed; not all systems are progressing cleanly"
        )

    elif system_state in ("baseline", "stable", "positive_adaptation"):
        support(f"Adaptation focus is {system_state}")

    elif system_state:
        support(f"Adaptation focus is {system_state}")

    # --------------------------------------------------
    # Clamp and label
    # --------------------------------------------------
    score = max(0, min(100, round(score)))

    if score >= 85:
        label = "excellent"
    elif score >= 70:
        label = "strong"
    elif score >= 50:
        label = "caution"
    elif score >= 35:
        label = "constrained"
    else:
        label = "blocked"

    return {
        "value": score,
        "label": label,
        "scope": "pre_phase_governance",
        "basis": (
            "ADE base score from operational state, risk flag, forecast context, "
            "load trend, HRV guardrail, target-event context, supplementary "
            "nutrition signal, and adaptation focus. Does not include phase governance."
        ),
        "drivers": drivers,
        "penalties": penalties
    }

def run_adaptive_decision_engine(context):

    training_state = context.get("training_state", {}) or {}
    forecast = context.get("future_forecast", {}) or {}
    espe = context.get("energy_system_progression", {}) or {}

    directive = training_state.get("recommendation")
    operational_state = training_state.get("operational_state")
    
    fatigue_class = forecast.get("fatigue_class")
    load_trend = forecast.get("load_trend")

    system_state = None
    sports = espe.get("sports") or {}

    for sport, block in sports.items():
        if block.get("supported"):
            system_state = block.get("adaptation_state")
            break

    risk_flag = "normal"

    if fatigue_class == "red":
        risk_flag = "high"

    elif fatigue_class == "amber":
        risk_flag = "moderate"

    nutrition = context.get("nutrition_balance", {}) or {}
    nutrition_status = nutrition.get("status")
    nutrition_conf = nutrition.get("confidence")

    # --------------------------------------------------
    # 🎯 TARGET EVENT CONTEXT (calendar ONLY)
    # --------------------------------------------------

    today_raw = context.get("athlete_today")

    if isinstance(today_raw, str):
        today = datetime.fromisoformat(today_raw).date()
    elif hasattr(today_raw, "date"):
        today = today_raw.date()
    else:
        today = today_raw

    events = context.get("calendar") or []

    next_a = None

    if today and events:

        candidates = []

        for ev in events:

            t = _extract_target_event(ev)

            if not t:
                continue

            if t["priority"] != "A":
                continue

            if t["dt"].date() < today:
                continue

            candidates.append(t)

        if candidates:
            next_a = sorted(candidates, key=lambda x: x["dt"])[0]

    days_to_event = None
    taper_state = "none"
    training_bias = "mixed"

    if next_a:
        days_to_event = (next_a["dt"].date() - today).days if today else None

        p = next_a.get("priority") if next_a else None

        if days_to_event is not None and p:

            if p == "A":
                if days_to_event <= 10:
                    taper_state = "taper"
                elif days_to_event <= 21:
                    taper_state = "pre_taper"

            elif p == "B":
                if days_to_event <= 5:
                    taper_state = "taper"
                elif days_to_event <= 10:
                    taper_state = "pre_taper"

            else:
                taper_state = "none"

        # ✅ DIRECT — no mapping
        training_bias = next_a.get("training_bias", "mixed")

    # --------------------------------------------------
    # Nutrition = supplementary signal only (graded)
    # --------------------------------------------------

    nutrition_note = None

    if nutrition_conf in ("moderate", "high"):

        if nutrition_status == "severely_underfuelled":
            nutrition_note = "Carbohydrate intake is far below demand for current load; fuelling gap likely limiting adaptation."

        elif nutrition_status == "underfuelled":
            nutrition_note = "Carbohydrate intake is below demand; consider increasing fuelling to match training load."

        elif nutrition_status == "overfuelled":
            nutrition_note = "Energy intake exceeds current demand; monitor balance relative to load."

        elif nutrition_status == "balanced":
            nutrition_note = "Energy intake aligns with current training demand."

    # DO NOT change:
    # - directive
    # - operational_state
    # - risk_flag

    decision = {
        "directive": directive,
        "operational_state": operational_state,
        "adaptation_focus": system_state,
        "risk_flag": risk_flag,
        "forecast_context": fatigue_class,
        "load_trend": load_trend,
        "nutrition_status": nutrition_status,
        "nutrition_confidence": nutrition_conf,
        "nutrition_note": nutrition_note,
        "target_event": {
            "exists": bool(next_a),
            "days_to_event": days_to_event,
            "taper_state": taper_state,
            "event_demand": training_bias
        },
        "version": ADE_VERSION
    }

    hrv_ratio = (training_state.get("signals") or {}).get("hrv_ratio")

    decision["ade_base_score"] = _score_ade_base_decision(
        operational_state=operational_state,
        risk_flag=risk_flag,
        fatigue_class=fatigue_class,
        load_trend=load_trend,
        system_state=system_state,
        taper_state=taper_state,
        days_to_event=days_to_event,
        nutrition_status=nutrition_status,
        nutrition_conf=nutrition_conf,
        hrv_ratio=hrv_ratio,
    )

    context["adaptive_decision"] = decision

    return {"adaptive_decision": decision}