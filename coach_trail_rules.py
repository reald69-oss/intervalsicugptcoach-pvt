# coach_trail_rules.py

"""
Trail Execution Rules — Deterministic Knowledge Layer
Aligned with URF v5.1 Tier-3 architecture

Purpose:
- Provide static thresholds and rule definitions
- No logic, no computation
- Consumed by tier3_trail_execution.py
"""

# --------------------------------------------------
# VERSION
# --------------------------------------------------

TRAIL_RULES = {
    "version": "v1.0",

    # Gradient bands (%)
    "gradient": {
        "moderate": 6,
        "steep": 10,
        "very_steep": 12,
        "extreme": 15
    },

    # Cadence thresholds (spm)
    "cadence": {
        "low": 70,
        "unstable_var": 15
    },

    # Decoupling (%)
    "decoupling": {
        "stable": 4,
        "drifting": 6,
        "failing": 10
    },

    # Environment
    "environment": {
        "heat_temp": 20,      # °C
        "altitude": 2000      # m
    }
}


# --------------------------------------------------
# DEFAULT STATES (fallback if no rule fires)
# --------------------------------------------------

TRAIL_DEFAULTS = {
    "efficiency": "moderate",
    "durability": "stable",
    "locomotion": "running_economical",
    "environment": "none"
}


# --------------------------------------------------
# EXECUTION RULES
# --------------------------------------------------

TRAIL_EXECUTION_RULES = [

    # -------------------------------
    # LOCOMOTION
    # -------------------------------

    {
        "id": "LOC_01",
        "type": "locomotion",
        "conditions": {
            "grade_min": 12,
            "cadence_max": 75
        },
        "result": "hiking_preferred",
        "priority": 2
    },

    # -------------------------------
    # EFFICIENCY (NEGATIVE)
    # -------------------------------

    {
        "id": "GRAD_01",
        "type": "efficiency",
        "conditions": {
            "grade_min": 10,
            "hr_ratio_min": 1.0
        },
        "result": "overexerting",
        "priority": 1
    },

    {
        "id": "GRAD_03",
        "type": "efficiency",
        "conditions": {
            "grade_min": 10,
            "speed_drop_min": 0.3
        },
        "result": "pace_collapse",
        "priority": 1
    },

    # -------------------------------
    # EFFICIENCY (POSITIVE)
    # -------------------------------

    {
        "id": "GRAD_02",
        "type": "efficiency",
        "conditions": {
            "grade_min": 8,
            "hr_ratio_max": 0.9
        },
        "result": "efficient",
        "priority": 3
    },

    # -------------------------------
    # DURABILITY
    # -------------------------------

    {
        "id": "DUR_01",
        "type": "durability",
        "conditions": {
            "decoupling_min": 6
        },
        "result": "drifting",
        "priority": 2
    },

    {
        "id": "DUR_02",
        "type": "durability",
        "conditions": {
            "decoupling_max": 4
        },
        "result": "stable",
        "priority": 3
    },

    # -------------------------------
    # ENVIRONMENT
    # -------------------------------

    {
        "id": "ENV_01",
        "type": "environment",
        "conditions": {
            "temp_min": 20,
            "hr_ratio_min": 0.9
        },
        "result": "heat",
        "priority": 1
    }
]


# --------------------------------------------------
# FLAGS (non-exclusive signals)
# --------------------------------------------------

TRAIL_FLAGS = [

    {
        "id": "TER_01",
        "conditions": {
            "grade_min": 12,
            "hr_ratio_min": 0.95
        },
        "flag": "direct_climb_penalty"
    },

    {
        "id": "TER_02",
        "conditions": {
            "grade_min": 15,
            "speed_drop_min": 0.25
        },
        "flag": "switchback_opportunity"
    }
]