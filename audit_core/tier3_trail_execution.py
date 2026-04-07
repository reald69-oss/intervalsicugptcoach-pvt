# tier3_trail_execution.py

"""
Tier-3 — Trail Execution Intelligence

Purpose:
- Evaluate how terrain affects execution quality
- Convert rule-based signals into a compact Tier-3 signal
- Inject into performance_intelligence (URF v5.1 compliant)

Output (minimal, compliant):
    performance_intelligence["run_terrain_execution"] = {
        "efficiency_state": "...",
        "limiter": "...",
        "confidence": "..."
    }
"""

from coach_trail_rules import (
    TRAIL_EXECUTION_RULES,
    TRAIL_FLAGS,
    TRAIL_DEFAULTS,
    TRAIL_INTERPRETATION
)


def _has_meaningful_trail_runs(df):

    if "type" not in df.columns:
        return False

    runs = df[df["type"].str.contains("Run", na=False)]

    if runs.empty:
        return False

    # --- minimum volume (30 min total) ---
    if "moving_time" in runs.columns:
        if runs["moving_time"].sum() < 1800:
            return False

    # --- terrain relevance (must have some gradient) ---
    if "grade" in runs.columns:
        if runs["grade"].mean() < 3:
            return False

    return True

# --------------------------------------------------
# CONDITION MATCHER
# --------------------------------------------------

def match_conditions(conditions: dict, metrics: dict) -> bool:

    for key, value in conditions.items():

        if key.endswith("_min"):
            m = key.replace("_min", "")
            if metrics.get(m, 0) < value:
                return False

        elif key.endswith("_max"):
            m = key.replace("_max", "")
            if metrics.get(m, 0) > value:
                return False

        else:
            if metrics.get(key) != value:
                return False

    return True


# --------------------------------------------------
# RULE EVALUATION
# --------------------------------------------------

def evaluate_rules(metrics: dict):

    results = {}
    priorities = {}
    flags = []

    # --- execution rules ---
    for rule in TRAIL_EXECUTION_RULES:

        if match_conditions(rule["conditions"], metrics):

            rtype = rule["type"]
            priority = rule.get("priority", 99)

            if rtype not in priorities or priority < priorities[rtype]:
                results[rtype] = rule["result"]
                priorities[rtype] = priority

    # --- flags ---
    for rule in TRAIL_FLAGS:
        if match_conditions(rule["conditions"], metrics):
            flags.append(rule["flag"])

    return results, flags


# --------------------------------------------------
# CLASSIFIER (compression layer)
# --------------------------------------------------

def classify_execution(signals: dict, flags: list):

    efficiency = signals.get("efficiency", TRAIL_DEFAULTS["efficiency"])
    durability = signals.get("durability", TRAIL_DEFAULTS["durability"])
    environment = signals.get("environment", TRAIL_DEFAULTS["environment"])

    # --- limiter ---
    if environment != "none":
        limiter = "heat" if environment == "heat" else "environment"
    elif efficiency in ["overexerting", "pace_collapse"]:
        limiter = "terrain"
    elif durability == "drifting":
        limiter = "fatigue"
    else:
        limiter = "none"

    # --- efficiency state ---
    if "direct_climb_penalty" in flags:
        state = "inefficient"
    elif efficiency in ["overexerting", "pace_collapse"]:
        state = "inefficient"
    elif durability == "drifting":
        state = "moderate"
    elif efficiency == "efficient":
        state = "efficient"
    else:
        state = "moderate"

    # --- confidence ---
    confidence = "high" if len(flags) > 0 else "moderate"

    return {
        "efficiency_state": state,
        "limiter": limiter,
        "confidence": confidence
    }


def build_interpretation(signals: dict, flags: list, classification: dict):

    eff = signals.get("efficiency")
    dur = signals.get("durability")
    env = signals.get("environment")

    state = classification.get("efficiency_state")

    interpretation = None
    coaching = None

    # --------------------------------------------------
    # PRIORITY 1 → FLAGS (most specific)
    # --------------------------------------------------

    for f in flags:
        block = TRAIL_INTERPRETATION.get("flags", {}).get(f)
        if block:
            return block["interpretation"], block["coaching"]

    # --------------------------------------------------
    # PRIORITY 2 → EFFICIENCY
    # --------------------------------------------------

    block = TRAIL_INTERPRETATION.get("efficiency", {}).get(eff)
    if block:
        interpretation = block["interpretation"]
        coaching = block["coaching"]

    # --------------------------------------------------
    # PRIORITY 3 → DURABILITY override
    # --------------------------------------------------

    if dur == "drifting":
        block = TRAIL_INTERPRETATION.get("durability", {}).get("drifting")
        if block:
            interpretation = block["interpretation"]
            coaching = block["coaching"]

    # --------------------------------------------------
    # PRIORITY 4 → ENVIRONMENT override
    # --------------------------------------------------

    if env != "none":
        block = TRAIL_INTERPRETATION.get("environment", {}).get(env)
        if block:
            interpretation = block["interpretation"]
            coaching = block["coaching"]

    # --------------------------------------------------
    # FALLBACK (state-based)
    # --------------------------------------------------

    if not interpretation:
        block = TRAIL_INTERPRETATION.get("efficiency", {}).get(state)
        if block:
            interpretation = block["interpretation"]
            coaching = block["coaching"]

    return interpretation, coaching

# --------------------------------------------------
# MAIN ENTRY
# --------------------------------------------------

def run_trail_execution(context: dict):

    df = context.get("_df_scope_full")

    if df is None or df.empty:
        return

    # --- RUN + TERRAIN GATE ---
    if not _has_meaningful_trail_runs(df):
        return

    # --------------------------------------------------
    # METRIC EXTRACTION (minimal + robust)
    # --------------------------------------------------

    metrics = {}

    # grade (%)
    if "grade" in df.columns:
        metrics["grade"] = float(df["grade"].mean())

    # cadence
    if "cadence" in df.columns:
        metrics["cadence"] = float(df["cadence"].mean())
        metrics["cadence_var"] = float(df["cadence"].std())

    # HR ratio (vs threshold if available)
    if "heartrate" in df.columns:
        hr = float(df["heartrate"].mean())
        lthr = context.get("athlete", {}).get("lthr", 160)
        metrics["hr_ratio"] = hr / lthr if lthr else 0

    # decoupling
    if "decoupling" in df.columns:
        metrics["decoupling"] = float(df["decoupling"].mean())

    # speed drop (proxy)
    if "speed" in df.columns:
        s = df["speed"]
        if len(s) > 0:
            metrics["speed_drop"] = float((s.max() - s.min()) / max(s.max(), 1))

    # temperature
    if "temperature" in df.columns:
        metrics["temp"] = float(df["temperature"].mean())

    # --------------------------------------------------
    # APPLY RULES
    # --------------------------------------------------

    signals, flags = evaluate_rules(metrics)

    # apply defaults
    for k, v in TRAIL_DEFAULTS.items():
        signals.setdefault(k, v)

    # --------------------------------------------------
    # CLASSIFY
    # --------------------------------------------------

    classification = classify_execution(signals, flags)

    interpretation, coaching = build_interpretation(
        signals,
        flags,
        classification
    )

    terrain_execution = {
        **classification,
        "interpretation": interpretation,
        "coaching_implication": coaching,
        "flags": flags   # keep for downstream use/debug
    }

    # --------------------------------------------------
    # INJECT INTO TIER-3
    # --------------------------------------------------

    pi = context.get("performance_intelligence", {})

    pi["run_terrain_execution"] = terrain_execution

    context["performance_intelligence"] = pi

    return