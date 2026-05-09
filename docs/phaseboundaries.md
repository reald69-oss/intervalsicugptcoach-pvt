    # ================================================================
    # 🧠 PHASE DETECTION ENGINE v2.1
    # ================================================================
    # V2 separates:
    #   1) PhaseBoundaries  → raw weekly load-pattern classification
    #   2) PhaseRulesV2     → sequence-aware refinement layer
    #
    # PhaseBoundaries remain deterministic and threshold-based.
    # PhaseRulesV2 is applied AFTER raw phase detection.
    #
    # Core metrics:
    #   tss        → weekly training load
    #   delta      → smoothed week-to-week % change in TSS
    #   ctl        → chronic training load / fitness
    #   atl        → acute training load / fatigue
    #   tsb        → ctl - atl
    #   acwr       → atl / ctl
    #
    # V1 classified load pattern only.
    # V2 classifies load pattern + periodisation context.
    # ================================================================


    "PhaseBoundaries": {

        "Recovery": {
            "trend_min": -1.00,
            "trend_max": -0.30,
            "acwr_max": 0.85,
            "tsb_min": 5
        },

        "Taper": {
            "trend_min": -0.40,
            "trend_max": -0.12,
            "acwr_max": 1.00,
            "tsb_min": 0
        },

        "Deload": {
            "trend_min": -0.12,
            "trend_max": -0.01,
            "acwr_max": 1.10
        },

        "Base": {
            "trend_min": -0.01,
            "trend_max": 0.05,
            "acwr_max": 1.15
        },

        "Peak": {
            "trend_min": -0.15,
            "trend_max": 0.02,
            "acwr_max": 1.00,
            "tsb_min": 8
        },

        "Build": {
            "trend_min": 0.03,
            "trend_max": 0.30,
            "acwr_max": 1.30
        }
    },

    # ================================================================
    # 🧠 PHASE RULES v2 — CORRECTED
    # ================================================================

    "PhaseRulesV2": {

        "version": "phase_rules_v2.1",

        "execution_order": [
            "peak_after_taper",
            "true_recovery_strict",
            "transition_after_recovery",
            "prevent_false_peak",
            "default_raw_phase"
        ],

        # ------------------------------------------------------------
        # RULE 1 — PEAK AFTER TAPER
        # ------------------------------------------------------------
        "peak_after_taper": {
            "if": {
                "prev_phase_final": "Taper",
                "delta_gt": 0.00,
                "acwr_lte": 1.10
            },
            "then": {
                "phase_final": "Peak"
            }
        },

        # ------------------------------------------------------------
        # RULE 2 — TRUE RECOVERY (RELATIVE, NOT ABSOLUTE)
        # ------------------------------------------------------------
        "true_recovery_strict": {
            "if": {
                "acwr_lt": 0.65,
                "delta_lt": -0.10,
                "tsb_gt": 5
            },
            "then": {
                "phase_final": "Recovery"
            }
        },

        # ------------------------------------------------------------
        # RULE 3 — TRANSITION AFTER RECOVERY (UPDATED)
        # ------------------------------------------------------------
        "transition_after_recovery": {
            "if": {
                "prev_phase_final": "Recovery",
                "abs_delta_lt": 0.15
            },
            "then": {
                "phase_final": "Transition"
            }
        },

        # ------------------------------------------------------------
        # RULE 4 — PREVENT FALSE PEAK
        # ------------------------------------------------------------
        "prevent_false_peak": {
            "if": {
                "phase_raw": "Peak",
                "tsb_lt": 5
            },
            "then": {
                "phase_final": "Base"
            }
        },

        # ------------------------------------------------------------
        # RULE 5 — DEFAULT
        # ------------------------------------------------------------
        "default_raw_phase": {
            "then": {
                "phase_final": "phase_raw"
            }
        }
    }
---

## ENGINE SUMMARY

```text
1. Aggregate events into ISO weeks
2. Compute weekly TSS
3. Use weekly CTL / ATL
4. Compute TSB = CTL - ATL
5. Compute delta = smoothed pct_change(TSS)
6. Compute ACWR = ATL / CTL
7. Run PhaseBoundaries → phase_raw
8. Run PhaseRulesV2 → phase_final
V1 = raw load-pattern classifier
V2 = periodisation-aware phase refinement

tss                = sum(icu_training_load)
ctl                = icu_ctl last value in week
atl                = icu_atl last value in week
tsb                = ctl - atl
delta_raw          = pct_change(tss)
delta              = EMA(delta_raw, span=3)
acwr               = atl / ctl
phase_raw          = PhaseBoundaries result
prev_phase_final   = prior week final V2 phase

FOR phase in PhaseBoundaries:

    IF:
        trend_min <= delta <= trend_max
        AND acwr <= acwr_max
        AND tsb >= tsb_min (if defined)
        AND tsb <= tsb_max (if defined)

    THEN:
        phase_raw = matched_phase
        BREAK

ELSE:
    phase_raw = "Transition"


RULE 1:
IF prev_phase_final == "Taper"
AND delta > 0
AND acwr <= 1.10
THEN phase_final = "Peak"


RULE 2:
IF acwr < 0.65
AND delta < -0.10
AND tsb > 5
THEN phase_final = "Recovery"


RULE 3:
IF prev_phase_final == "Recovery"
AND abs(delta) < 0.15
THEN phase_final = "Transition"


RULE 4:
IF phase_raw == "Peak"
AND tsb < 5
THEN phase_final = "Base"


RULE 5:
ELSE phase_final = phase_raw

{
  "week_start": "YYYY-MM-DD",
  "phase_raw": "string",
  "phase_final": "string",
  "tss": number,
  "delta": number,
  "acwr": number,
  "tsb": number,
  "ctl": number,
  "atl": number
}

- deterministic
- first-match wins
- PhaseBoundaries remains load-pattern based
- PhaseRulesV2 adds sequence awareness
- projected and historical weeks use same pipeline
- phase_raw is preserved
- phase_final is used for reporting