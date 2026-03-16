#ADE V1.0

ADE_VERSION = "ade_v1"


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

    decision = {
        "directive": directive,
        "operational_state": operational_state,
        "adaptation_focus": system_state,
        "risk_flag": risk_flag,
        "forecast_context": fatigue_class,
        "load_trend": load_trend,
        "version": ADE_VERSION
    }

    context["adaptive_decision"] = decision

    return {"adaptive_decision": decision}