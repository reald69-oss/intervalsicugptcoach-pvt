"""
Energy System Progression Engine (ESPE)
Version: v1
Stateless, deterministic, window-comparison based.

Consumes:
    - power_curve block injected by Worker
Produces:
    - energy_system_progression section
"""

from typing import Dict, Any


ESPE_VERSION = "espe_v1"


# -------------------------------------------------------------------
# Public Entry Point
# -------------------------------------------------------------------

def run_espe(power_curve_block: Dict[str, Any]) -> Dict[str, Any]:
    """
    power_curve_block structure expected:

    {
        "Ride": {
            "current": {...},
            "previous": {...},
            "window_days": 90
        },
        "Run": {...}
    }
    """

    result = {
        "version": ESPE_VERSION,
        "sports": {}
    }

    if not power_curve_block:
        return _unsupported("missing power curve data")

    for sport, data in power_curve_block.items():

        if not _valid_curve_block(data):
            result["sports"][sport] = _unsupported("invalid or insufficient data")
            continue

        result["sports"][sport] = _process_sport(sport, data)

    return result


# -------------------------------------------------------------------
# Core Logic
# -------------------------------------------------------------------

def _process_sport(sport: str, data: Dict[str, Any]) -> Dict[str, Any]:

    current = data["current"]
    previous = data["previous"]

    delta = _compute_delta_percent(current, previous)

    glycolytic_bias = _safe_ratio(current.get("1m"), current.get("20m"))
    aerobic_durability = _safe_ratio(current.get("60m"), current.get("5m"))

    system_status = _classify_system_status(sport, delta)
    plateau = _detect_plateau(sport, delta)

    balance_score = _compute_balance_score(glycolytic_bias, aerobic_durability)

    adaptation_bias = _derive_adaptation_bias(system_status)

    return {
        "supported": True,
        "delta_percent": delta,
        "system_status": system_status,
        "derived_metrics": {
            "glycolytic_bias_ratio": glycolytic_bias,
            "aerobic_durability_ratio": aerobic_durability,
            "system_balance_score": balance_score
        },
        "plateau_detected": plateau,
        "adaptation_bias": adaptation_bias
    }


# -------------------------------------------------------------------
# Calculations
# -------------------------------------------------------------------

def _compute_delta_percent(current: Dict[str, float],
                           previous: Dict[str, float]) -> Dict[str, float]:

    delta = {}

    for k in current:
        if k in previous and previous[k] > 0:
            delta[k] = round(
                ((current[k] - previous[k]) / previous[k]) * 100,
                2
            )

    return delta


def _safe_ratio(a: float, b: float) -> float:
    if not a or not b or b == 0:
        return 0.0
    return round(a / b, 2)


# -------------------------------------------------------------------
# Classification Logic (v1 thresholds)
# -------------------------------------------------------------------

def _classify_system_status(sport: str,
                            delta: Dict[str, float]) -> Dict[str, str]:

    thresholds = _sport_thresholds(sport)

    return {
        "anaerobic": _band(delta.get("1m", 0), thresholds["anaerobic"]),
        "vo2": _band(delta.get("5m", 0), thresholds["vo2"]),
        "threshold": _band(delta.get("20m", 0), thresholds["threshold"]),
        "aerobic_durability": _band(delta.get("60m", 0), thresholds["aerobic"])
    }


def _band(value: float, bands: Dict[str, float]) -> str:
    if value >= bands["strong"]:
        return "strong_gain"
    if value >= bands["moderate"]:
        return "moderate_gain"
    if value >= bands["mild"]:
        return "mild_gain"
    if value <= bands["decline"]:
        return "decline"
    return "stable"


def _sport_thresholds(sport: str) -> Dict[str, Dict[str, float]]:

    if sport == "Run":
        return {
            "anaerobic": {"strong": 2.0, "moderate": 1.0, "mild": 0.5, "decline": -1.0},
            "vo2": {"strong": 2.0, "moderate": 1.0, "mild": 0.5, "decline": -1.0},
            "threshold": {"strong": 1.0, "moderate": 0.5, "mild": 0.3, "decline": -0.8},
            "aerobic": {"strong": 1.0, "moderate": 0.5, "mild": 0.3, "decline": -0.8}
        }

    # Ride default
    return {
        "anaerobic": {"strong": 3.0, "moderate": 1.5, "mild": 0.8, "decline": -1.5},
        "vo2": {"strong": 3.0, "moderate": 1.5, "mild": 0.8, "decline": -1.5},
        "threshold": {"strong": 2.0, "moderate": 1.0, "mild": 0.5, "decline": -1.0},
        "aerobic": {"strong": 1.5, "moderate": 0.7, "mild": 0.4, "decline": -1.0}
    }


def _detect_plateau(sport: str, delta: Dict[str, float]) -> bool:

    threshold_gain = delta.get("20m", 0)

    if sport == "Run":
        return threshold_gain < 0.5

    return threshold_gain < 1.0


def _compute_balance_score(glycolytic: float,
                           aerobic: float) -> float:

    # ideal glycolytic/aerobic ratio band around 1.8 (Ride)
    ideal = 1.8

    if glycolytic == 0:
        return 0.0

    deviation = abs(glycolytic - ideal) / ideal
    score = max(0.0, 1 - deviation)

    return round(score, 2)


def _derive_adaptation_bias(system_status: Dict[str, str]) -> str:

    if system_status["vo2"] in ("strong_gain", "moderate_gain"):
        return "vo2_dominant"

    if system_status["threshold"] in ("strong_gain", "moderate_gain"):
        return "threshold_dominant"

    return "balanced"


# -------------------------------------------------------------------
# Validation
# -------------------------------------------------------------------

def _valid_curve_block(data: Dict[str, Any]) -> bool:
    if "current" not in data or "previous" not in data:
        return False
    return bool(data["current"]) and bool(data["previous"])


def _unsupported(reason: str) -> Dict[str, Any]:
    return {
        "supported": False,
        "reason": reason
    }