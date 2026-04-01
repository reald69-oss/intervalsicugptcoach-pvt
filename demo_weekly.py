
# WHEN UPDATING THIS YOU MUST CHANGE ALL Null TO None, true to TRUE, false to False
# Ensure than you have only this
# DEMO_WEEKLY = {
#     "semantic_graph": {
# and closing bracket }

DEMO_WEEKLY = {
    "meta": {
      "framework": "V5.1 Unified Reporting Framework",
      "version": "v16.17",
      "generated_at": {
        "local": "2026-04-01T11:23:06+02:00"
      },
      "timezone": "Europe/Zurich",
      "athlete": {
        "identity": {
          "id": "1914741",
          "name": "Demo Athlete",
          "firstname": "Demo",
          "lastname": "Athlete",
          "sex": "M",
          "dob": "1975-01-01",
          "country": "Switzerland",
          "city": "Zurich",
          "timezone": "Europe/Zurich",
          "profile_image": ""
        },
        "profile": {
          "ftp": 300,
          "eftp": 300,
          "ftp_kg": 4.12,
          "lthr": 157,
          "max_hr": 177,
          "threshold_pace": None,
          "pace_units": None,
          "primary_sport": "ride",
          "dominant_sport": "ride",
          "vo2max_garmin": 72,
          "lactate_mmol_l": 1.9,
          "lactate_power": 185
        },
        "profiles": {
          "ride": {
            "ftp": 300,
            "eftp": 300,
            "w_prime": 24198,
            "p_max": 942,
            "lthr": 157,
            "max_hr": 177,
            "threshold_pace": None,
            "pace_units": None,
            "power_zones": [
              55,
              75,
              90,
              105,
              120,
              150
            ],
            "hr_zones": [
              126,
              140,
              146,
              156,
              160,
              165,
              177
            ],
            "pace_zones": None,
            "vo2max_garmin": 72,
            "lactate_mmol_l": 1.9,
            "lactate_power": 185
          },
          "run": {
            "ftp": 327,
            "eftp": 329,
            "w_prime": 28265,
            "p_max": 523,
            "lthr": 157,
            "max_hr": 177,
            "threshold_pace": 3.5714285,
            "pace_units": "M_PER_SEC",
            "power_zones": [
              55,
              75,
              90,
              105,
              120,
              150,
              999
            ],
            "hr_zones": [
              132,
              140,
              148,
              156,
              161,
              165,
              177
            ],
            "pace_zones": [
              77.5,
              87.7,
              94.3,
              100,
              103.4,
              111.5,
              999
            ],
            "vo2max_garmin": None,
            "lactate_mmol_l": None,
            "lactate_power": None
          },
          "swim": {
            "ftp": None,
            "eftp": None,
            "w_prime": None,
            "p_max": None,
            "lthr": 157,
            "max_hr": 177,
            "threshold_pace": None,
            "pace_units": "SECS_100M",
            "power_zones": None,
            "hr_zones": [
              132,
              140,
              148,
              156,
              161,
              165,
              177
            ],
            "pace_zones": None,
            "vo2max_garmin": None,
            "lactate_mmol_l": None,
            "lactate_power": None
          },
          "ski": {
            "ftp": None,
            "eftp": None,
            "w_prime": None,
            "p_max": None,
            "lthr": 157,
            "max_hr": 177,
            "threshold_pace": None,
            "pace_units": "MINS_KM",
            "power_zones": None,
            "hr_zones": [
              125,
              140,
              146,
              156,
              160,
              165,
              177
            ],
            "pace_zones": None,
            "vo2max_garmin": None,
            "lactate_mmol_l": None,
            "lactate_power": None
          }
        },
        "global": {
          "resting_hr": 40,
          "weight": 72.9,
          "height": 1.81,
          "sex": "M"
        },
        "context": {}
      },
      "report_type": "weekly",
      "render_mode": "full+metrics",
      "window_days": 7,
      "period": "2026-03-25 \u2192 2026-03-31",
      "report_header": {
        "title": "Weekly Training Report",
        "scope": "Detailed analysis of the last 7 days of training activity",
        "data_sources": "7-day full activities, 42-day wellness, 90 day light activities",
        "intended_use": "Day-to-day coaching decisions, intensity balance, short-term fatigue and recovery management"
      },
      "events": {
        "is_event_block": True,
        "event_block_count": 8,
        "render": True
      },
      "phases_summary": {
        "is_phase_block": True,
        "phase_block_count": 10,
        "notes": "Macro-level sequential phase summary, intended for ChatGPT / structured UI rendering."
      },
      "resolution": {
        "CTL": "authoritative",
        "ATL": "authoritative",
        "TSB": "authoritative",
        "zones": "authoritative",
        "derived_metrics": "full",
        "performance_intelligence": "acute_full_7d",
        "energy_system_progression": "full",
        "insights": "tactical"
      }
    },
    "performance_intelligence": {
      "acute": {
        "anaerobic_repeatability": {
          "max_depletion_pct_7d": {
            "name": "max_depletion_pct_7d",
            "display_name": "Max W\u2032 Depletion (7-day)",
            "value": 0.7925035126869989,
            "framework": "W\u2032 Depletion & Repeatability Model (WDRM)",
            "formula": "Max W\u2032 depletion observed (7d)",
            "criteria": {
              "low": "<0.3 \u2014 shallow depletion",
              "moderate": "0.3\u20130.6 \u2014 meaningful anaerobic stimulus",
              "high": ">0.6 \u2014 deep depletion event"
            },
            "semantic_state": "high",
            "thresholds": {},
            "phase_context": None,
            "classification": "informational",
            "metric_confidence": "contextual",
            "interpretation": "WDRM (W\u2032 Depletion & Repeatability Metric) quantifies depth and frequency of anaerobic reserve depletion across sessions. Higher values reflect repeated deep supra-threshold exposure.",
            "coaching_implication": {
              "low": "Anaerobic exposure controlled \u2014 maintain structure.",
              "moderate": "Moderate anaerobic load \u2014 ensure recovery spacing.",
              "high": "High W\u2032 depletion \u2014 monitor recovery and intensity stacking."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "mean_depletion_pct_7d": {
            "name": "mean_depletion_pct_7d",
            "display_name": "Mean W\u2032 Depletion (7-day)",
            "value": 0.25881123587545607,
            "framework": "W\u2032 Depletion & Repeatability Model (WDRM)",
            "formula": "Mean W\u2032 depletion across sessions (7d)",
            "criteria": {
              "low": "<0.2 \u2014 minimal anaerobic strain",
              "moderate": "0.2\u20130.45 \u2014 controlled anaerobic contribution",
              "high": ">0.45 \u2014 repeated deep depletion"
            },
            "semantic_state": "moderate",
            "thresholds": {},
            "phase_context": None,
            "classification": "informational",
            "metric_confidence": "contextual",
            "interpretation": "WDRM (W\u2032 Depletion & Repeatability Metric) quantifies depth and frequency of anaerobic reserve depletion across sessions. Higher values reflect repeated deep supra-threshold exposure.",
            "coaching_implication": {
              "low": "Anaerobic exposure controlled \u2014 maintain structure.",
              "moderate": "Moderate anaerobic load \u2014 ensure recovery spacing.",
              "high": "High W\u2032 depletion \u2014 monitor recovery and intensity stacking."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "moderate_depletion_sessions_7d": {
            "name": "moderate_depletion_sessions_7d",
            "display_name": "Moderate W\u2032 Depletion Sessions (7-day)",
            "value": 2,
            "framework": "W\u2032 Depletion & Repeatability Model (WDRM)",
            "formula": None,
            "criteria": {},
            "semantic_state": "unclassified",
            "thresholds": {
              "green": [
                0,
                3
              ],
              "amber": [
                4,
                6
              ],
              "red": [
                7,
                10
              ]
            },
            "phase_context": None,
            "classification": "green",
            "metric_confidence": "contextual",
            "interpretation": "WDRM (W\u2032 Depletion & Repeatability Metric) quantifies depth and frequency of anaerobic reserve depletion across sessions. Higher values reflect repeated deep supra-threshold exposure.",
            "coaching_implication": {
              "low": "Anaerobic exposure controlled \u2014 maintain structure.",
              "moderate": "Moderate anaerobic load \u2014 ensure recovery spacing.",
              "high": "High W\u2032 depletion \u2014 monitor recovery and intensity stacking."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "high_depletion_sessions_7d": {
            "name": "high_depletion_sessions_7d",
            "display_name": "High W\u2032 Depletion Sessions (7-day)",
            "value": 2,
            "framework": "W\u2032 Depletion & Repeatability Model (WDRM)",
            "formula": None,
            "criteria": {},
            "semantic_state": "unclassified",
            "thresholds": {
              "green": [
                0,
                2
              ],
              "amber": [
                3,
                4
              ]
            },
            "phase_context": None,
            "classification": "green",
            "metric_confidence": "contextual",
            "interpretation": "WDRM (W\u2032 Depletion & Repeatability Metric) quantifies depth and frequency of anaerobic reserve depletion across sessions. Higher values reflect repeated deep supra-threshold exposure.",
            "coaching_implication": {
              "low": "Anaerobic exposure controlled \u2014 maintain structure.",
              "moderate": "Moderate anaerobic load \u2014 ensure recovery spacing.",
              "high": "High W\u2032 depletion \u2014 monitor recovery and intensity stacking."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "total_joules_above_ftp_7d": {
            "name": "total_joules_above_ftp_7d",
            "display_name": "Total Work Above FTP (7-day)",
            "value": 112009.0,
            "framework": "W\u2032 Depletion & Repeatability Model (WDRM)",
            "formula": "Total work above FTP (7d)",
            "criteria": {
              "low": "<100kJ \u2014 low anaerobic stimulus",
              "moderate": "100\u2013250kJ \u2014 structured intensity",
              "high": ">250kJ \u2014 heavy anaerobic load"
            },
            "semantic_state": "unclassified",
            "thresholds": {},
            "phase_context": None,
            "classification": "informational",
            "metric_confidence": "high",
            "interpretation": "WDRM (W\u2032 Depletion & Repeatability Metric) quantifies depth and frequency of anaerobic reserve depletion across sessions. Higher values reflect repeated deep supra-threshold exposure.",
            "coaching_implication": {
              "low": "Anaerobic exposure controlled \u2014 maintain structure.",
              "moderate": "Moderate anaerobic load \u2014 ensure recovery spacing.",
              "high": "High W\u2032 depletion \u2014 monitor recovery and intensity stacking."
            },
            "related_metrics": [],
            "context_window": "7d"
          }
        },
        "model_diagnostics": {
          "w_prime_divergence_7d": {
            "name": "w_prime_divergence_7d",
            "display_name": "W\u2032 Utilisation Divergence (7-day)",
            "value": -0.04118876412454392,
            "framework": "Skiba Critical Power",
            "formula": None,
            "criteria": {},
            "semantic_state": "unclassified",
            "thresholds": {
              "green": [
                -0.1,
                0.15
              ],
              "amber": [
                0.15,
                0.3
              ],
              "red": [
                0.3,
                1.0
              ]
            },
            "phase_context": None,
            "classification": "green",
            "metric_confidence": "contextual",
            "interpretation": "Difference between observed W\u2032 depletion behaviour and expected endurance baseline. Positive values indicate higher-than-normal anaerobic utilisation, while negative values indicate lower-than-expected supra-threshold engagement.",
            "coaching_implication": {
              "green": "Anaerobic utilisation within normal endurance range.",
              "amber": "Elevated W\u2032 usage \u2014 indicates VO\u2082max or anaerobic stimulus.",
              "red": "Very high W\u2032 utilisation \u2014 likely race load or repeated high-intensity sessions."
            },
            "related_metrics": [],
            "context_window": "7d"
          }
        },
        "durability": {
          "mean_decoupling_7d": {
            "name": "mean_decoupling_7d",
            "display_name": "Mean Decoupling (7-day)",
            "value": 9.051464414285714,
            "framework": "Intensity Stability & Durability Model (ISDM)",
            "formula": "Mean HR\u2013Power decoupling (%) (7d)",
            "criteria": {
              "stable": "<5 \u2014 strong durability",
              "moderate": "5\u20138 \u2014 emerging fatigue",
              "high": ">8 \u2014 durability limitation"
            },
            "semantic_state": "high",
            "thresholds": {},
            "phase_context": None,
            "classification": "informational",
            "metric_confidence": "contextual",
            "interpretation": "ISDM (Intensity Stability & Durability Metric) reflects decoupling behaviour under fatigue. Elevated values indicate cardiovascular drift or durability stress.",
            "coaching_implication": {
              "stable": "Durability stable \u2014 cardiovascular drift controlled.",
              "fatigue": "Elevated drift \u2014 consider aerobic consolidation.",
              "severe": "Significant durability stress \u2014 reduce load."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "max_decoupling_7d": {
            "name": "max_decoupling_7d",
            "display_name": "Max Decoupling (7-day)",
            "value": 21.18352,
            "framework": "Intensity Stability & Durability Model (ISDM)",
            "formula": "Max HR\u2013Power decoupling (%) (7d)",
            "criteria": {
              "low": "<6 \u2014 stable session",
              "moderate": "6\u201310 \u2014 moderate drift",
              "high": ">10 \u2014 significant durability stress"
            },
            "semantic_state": "high",
            "thresholds": {},
            "phase_context": None,
            "classification": "informational",
            "metric_confidence": "contextual",
            "interpretation": "ISDM (Intensity Stability & Durability Metric) reflects decoupling behaviour under fatigue. Elevated values indicate cardiovascular drift or durability stress.",
            "coaching_implication": {
              "stable": "Durability stable \u2014 cardiovascular drift controlled.",
              "fatigue": "Elevated drift \u2014 consider aerobic consolidation.",
              "severe": "Significant durability stress \u2014 reduce load."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "high_drift_sessions_7d": {
            "name": "high_drift_sessions_7d",
            "display_name": "High Drift Sessions (7-day)",
            "value": 5,
            "framework": "Intensity Stability & Durability Model (ISDM)",
            "formula": None,
            "criteria": {},
            "semantic_state": "unclassified",
            "thresholds": {
              "green": [
                0,
                2
              ],
              "amber": [
                3,
                4
              ]
            },
            "phase_context": None,
            "classification": "amber",
            "metric_confidence": "contextual",
            "interpretation": "ISDM (Intensity Stability & Durability Metric) reflects decoupling behaviour under fatigue. Elevated values indicate cardiovascular drift or durability stress.",
            "coaching_implication": {
              "stable": "Durability stable \u2014 cardiovascular drift controlled.",
              "fatigue": "Elevated drift \u2014 consider aerobic consolidation.",
              "severe": "Significant durability stress \u2014 reduce load."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "long_sessions_7d": {
            "name": "long_sessions_7d",
            "display_name": "Long Endurance Sessions (7-day)",
            "value": 1,
            "framework": "Intensity Stability & Durability Model (ISDM)",
            "formula": "Count of long endurance sessions (7d)",
            "criteria": {
              "low": "0 \u2014 no long sessions",
              "moderate": "1\u20132 \u2014 adequate durability stimulus",
              "high": "3+ \u2014 high endurance demand"
            },
            "semantic_state": "moderate",
            "thresholds": {},
            "phase_context": None,
            "classification": "informational",
            "metric_confidence": "high",
            "interpretation": "ISDM (Intensity Stability & Durability Metric) reflects decoupling behaviour under fatigue. Elevated values indicate cardiovascular drift or durability stress.",
            "coaching_implication": {
              "stable": "Durability stable \u2014 cardiovascular drift controlled.",
              "fatigue": "Elevated drift \u2014 consider aerobic consolidation.",
              "severe": "Significant durability stress \u2014 reduce load."
            },
            "related_metrics": [],
            "context_window": "7d"
          }
        },
        "neural_density": {
          "rolling_joules_above_ftp_7d": {
            "name": "rolling_joules_above_ftp_7d",
            "display_name": "Rolling Work Above FTP (7-day)",
            "value": 112009.0,
            "framework": "Neural Density Load Index (NDLI)",
            "formula": None,
            "criteria": {},
            "semantic_state": "unclassified",
            "thresholds": {
              "green": [
                0,
                150000
              ],
              "amber": [
                150000,
                250000
              ],
              "red": [
                250000,
                1000000
              ]
            },
            "phase_context": None,
            "classification": "green",
            "metric_confidence": "contextual",
            "interpretation": "NDLI (Neural Density Load Index) captures clustering of high-intensity work within short time windows (e.g. 72h). High density increases recovery demand.",
            "coaching_implication": {
              "balanced": "Intensity density well distributed.",
              "clustered": "High short-term clustering \u2014 monitor recovery.",
              "overloaded": "Neural load accumulation high \u2014 reduce intensity density."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "high_intensity_days_7d": {
            "name": "high_intensity_days_7d",
            "display_name": "High-Intensity Days (7-day)",
            "value": 3,
            "framework": "Neural Density Load Index (NDLI)",
            "formula": None,
            "criteria": {},
            "semantic_state": "unclassified",
            "thresholds": {
              "green": [
                0,
                2
              ],
              "amber": [
                3,
                4
              ],
              "red": [
                5,
                7
              ]
            },
            "phase_context": None,
            "classification": "amber",
            "metric_confidence": "contextual",
            "interpretation": "NDLI (Neural Density Load Index) captures clustering of high-intensity work within short time windows (e.g. 72h). High density increases recovery demand.",
            "coaching_implication": {
              "balanced": "Intensity density well distributed.",
              "clustered": "High short-term clustering \u2014 monitor recovery.",
              "overloaded": "Neural load accumulation high \u2014 reduce intensity density."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "mean_if_7d": {
            "name": "mean_if_7d",
            "display_name": "Mean Intensity Factor (7-day)",
            "value": 0.7049880937499999,
            "framework": "Neural Density Load Index (NDLI)",
            "formula": "Mean Intensity Factor (7d)",
            "criteria": {
              "low": "<0.65 \u2014 low intensity bias",
              "moderate": "0.65\u20130.8 \u2014 endurance mix",
              "high": ">0.8 \u2014 intensity heavy"
            },
            "semantic_state": "moderate",
            "thresholds": {},
            "phase_context": None,
            "classification": "informational",
            "metric_confidence": "high",
            "interpretation": "NDLI (Neural Density Load Index) captures clustering of high-intensity work within short time windows (e.g. 72h). High density increases recovery demand.",
            "coaching_implication": {
              "balanced": "Intensity density well distributed.",
              "clustered": "High short-term clustering \u2014 monitor recovery.",
              "overloaded": "Neural load accumulation high \u2014 reduce intensity density."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "mean_efficiency_factor_7d": {
            "name": "mean_efficiency_factor_7d",
            "display_name": "Mean Efficiency Factor (7-day)",
            "value": 1.8153863285714285,
            "framework": "Neural Density Load Index (NDLI)",
            "formula": "Mean Efficiency Factor (7d)",
            "criteria": {
              "low": "<1.7 \u2014 low aerobic efficiency",
              "moderate": "1.7\u20132.1 \u2014 stable efficiency",
              "high": ">2.1 \u2014 strong aerobic efficiency"
            },
            "semantic_state": "moderate",
            "thresholds": {},
            "phase_context": None,
            "classification": "informational",
            "metric_confidence": "contextual",
            "interpretation": "NDLI (Neural Density Load Index) captures clustering of high-intensity work within short time windows (e.g. 72h). High density increases recovery demand.",
            "coaching_implication": {
              "balanced": "Intensity density well distributed.",
              "clustered": "High short-term clustering \u2014 monitor recovery.",
              "overloaded": "Neural load accumulation high \u2014 reduce intensity density."
            },
            "related_metrics": [],
            "context_window": "7d"
          },
          "mean_variability_index_7d": {
            "name": "mean_variability_index_7d",
            "display_name": "Mean Variability Index (7-day)",
            "value": 1.0938127142857144,
            "framework": "Neural Density Load Index (NDLI)",
            "formula": "Mean Variability Index (7d)",
            "criteria": {
              "steady": "<1.05 \u2014 steady pacing",
              "moderate": "1.05\u20131.15 \u2014 mixed intensity",
              "high": ">1.15 \u2014 stochastic / variable load"
            },
            "semantic_state": "moderate",
            "thresholds": {},
            "phase_context": None,
            "classification": "informational",
            "metric_confidence": "contextual",
            "interpretation": "NDLI (Neural Density Load Index) captures clustering of high-intensity work within short time windows (e.g. 72h). High density increases recovery demand.",
            "coaching_implication": {
              "balanced": "Intensity density well distributed.",
              "clustered": "High short-term clustering \u2014 monitor recovery.",
              "overloaded": "Neural load accumulation high \u2014 reduce intensity density."
            },
            "related_metrics": [],
            "context_window": "7d"
          }
        }
      },
      "chronic": {},
      "version": "PI_v1.4",
      "load_distribution": {
        "rest_days": 1,
        "context_window": "7d"
      },
      "training_state": {
        "framework": "Autonomic\u2013Load Interaction Model",
        "interpretation": "Load\u2013Recovery state describing the interaction between training load (ATL vs CTL) and autonomic recovery (HRV ratio). Balanced indicates load and recovery aligned. Productive_load indicates elevated load with stable recovery. Adaptation_pressure indicates recovery suppression under load. Maladaptation_risk indicates recovery breakdown relative to training stress.",
        "coaching_implication": None,
        "context_window": "current_microcycle",
        "classification": None,
        "classification_source": "load_recovery_state",
        "state_label": "Load Pressure",
        "operational_state": "recovery_priority",
        "confidence": "moderate",
        "signals": {
          "readiness_signal": "Training load is high with accumulating fatigue.",
          "adaptation_signal": "Durability strain rising \u2014 aerobic consolidation advised.",
          "load_recovery_state": "load_pressure",
          "hrv_ratio": 1.05,
          "atl": 100.33614,
          "ctl": 89.47856
        },
        "operational_context": {
          "framework": "Autonomic\u2013Load Interaction Model",
          "model_basis": "Operational coaching mode derived from autonomic recovery and training load interaction.",
          "signals_used": {
            "hrv_ratio": 1.05,
            "atl": 100.33614,
            "ctl": 89.47856,
            "tsb": -10.857579999999999,
            "load_pressure": 10.857579999999999
          },
          "physiological_state": "load_pressure",
          "operational_state": "recovery_priority",
          "decision_logic": "recovery_priority when fatigue or load exceeds recovery capacity; load_accepting when athlete is absorbing load effectively"
        },
        "recommended_action": {
          "recommendation": "Stabilise load and prioritise recovery",
          "next_session": "Endurance or recovery session"
        },
        "phase_context": None
      },
      "nutrition": {
        "framework": "Fuel Availability (IOC / ACSM Sports Nutrition)",
        "interpretation": "Carbohydrate availability (\u22483\u201310 g/kg depending on training load; IOC/ACSM guidelines) determines glycogen replenishment and endurance capacity.",
        "coaching_implication": "Align carbohydrate intake with training demand (IOC/ACSM) to maintain glycogen availability, recovery, and performance capacity.",
        "formula": "Actual carbohydrate intake (g/kg) \u2212 required carbohydrate demand (g/kg), with requirement derived from recent daily training duration and intensity",
        "context_window": "rolling_3d",
        "classification": "severely_underfuelled",
        "classification_source": "nutrition_balance",
        "confidence": "moderate",
        "signals": {
          "carbs_actual_g": 85.0,
          "protein_actual_g": 90.0,
          "fat_actual_g": 44.0,
          "carbs_required_g": 437.0,
          "protein_required_g": 117.0,
          "fat_required_g": 73.0,
          "carbs_delta_g": -352.0,
          "protein_delta_g": -27.0,
          "fat_delta_g": -29.0
        }
      }
    },
    "zones": {
      "power": {
        "label": "Cycling Power Zones",
        "description": "Distribution of training time by cycling power zones. Derived from Intervals.icu power zone times for Ride-based activities. SS = Sweetspot",
        "distribution": {
          "z1": 20.5,
          "z2": 29.0,
          "z3": 32.9,
          "z4": 4.6,
          "z5": 3.5,
          "z6": 0.9,
          "z7": 0.0,
          "SS": 8.5
        },
        "thresholds": [
          55,
          75,
          90,
          105,
          120,
          150
        ]
      },
      "hr": {
        "label": "Cycling Heart Rate Zones",
        "description": "Distribution of training time by heart rate zones. Restricted to Ride-based activities for physiological comparability.",
        "distribution": {
          "z1": 50.3,
          "z2": 38.2,
          "z3": 4.9,
          "z4": 2.7,
          "z5": 1.2,
          "z6": 2.5,
          "z7": 0.3
        },
        "thresholds": [
          126,
          140,
          146,
          156,
          160,
          165,
          177
        ]
      },
      "pace": {
        "label": "Run Pace Zones",
        "description": "Distribution of training time by pace zones. Used primarily for Run-based activities.",
        "distribution": {},
        "thresholds": []
      },
      "swim": {
        "label": "Swim Pace Zones",
        "description": "Distribution of training time by swim pace zones for pool and open water swims.",
        "distribution": {},
        "thresholds": []
      },
      "calibration": {
        "source": "lactate_test",
        "method": "physiological",
        "confidence": 0.977,
        "reason": "lactate correlation r=0.98",
        "lactate_thresholds": {}
      },
      "fused": {
        "per_sport": {
          "Ride": {
            "_fused_power_z1": 20.5,
            "_fused_power_z2": 29.0,
            "_fused_power_z3": 32.9,
            "_fused_power_z4": 4.6,
            "_fused_power_z5": 3.5,
            "_fused_power_z6": 0.9,
            "_fused_power_z7": 0.0,
            "_fused_power_SS": 8.5,
            "_fused_hr_z1": 0.0,
            "_fused_hr_z2": 0.0,
            "_fused_hr_z3": 0.0,
            "_fused_hr_z4": 0.0,
            "_fused_hr_z5": 0.0,
            "_fused_hr_z6": 0.0,
            "_fused_hr_z7": 0.0
          },
          "Run": {
            "_fused_hr_z1": 86.2,
            "_fused_hr_z2": 10.2,
            "_fused_hr_z3": 3.6,
            "_fused_hr_z4": 0.0,
            "_fused_hr_z5": 0.0,
            "_fused_hr_z6": 0.0,
            "_fused_hr_z7": 0.0,
            "_fused_power_z1": 0.0,
            "_fused_power_z2": 0.0,
            "_fused_power_z3": 0.0,
            "_fused_power_z4": 0.0,
            "_fused_power_z5": 0.0,
            "_fused_power_z6": 0.0,
            "_fused_power_z7": 0.0,
            "_fused_power_SS": 0.0
          }
        },
        "basis": "Sport-specific fusion of power and HR zones (power preferred, HR fallback)"
      },
      "combined": {
        "label": "Combined Intensity Distribution",
        "description": "Global distribution of training time across intensity zones for all endurance activities. Power is prioritised where available, heart rate otherwise. Normalised once across total training time (Seiler / St\u00f6ggl / Issurin methodology) SS = Sweetspot.",
        "distribution": {
          "z1": 37.0,
          "z2": 32.4,
          "z3": 18.8,
          "z4": 3.5,
          "z5": 2.3,
          "z6": 1.6,
          "z7": 0.2,
          "SS": 4.3
        },
        "basis": "Time-based intensity distribution across all endurance activities. Power used when available, HR otherwise. Normalised once across total training time (Seiler / St\u00f6ggl / Issurin methodology)."
      }
    },
    "daily_load": [
      {
        "date": "2026-03-25 00:00:00",
        "tss": 75.0
      },
      {
        "date": "2026-03-27 00:00:00",
        "tss": 79.0
      },
      {
        "date": "2026-03-28 00:00:00",
        "tss": 92.0
      },
      {
        "date": "2026-03-29 00:00:00",
        "tss": 385.0
      },
      {
        "date": "2026-03-30 00:00:00",
        "tss": 26.0
      },
      {
        "date": "2026-03-31 00:00:00",
        "tss": 64.0
      }
    ],
    "events": [
      {
        "name": "Group Ride",
        "type": "VirtualRide",
        "start_date_local": "2026-03-31T17:30:41",
        "duration": 3636,
        "distance": 39.6,
        "tss": 61,
        "IF": 0.78,
        "NP": 233,
        "HRR60": 28,
        "rpe_emoji": "4\ufe0f\u20e3",
        "feel_emoji": "\ud83d\ude42",
        "flags": [
          "repeated",
          "efficient",
          "hrr"
        ]
      },
      {
        "name": "Warmup Ride",
        "type": "VirtualRide",
        "start_date_local": "2026-03-31T17:18:29",
        "duration": 602,
        "distance": 5.4,
        "tss": 3,
        "IF": 0.44,
        "NP": 133,
        "flags": [
          "efficient"
        ]
      },
      {
        "name": "Recovery 45m",
        "type": "VirtualRide",
        "start_date_local": "2026-03-30T18:54:03",
        "duration": 2792,
        "distance": 28.3,
        "tss": 26,
        "IF": 0.58,
        "NP": 174,
        "flags": [
          "efficient"
        ]
      },
      {
        "name": "Dog walk",
        "type": "Hike",
        "start_date_local": "2026-03-29T18:16:20",
        "duration": 4044,
        "distance": 5.8,
        "tss": 44,
        "IF": 0.62,
        "flags": [
          "repeated"
        ]
      },
      {
        "name": "Basecamp 5365m",
        "type": "VirtualRide",
        "start_date_local": "2026-03-29T10:59:46",
        "duration": 22218,
        "distance": 131.1,
        "tss": 341,
        "IF": 0.74,
        "NP": 223,
        "rpe_emoji": "6\ufe0f\u20e3",
        "feel_emoji": "\ud83d\ude42",
        "flags": [
          "efficient"
        ]
      },
      {
        "name": "Grim Ride",
        "type": "Ride",
        "start_date_local": "2026-03-28T13:37:28",
        "duration": 5963,
        "distance": 45.2,
        "tss": 92,
        "IF": 0.74,
        "NP": 223,
        "rpe_emoji": "6\ufe0f\u20e3",
        "feel_emoji": "\ud83d\ude42",
        "flags": [
          "repeated",
          "efficient"
        ]
      },
      {
        "name": "Group Ride",
        "type": "VirtualRide",
        "start_date_local": "2026-03-27T19:30:12",
        "duration": 3774,
        "distance": 40.9,
        "tss": 79,
        "IF": 0.87,
        "NP": 261,
        "HRR60": 20,
        "rpe_emoji": "6\ufe0f\u20e3",
        "feel_emoji": "\ud83d\ude10",
        "flags": [
          "efficient",
          "hrr"
        ]
      },
      {
        "name": "Workout VO2 Max 5x3min",
        "type": "VirtualRide",
        "start_date_local": "2026-03-25T18:59:34",
        "duration": 3659,
        "distance": 30.2,
        "tss": 75,
        "IF": 0.86,
        "NP": 258,
        "HRR60": 28,
        "rpe_emoji": "6\ufe0f\u20e3",
        "feel_emoji": "\ud83d\ude10",
        "flags": [
          "efficient",
          "hrr"
        ]
      }
    ],
    "wellness": {
      "hrv_ratio": 1.05,
      "rest_hr": 42.0,
      "hrv_trend": -5,
      "ctl": 89.47856,
      "atl": 100.33614,
      "tsb": -10.857579999999999,
      "coverage": {
        "unit": "proportion",
        "hrv_pct": 1.0,
        "resting_hr_pct": 1.0,
        "sleep_pct": 1.0,
        "subjective_pct": 0.163,
        "total_days": 43
      },
      "hrv_mean": 52.6,
      "hrv_latest": 55,
      "hrv_trend_7d": 1.7,
      "hrv_source": "garmin",
      "hrv_available": True,
      "hrv_samples": 43,
      "subjective": {
        "fatigue": {
          "value": 2.1,
          "label": "avg"
        },
        "stress": {
          "value": 1.9,
          "label": "avg"
        },
        "soreness": {
          "value": 2.0,
          "label": "avg"
        },
        "mood": {
          "value": 2.7,
          "label": "ok"
        },
        "motivation": {
          "value": 2.9,
          "label": "avg"
        },
        "injury": {
          "value": 1.0,
          "label": "none"
        },
        "hydration": {
          "value": 2.0,
          "label": "ok"
        }
      },
      "CTL": 89.47856,
      "ATL": 100.33614,
      "TSB": -10.857579999999999
    },
    "training_volume": {
      "hours": 12.97,
      "tss": 721,
      "distance_km": 326.6
    },
    "physiology": {
      "lactate_calibration": {
        "lactate": {
          "available": True,
          "samples": 38,
          "mean_mmol": 1.92,
          "latest_mmol": 1.8,
          "range_mmol": [
            1.8,
            2.0
          ],
          "paired_with_power": True,
          "power_field": "HrtLndLt1p",
          "power_spread_w": [
            170.0,
            195.0
          ],
          "power_source": "activity_samples",
          "corr_with_power": 0.977,
          "corr_window_days": 90,
          "source": "df_light",
          "mean": 1.92,
          "latest": 1.8
        },
        "personalized_z2": {
          "start_w": 210,
          "end_w": 225,
          "start_pct": 70.0,
          "end_pct": 75.0,
          "method": "lactate_inferred",
          "mean_lactate": 1.92,
          "latest_lactate": 1.8,
          "samples": 38
        },
        "power_lactate": {
          "method": "lactate_inferred",
          "lt1_w": 210,
          "lt2_w": 300,
          "zones": {
            "z1": [
              0,
              210
            ],
            "z2": [
              210,
              225
            ],
            "z3": [
              225,
              300
            ]
          },
          "confidence_r": 0.977,
          "source": "extended_metrics"
        }
      }
    },
    "wbal_summary": {
      "mean_wbal_depletion_pct": 0.276,
      "mean_anaerobic_contrib_pct": 0.717,
      "sessions_with_wbal_data": 7,
      "basis": "per-session mean (W\u2032-capable sessions only)",
      "window": "weekly",
      "temporal_pattern": {
        "2026-03-25": "high",
        "2026-03-27": "high",
        "2026-03-28": "moderate",
        "2026-03-29": "low",
        "2026-03-30": "low",
        "2026-03-31": "moderate"
      },
      "dominant_pattern": "distributed"
    },
    "planned_summary_by_iso_week": {
      "2026-W15": {
        "total_events": 7,
        "total_duration_minutes": 731.5,
        "planned_load": 603,
        "categories": [
          "WORKOUT"
        ],
        "is_current_week": False
      }
    },
    "future_forecast": {
      "start_date": "2026-04-01",
      "end_date": "2026-04-15",
      "horizon_days": 14,
      "CTL_future": 87.67,
      "ATL_future": 89.8,
      "TSB_future": -2.12,
      "load_trend": "declining",
      "fatigue_class": "neutral"
    },
    "future_actions": [
      {
        "priority": "normal",
        "title": "Neutral load",
        "reason": "Training stimulus and recovery are balanced.",
        "label": "Neutral \u2014 balanced load",
        "color": "#cccccc",
        "date_range": "2026-04-01 \u2192 2026-04-15"
      }
    ],
    "metrics_groups": {
      "load": {
        "ACWR": {
          "name": "ACWR",
          "display_name": "ACWR",
          "value": 0.97,
          "framework": "Banister Load Ratio",
          "formula": "EWMA(Acute) / EWMA(Chronic)",
          "criteria": {
            "recovery": "<0.8",
            "productive": "0.8\u20131.3",
            "aggressive": "1.3\u20131.5",
            "overload": ">1.5"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "green": [
              0.8,
              1.3
            ],
            "amber": [
              0.6,
              1.5
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "high",
          "interpretation": "EWMA Acute:Chronic Load Ratio \u2014 compares 7-day vs 28-day weighted loads. 0.8\u20131.3 = productive training, <0.8 = recovery or detraining, >1.5 = overload/injury risk.",
          "coaching_implication": "If ACWR > 1.5, reduce intensity and focus on recovery to avoid overload. If ACWR < 0.8, gradually increase training load with controlled progression to build endurance.",
          "related_metrics": [
            "ATL",
            "CTL",
            "TSS_7d"
          ],
          "context_window": "rolling"
        },
        "Strain": {
          "name": "Strain",
          "display_name": "Strain",
          "value": 576.8,
          "framework": "Modified Foster 2001 (TSS-based)",
          "formula": "Monotony \u00d7 \u03a3TSS_7d",
          "criteria": {
            "low": "<2000",
            "moderate": "2000\u20133000",
            "high": "3000\u20134000",
            "very_high": ">4000"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "green": [
              0,
              2500
            ],
            "amber": [
              2500,
              4000
            ],
            "red": [
              4000,
              8000
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "high",
          "interpretation": "Modified Foster Strain (\u03a3TSS_7d \u00d7 Monotony). Values >3500 indicate elevated combined load and variability risk; interpret relative to athlete baseline.",
          "coaching_implication": "If Strain > 3000, monitor for signs of overreach and consider more rest or deloading. If Strain > 3500, consider reducing volume or intensity temporarily.",
          "related_metrics": [
            "Monotony",
            "TSS_7d"
          ],
          "context_window": "rolling"
        },
        "FatigueTrend": {
          "name": "FatigueTrend",
          "display_name": "FatigueTrend",
          "value": 31.9,
          "framework": "Banister EWMA Delta",
          "formula": "(Mean_7d - Mean_28d) / Mean_28d \u00d7 100",
          "criteria": {
            "balanced": "-10\u201310",
            "moderate_low": "-20\u2013-10",
            "moderate_high": "10\u201320",
            "accumulating": "20\u201340",
            "extreme_accumulation": ">40",
            "recovering": "<-20"
          },
          "semantic_state": "unclassified",
          "thresholds": {},
          "phase_context": None,
          "classification": "informational",
          "metric_confidence": "high",
          "interpretation": "FatigueTrend is calculated as the percentage change between the 7-day and 28-day moving averages. A 0% change indicates balance, while a positive percentage change indicates accumulating fatigue, and a negative percentage change indicates recovery.",
          "coaching_implication": "If FatigueTrend drops below -10%, recovery is dominating and training load is decreasing relative to the 28-day baseline. Maintain controlled progression and avoid aggressive load increases. If FatigueTrend rises above +10%, fatigue is accumulating \u2014 consider adjusting intensity density or inserting additional recovery to prevent overload.",
          "related_metrics": [
            "ATL",
            "CTL"
          ],
          "context_window": "90d"
        }
      },
      "intensity": {
        "ZQI": {
          "name": "ZQI",
          "display_name": "ZQI",
          "value": 7.5,
          "framework": "Seiler Intensity Distribution (power-zone mapped)",
          "formula": "% time in Z4\u2013Z7 (proxy for Seiler Z3 high-intensity)",
          "criteria": {
            "low": "<5",
            "optimal": "5\u201315",
            "high": "15\u201325",
            "excessive": ">25"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "green": [
              5,
              15
            ],
            "amber": [
              3,
              5
            ],
            "red": [
              0,
              3
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "high",
          "interpretation": "Zone Quality Index (%) 5-15 high-intensity time is normal <3% too easy, >20% too intense or erratic pacing.",
          "coaching_implication": "If ZQI > 20%, review pacing strategy; excessive high-intensity time could indicate erratic pacing or overtraining. Aim for 5-15% ZQI for balanced training.",
          "related_metrics": [],
          "context_window": "7d"
        },
        "Polarisation": {
          "name": "Polarisation",
          "display_name": "Polarisation (Power-based, Seiler ratio)",
          "value": 1.076,
          "framework": "Seiler 3-Zone Contrast Model",
          "formula": "(Z1 + Z3+) / (2 \u00d7 Z2)  (3-zone collapsed, renormalised)",
          "criteria": {
            "z2_dominant": "< 0.65",
            "pyramidal": "0.65\u20130.84",
            "polarised": "0.85\u20131.25",
            "high_contrast": "> 1.25"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "red": [
              0.0,
              0.65
            ],
            "amber": [
              0.65,
              0.85
            ],
            "green": [
              0.85,
              3.0
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "contextual",
          "interpretation": "Power-based Seiler Polarisation Ratio (Z1 + Z3) / (2 \u00d7 Z2), showing the balance between low- and high-intensity work relative to moderate (Z2) training. <0.65 = Z2-dominant distribution, 0.65\u20130.84 = mixed intensity distribution, 0.85\u20131.25 = balanced polarised structure (classic 80/20), >1.25 = high-contrast polarisation with minimal Z2 exposure. \u2699\ufe0f *Power-only metric \u2014 HR ignored.* Use primarily during power-measured cycling phases.",
          "coaching_implication": "If Polarisation <0.65 during base, this reflects aerobic Z2 dominance (\u2705 normal). If in Build/Peak, reduce Z2 time and increase Z1/Z3 contrast. Maintain \u22650.85 for ideal 80/20 balance in power-measured disciplines.",
          "related_metrics": [],
          "context_window": "7d"
        },
        "PolarisationIndex": {
          "name": "PolarisationIndex",
          "display_name": "Polarisation Index (Treff 2019, Power 3-zone)",
          "value": 2.188,
          "framework": "Treff 2019 Polarization-Index",
          "formula": "log10( Z1 / (Z2 \u00d7 Z3) \u00d7 100 )  (3-zone collapsed)",
          "criteria": {
            "threshold_dominant": "< 1.5",
            "pyramidal": "1.5\u20131.99",
            "polarised": "\u2265 2.0"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "red": [
              0.0,
              1.5
            ],
            "amber": [
              1.5,
              2.0
            ],
            "green": [
              2.0,
              4.0
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "contextual",
          "interpretation": "Treff Polarization-Index (2019). Calculated as log10(z1 / (z2 \u00d7 z3) \u00d7 100) after collapsing 7-zone power data to the 3-zone Seiler model (z1=z1, z2=z2, z3=z3+z4+z5+z6+z7), then renormalising the collapsed zones so z1+z2+z3=1 before applying the formula. Uses proportional (0\u20131) zone distribution, not raw time or displayed percentages. >2.0 = polarised distribution, 1.5\u20132.0 = pyramidal, <1.5 = threshold-heavy. \u2699\ufe0f Power-only metric using normalised 3-zone distribution.",
          "coaching_implication": "If PolarisationIndex <1.5, training is threshold-heavy. Between 1.5\u20132.0 reflects pyramidal distribution. Target >2.0 for classical polarised structure during build or peak phases. Interpret relative to normalised 3-zone balance (z1 vs z2\u00d7z3), not absolute time in zones.",
          "related_metrics": [],
          "context_window": "7d"
        },
        "Polarisation_variants": {
          "fused": {
            "name": "Polarisation_fused",
            "display_name": "Polarisation Index (Fused HR+Power, sport-specific)",
            "value": 1.076,
            "framework": "Seiler / St\u00f6ggl / Issurin (HR+Power fused)",
            "formula": "Normalized intensity-domain distribution (fused HR+Power)",
            "criteria": {
              "polarised": "\u2265 0.80",
              "pyramidal": "0.65\u20130.79",
              "threshold_dominant": "< 0.65"
            },
            "semantic_state": "unclassified",
            "thresholds": {
              "red": [
                0.0,
                0.64
              ],
              "green": [
                0.8,
                3.0
              ],
              "amber": [
                0.65,
                0.8
              ]
            },
            "phase_context": "Taper",
            "classification": "green",
            "metric_confidence": "contextual",
            "interpretation": "Sport-specific Polarisation derived from fused HR+Power data. Represents how the athlete distributes intensity within the dominant discipline. Dominance reflects the sport providing the clearest and most internally consistent intensity (zone) signal \u2014 not the sport with the greatest volume, duration, or load. \u22650.80 = polarised, 0.65\u20130.79 = pyramidal, <0.65 = threshold-dominant. \u2699\ufe0f *HR fills gaps when power unavailable; low-intensity HR-only activities may dominate the signal when cycling intensity is spread across Z2\u2013Z4.*",
            "coaching_implication": "If fused Polarisation Index <0.65, the dominant sport is intensity-heavy \u2014 increase Z1/Z2 duration or insert a recovery microcycle. Maintain \u22650.80 for a robust endurance foundation.",
            "related_metrics": {
              "polarised": "\u2265 0.80",
              "pyramidal": "0.65\u20130.79",
              "threshold_dominant": "< 0.65"
            },
            "basis": "Fused HR+Power",
            "source": "zones.fused",
            "context_window": "7d"
          },
          "combined": {
            "name": "Polarisation_combined",
            "display_name": "Polarisation Index (Combined HR+Power, multi-sport)",
            "value": 2.188,
            "framework": "Seiler / St\u00f6ggl / Issurin (multi-sport combined)",
            "formula": "Normalized global intensity-domain distribution",
            "criteria": {
              "polarised": "\u2265 0.78",
              "pyramidal": "0.65\u20130.77",
              "threshold_dominant": "< 0.65"
            },
            "semantic_state": "unclassified",
            "thresholds": {
              "red": [
                0.0,
                0.59
              ],
              "green": [
                0.78,
                3.0
              ],
              "amber": [
                0.6,
                0.78
              ]
            },
            "phase_context": "Taper",
            "classification": "green",
            "metric_confidence": "informational",
            "interpretation": "Global HR+Power combined Polarisation Index across all sports. Reflects total weekly distribution and load balance for multi-sport athletes. Dominance reflects intensity signal strength, not training volume. \u22650.80 = polarised, 0.65\u20130.79 = pyramidal, <0.65 = threshold-heavy. \u2699\ufe0f *Cross-discipline index \u2014 lower precision, but best overall summary of load contrast.*",
            "coaching_implication": "If combined Polarisation Index <0.65, total weekly load is intensity-heavy. Add endurance-focused sessions or recovery days to preserve a healthy 80/20 ratio. Ideal global range \u22650.78 for mixed-sport athletes.",
            "related_metrics": {
              "polarised": "\u2265 0.78",
              "pyramidal": "0.65\u20130.77",
              "threshold_dominant": "< 0.65"
            },
            "basis": "Power where available, HR otherwise (multi-sport weighted)",
            "source": "zones.combined",
            "context_window": "7d"
          },
          "context_window": "unknown"
        }
      },
      "variability": {
        "Monotony": {
          "name": "Monotony",
          "display_name": "Monotony",
          "value": 0.8,
          "framework": "Foster 2001",
          "formula": "Mean_7d / SD_7d",
          "criteria": {
            "optimal": "0\u20132",
            "moderate": "2.1\u20132.5",
            "high": ">2.5"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "green": [
              1.0,
              2.0
            ],
            "amber": [
              0.8,
              2.5
            ]
          },
          "phase_context": None,
          "classification": "amber",
          "metric_confidence": "high",
          "interpretation": "1\u20132 shows healthy variation; >2.5 means repetitive stress pattern.",
          "coaching_implication": "If Monotony > 2.5, introduce more variation in training or implement a deload week to reduce repetitive stress.",
          "related_metrics": [
            "TSS_7d"
          ],
          "context_window": "rolling"
        }
      },
      "metabolic": {
        "FOxI": {
          "name": "FOxI",
          "display_name": "FOxI",
          "value": 63.4,
          "framework": "Internal Derived Metric",
          "formula": "FatOxEfficiency \u00d7 100",
          "criteria": {
            "optimal": ">=70",
            "moderate": "50\u201369",
            "low": "<50"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "green": [
              30,
              80
            ],
            "amber": [
              20,
              90
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "high",
          "interpretation": "FatOx index %; higher values mean more efficient aerobic base.",
          "coaching_implication": "If FOxI is increasing, continue to prioritize low-intensity work to enhance fat metabolism. If it decreases, consider increasing your Zone 2 training duration.",
          "related_metrics": [
            "FatOxEfficiency"
          ],
          "context_window": "7d"
        },
        "CUR": {
          "name": "CUR",
          "display_name": "CUR",
          "value": 36.6,
          "framework": "Internal Derived Metric",
          "formula": "100 - FOxI",
          "criteria": {
            "balanced": "30\u201370",
            "moderate_low": "20\u201329",
            "moderate_high": "71\u201380",
            "low_carb_bias": "<20",
            "high_carb_bias": ">80"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "green": [
              30,
              70
            ],
            "amber": [
              20,
              80
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "high",
          "interpretation": "Carbohydrate Utilisation Ratio; 30\u201370 indicates balanced metabolic use.",
          "coaching_implication": "If CUR is outside the green zone (30-70), adjust carbohydrate intake and fueling strategy to ensure balanced metabolic use during long sessions.",
          "related_metrics": [
            "FOxI",
            "GR"
          ],
          "context_window": "7d"
        },
        "GR": {
          "name": "GR",
          "display_name": "GR",
          "value": 1.69,
          "framework": "Internal Derived Metric",
          "formula": "IF \u00d7 2.4",
          "criteria": {
            "optimal": "1.5\u20132.1",
            "moderate": "1.2\u20131.49",
            "high": ">2.1",
            "low": "<1.2"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "green": [
              0.5,
              2.0
            ],
            "amber": [
              0.3,
              3.0
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "high",
          "interpretation": "Glucose Ratio; >2 indicates excess glycolytic bias.",
          "coaching_implication": "If GR exceeds 2.0, focus on reducing glycolytic intensity and increase aerobic work. Ensure sufficient recovery to avoid over-reliance on carbs.",
          "related_metrics": [
            "IF"
          ],
          "context_window": "7d"
        },
        "MES": {
          "name": "MES",
          "display_name": "MES",
          "value": 22.5,
          "framework": "Internal Derived Metric",
          "formula": "(FatOxEfficiency \u00d7 60) / GR",
          "criteria": {
            "optimal": ">=20",
            "moderate": "10\u201319",
            "low": "<10"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "green": [
              20,
              100
            ],
            "amber": [
              10,
              120
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "high",
          "interpretation": "Metabolic Efficiency Score; >20 is good endurance economy.",
          "coaching_implication": "If MES is below 20, work on improving metabolic efficiency by increasing endurance training with a focus on aerobic base and fat metabolism.",
          "related_metrics": [
            "FatOxEfficiency",
            "GR"
          ],
          "context_window": "7d"
        },
        "FatOxEfficiency": {
          "name": "FatOxEfficiency",
          "display_name": "FatOxEfficiency",
          "value": 0.634,
          "framework": "San Mill\u00e1n 2020",
          "formula": "Derived from IF \u00d7 0.9",
          "criteria": {
            "optimal": "0.60\u20130.80",
            "moderate": "0.50\u20130.59",
            "low": "<0.50"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "green": [
              0.4,
              0.8
            ],
            "amber": [
              0.3,
              0.9
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "high",
          "interpretation": "0.4\u20130.8 means balanced fat oxidation; lower = carb dependence.",
          "coaching_implication": "If FatOxEfficiency is low (<0.6), focus on improving aerobic base with longer, low-intensity efforts.",
          "related_metrics": [
            "IF"
          ],
          "context_window": "7d"
        }
      },
      "capacity": {
        "StressTolerance": {
          "name": "StressTolerance",
          "display_name": "StressTolerance",
          "value": 1.15,
          "framework": "Banister Capacity-Adjusted Load Ratio",
          "formula": "\u03a3TSS_7d / (CTL \u00d7 7)",
          "criteria": {
            "underload": "<0.8",
            "optimal": "0.8\u20131.2",
            "aggressive": "1.2\u20131.4",
            "overreach_risk": ">1.4"
          },
          "semantic_state": "unclassified",
          "thresholds": {
            "green": [
              0.8,
              1.2
            ],
            "amber": [
              0.6,
              1.4
            ],
            "red": [
              1.4,
              3.0
            ]
          },
          "phase_context": None,
          "classification": "green",
          "metric_confidence": "high",
          "interpretation": "Capacity-adjusted weekly load ratio (\u03a3TSS_7d / (CTL \u00d7 7)). 1.0 indicates weekly load equals chronic fitness baseline. Values >1.2 reflect overload relative to adaptive capacity; <0.8 indicates under-stimulation.",
          "coaching_implication": "If StressTolerance >1.4, weekly load significantly exceeds chronic capacity \u2014 reduce volume or intensity and monitor recovery. If <0.8, stimulus may be insufficient for adaptation.",
          "related_metrics": [
            "CTL",
            "TSS_7d"
          ],
          "context_window": "7d"
        }
      }
    },
    "actions": [
      {
        "type": "adaptive_summary",
        "role": "directive",
        "priority": "primary",
        "label": "Coaching Directive",
        "source": "adaptive_decision_engine",
        "directive": "Stabilise load and prioritise recovery",
        "operational_state": "recovery_priority",
        "adaptation_focus": "aerobic_consolidation",
        "risk_flag": "normal",
        "forecast_context": "neutral",
        "load_trend": "declining",
        "nutrition_status": "severely_underfuelled",
        "nutrition_confidence": "moderate",
        "nutrition_note": "Carbohydrate intake is far below demand for current load; fuelling gap likely limiting adaptation.",
        "version": "ade_v2.0",
        "phase_constraint": "recovery",
        "phase_alignment": "aligned",
        "resolution": "honoured"
      },
      {
        "type": "state_action",
        "priority": "supporting",
        "label": "Training State",
        "source": "tier3_training_state",
        "model": "Seiler Load Governance",
        "recommendation": "Stabilise load and prioritise recovery",
        "readiness_signal": "Training load is high with accumulating fatigue.",
        "state_label": "Load Pressure",
        "operational_state": "recovery_priority",
        "operational_context": {
          "framework": "Autonomic\u2013Load Interaction Model",
          "model_basis": "Operational coaching mode derived from autonomic recovery and training load interaction.",
          "signals_used": {
            "hrv_ratio": 1.05,
            "atl": 100.33614,
            "ctl": 89.47856,
            "tsb": -10.857579999999999,
            "load_pressure": 10.857579999999999
          },
          "physiological_state": "load_pressure",
          "operational_state": "recovery_priority",
          "decision_logic": "recovery_priority when fatigue or load exceeds recovery capacity; load_accepting when athlete is absorbing load effectively"
        }
      },
      {
        "type": "system_guidance",
        "priority": "supporting",
        "label": "Energy System Direction",
        "sport": "Ride",
        "source": "energy_system_progression",
        "model": "Energy System Progression Engine",
        "system_state": "aerobic_consolidation",
        "message": "Aerobic development progressing while VO\u2082 capacity drifts \u2014 reintroduce VO\u2082 stimulus within the next microcycle."
      },
      {
        "type": "reflection",
        "priority": "supporting",
        "source": "montis_question_engine",
        "signal": "durability_decline",
        "question": "Is fatigue revealing limits in durability?"
      }
    ],
    "energy_system_progression": {
      "version": "espe_v1.1",
      "sports": {
        "Ride": {
          "supported": True,
          "curve_window": {
            "current_days": 85,
            "previous_days": 85,
            "comparison": "85d_vs_85d",
            "anchor": "report_end",
            "curve_source": "FFT_CURVES"
          },
          "power_curve_anchors": {
            "context": {
              "window_days": 85,
              "description": "Best power values recorded within the last 85 days"
            },
            "values": {
              "5s": {
                "power": 826,
                "activity_id": "i130433348",
                "activity_link": "https://intervals.icu/activities/i130433348"
              },
              "1m": {
                "power": 466,
                "activity_id": "i119106703",
                "activity_link": "https://intervals.icu/activities/i119106703"
              },
              "5m": {
                "power": 333,
                "activity_id": "i120238341",
                "activity_link": "https://intervals.icu/activities/i120238341"
              },
              "20m": {
                "power": 307,
                "activity_id": "i126785019",
                "activity_link": "https://intervals.icu/activities/i126785019"
              },
              "60m": {
                "power": 288,
                "activity_id": "i122292136",
                "activity_link": "https://intervals.icu/activities/i122292136"
              }
            }
          },
          "delta_percent": {
            "5s": -1.2,
            "1m": -4.7,
            "5m": -7.24,
            "20m": 1.99,
            "60m": 5.11
          },
          "curve_dynamics": {
            "vertical_shift_pct": -1.21,
            "rotation_index": -9.52,
            "dominant_shift": "aerobic_rotation"
          },
          "system_status": {
            "anaerobic": "decline",
            "vo2": "decline",
            "threshold": "moderate_gain",
            "aerobic_durability": "strong_gain"
          },
          "system_status_timeline": {
            "anaerobic": "detraining",
            "vo2": "detraining",
            "threshold": "building",
            "aerobic_durability": "building"
          },
          "derived_metrics": {
            "glycolytic_bias_ratio": {
              "name": "glycolytic_bias_ratio",
              "value": 1.52,
              "framework": "Energy System Balance Model",
              "interpretation": "Ratio of short-duration power to threshold power indicating glycolytic dominance.",
              "coaching_implication": "High values suggest anaerobic bias relative to aerobic capacity.",
              "related_metrics": {},
              "context_window": "85d_vs_85d"
            },
            "aerobic_durability_ratio": {
              "name": "aerobic_durability_ratio",
              "value": 0.86,
              "framework": "Durability / Endurance Model",
              "interpretation": "Ratio of 60-minute power to 5-minute power reflecting endurance durability across prolonged efforts.",
              "coaching_implication": "Lower ratios suggest fatigue-driven endurance drop-off.",
              "related_metrics": {},
              "context_window": "85d_vs_85d"
            },
            "durability_gradient": {
              "name": "durability_gradient",
              "value": 0.94,
              "framework": "Durability Gradient Model",
              "interpretation": "Ratio of 60-minute power to 20-minute power reflecting fatigue resistance across prolonged efforts.",
              "coaching_implication": "Lower gradients indicate durability decline during long efforts.",
              "related_metrics": {},
              "context_window": "85d_vs_85d"
            },
            "system_balance_score": {
              "name": "system_balance_score",
              "value": 0.84,
              "framework": "Energy System Balance Composite",
              "interpretation": "Composite indicator describing balance of energy system development.",
              "coaching_implication": "Values closer to 1 indicate balanced development across systems.",
              "related_metrics": {},
              "context_window": "85d_vs_85d"
            },
            "pdr_5m": {
              "name": "pdr_5m",
              "value": 39,
              "framework": "Power Duration Reserve",
              "interpretation": "Difference between 5-minute power and Critical Power representing VO\u2082 reserve capacity.",
              "coaching_implication": "Higher reserve suggests strong VO\u2082 capacity above threshold.",
              "related_metrics": {},
              "context_window": "85d_vs_85d"
            },
            "vo2_reserve_ratio": {
              "name": "vo2_reserve_ratio",
              "value": 1.133,
              "framework": "Critical Power / VO\u2082 Reserve Model",
              "interpretation": "Ratio of 5-minute power to Critical Power reflecting VO\u2082 headroom above threshold.",
              "coaching_implication": "Lower ratios indicate fatigue or VO\u2082 limitation.",
              "related_metrics": {},
              "context_window": "85d_vs_85d"
            }
          },
          "curve_regression": {
            "model": "power_duration_log_regression",
            "slope": -0.5501284032544075,
            "r2": 0.8951035597231284
          },
          "curve_quality": "excellent",
          "power_model": {
            "source": "FFT_CURVES",
            "model_quality": "excellent",
            "cp": 294,
            "w_prime": 15360,
            "pmax": 835,
            "ftp": 300
          },
          "plateau_detected": False,
          "adaptation_bias": "threshold_dominant",
          "adaptation_state": "aerobic_consolidation",
          "curve_profile": "all_rounder",
          "system_guidance": "Aerobic development progressing while VO\u2082 capacity drifts \u2014 reintroduce VO\u2082 stimulus within the next microcycle."
        }
      }
    },
    "current_ISO_weekly_microcycle": {
      "week_iso": "2026-W14",
      "weekly_target_tss": 354.0,
      "completed_tss": 90.0,
      "planned_remaining_tss": 330.0,
      "projected_total_tss": 420.0,
      "delta_to_target": 396.0,
      "basis": "The microcycle is based on the current ISO week (Monday to Sunday) and includes planned and completed with compliance,",
      "completed_hours": 1.95,
      "projected_hours": 11.12,
      "is_projected": True
    },
    "phases_summary": [
      {
        "phase": "Base",
        "start": "2025-12-29",
        "end": "2026-01-11",
        "duration_days": 14,
        "duration_weeks": 2.0,
        "tss_total": 883.0,
        "hours_total": 23.0,
        "distance_km_total": 409.9,
        "descriptor": "\ud83e\uddf1 **Base phase detected** \u2014 prioritise aerobic volume (Z1\u2013Z2 \u2265 70%) and stable load progression (ACWR \u2264 1.0).",
        "calc_method": "|\u0394TSS|<5% & TSB\u22480",
        "calc_context": {
          "delta": 0.034,
          "tsb": -11.05,
          "ctl_slope": 8.29,
          "atl_slope": 19.33,
          "acwr": 1.03,
          "lvi": 0.8
        }
      },
      {
        "phase": "Build",
        "start": "2026-01-12",
        "end": "2026-01-18",
        "duration_days": 7,
        "duration_weeks": 1.0,
        "tss_total": 592.0,
        "hours_total": 13.6,
        "distance_km_total": 275.5,
        "descriptor": "\ud83d\udcc8 **Build phase detected** \u2014 progressive overload active; maintain ACWR \u2264 1.3 and manage intensity density.",
        "calc_method": "TSB<-30 (acute overload)",
        "calc_context": {
          "delta": 0.166,
          "tsb": -63.38,
          "ctl_slope": 44.78,
          "atl_slope": 97.11,
          "acwr": 1.13,
          "lvi": 0.0
        }
      },
      {
        "phase": "Base",
        "start": "2026-01-19",
        "end": "2026-01-25",
        "duration_days": 7,
        "duration_weeks": 1.0,
        "tss_total": 432.0,
        "hours_total": 10.6,
        "distance_km_total": 234.5,
        "descriptor": "\ud83e\uddf1 **Base phase detected** \u2014 prioritise aerobic volume (Z1\u2013Z2 \u2265 70%) and stable load progression (ACWR \u2264 1.0).",
        "calc_method": "steady_load_fallback",
        "calc_context": {
          "delta": -0.052,
          "tsb": -2.82,
          "ctl_slope": -13.73,
          "atl_slope": -74.3,
          "acwr": 1.01,
          "lvi": 0.0
        }
      },
      {
        "phase": "Recovery",
        "start": "2026-01-26",
        "end": "2026-02-01",
        "duration_days": 7,
        "duration_weeks": 1.0,
        "tss_total": 436.0,
        "hours_total": 9.4,
        "distance_km_total": 168.5,
        "descriptor": "\ud83d\udca4 **Recovery phase detected** \u2014 reduce load and prioritise recovery; target low monotony and declining load trend.",
        "calc_method": "TSB>10 + low load",
        "calc_context": {
          "delta": -0.021,
          "tsb": 10.61,
          "ctl_slope": -8.67,
          "atl_slope": -22.1,
          "acwr": 0.98,
          "lvi": 0.0
        }
      },
      {
        "phase": "Overreached",
        "start": "2026-02-02",
        "end": "2026-02-08",
        "duration_days": 7,
        "duration_weeks": 1.0,
        "tss_total": 689.0,
        "hours_total": 15.7,
        "distance_km_total": 341.2,
        "descriptor": "Overreached phase \u2014 maintain adaptive consistency.",
        "calc_method": "TSB<-50 + overload spike",
        "calc_context": {
          "delta": 0.279,
          "tsb": -84.59,
          "ctl_slope": 66.1,
          "atl_slope": 161.3,
          "acwr": 1.16,
          "lvi": 0.14
        }
      },
      {
        "phase": "Base",
        "start": "2026-02-09",
        "end": "2026-02-15",
        "duration_days": 7,
        "duration_weeks": 1.0,
        "tss_total": 493.0,
        "hours_total": 8.5,
        "distance_km_total": 282.1,
        "descriptor": "\ud83e\uddf1 **Base phase detected** \u2014 prioritise aerobic volume (Z1\u2013Z2 \u2265 70%) and stable load progression (ACWR \u2264 1.0).",
        "calc_method": "steady_load_fallback",
        "calc_context": {
          "delta": -0.003,
          "tsb": -16.48,
          "ctl_slope": -8.79,
          "atl_slope": -76.9,
          "acwr": 1.03,
          "lvi": 0.0
        }
      },
      {
        "phase": "Build",
        "start": "2026-02-16",
        "end": "2026-03-15",
        "duration_days": 28,
        "duration_weeks": 4.0,
        "tss_total": 2793.0,
        "hours_total": 51.9,
        "distance_km_total": 1379.9,
        "descriptor": "\ud83d\udcc8 **Build phase detected** \u2014 progressive overload active; maintain ACWR \u2264 1.3 and manage intensity density.",
        "calc_method": "TSB<-30 (acute overload)",
        "calc_context": {
          "delta": 0.069,
          "tsb": -75.1,
          "ctl_slope": 38.46,
          "atl_slope": 42.11,
          "acwr": 1.11,
          "lvi": 0.0
        }
      },
      {
        "phase": "Deload",
        "start": "2026-03-16",
        "end": "2026-03-22",
        "duration_days": 7,
        "duration_weeks": 1.0,
        "tss_total": 508.0,
        "hours_total": 11.3,
        "distance_km_total": 256.8,
        "descriptor": "\ud83e\uddd8 **Deload phase detected** \u2014 controlled reduction in load while maintaining frequency; prepare for next progression block.",
        "calc_method": "TSB>10 + moderate unload",
        "calc_context": {
          "delta": -0.131,
          "tsb": 33.96,
          "ctl_slope": -44.24,
          "atl_slope": -153.3,
          "acwr": 0.95,
          "lvi": 0.0
        }
      },
      {
        "phase": "Build",
        "start": "2026-03-23",
        "end": "2026-03-29",
        "duration_days": 7,
        "duration_weeks": 1.0,
        "tss_total": 813.0,
        "hours_total": 13.6,
        "distance_km_total": 332.2,
        "descriptor": "\ud83d\udcc8 **Build phase detected** \u2014 progressive overload active; maintain ACWR \u2264 1.3 and manage intensity density.",
        "calc_method": "TSB<-30 (acute overload)",
        "calc_context": {
          "delta": 0.235,
          "tsb": -62.74,
          "ctl_slope": 55.54,
          "atl_slope": 152.23,
          "acwr": 1.09,
          "lvi": 0.0
        }
      },
      {
        "phase": "Taper",
        "start": "2026-03-30",
        "end": "2026-04-05",
        "duration_days": 7,
        "duration_weeks": 1.0,
        "tss_total": 420.0,
        "hours_total": 11.1,
        "distance_km_total": 73.4,
        "descriptor": "\ud83d\udcc9 **Taper phase detected** \u2014 reduce ATL by ~30\u201350% while maintaining intensity; expect freshness to rise (TSB \u2191, fatigue \u2193).",
        "calc_method": "projection_forecast",
        "calc_context": None,
        "is_projected": True,
        "projection_basis": "planned_remaining",
        "completed_tss": 90.0,
        "planned_remaining_tss": 330.0,
        "projected_total_tss": 420.0,
        "completed_hours": 1.95,
        "projected_hours": 11.12
      }
    ],
    "insight_view": {
      "critical": [],
      "watch": [],
      "positive": [
        {
          "name": "fat_oxidation_index",
          "classification": "green",
          "interpretation": "FatOx index %; higher values mean more efficient aerobic base.",
          "coaching_implication": "If FOxI is increasing, continue to prioritize low-intensity work to enhance fat metabolism. If it decreases, consider increasing your Zone 2 training duration."
        }
      ]
    },
    "phase_alignment": {
      "past_pattern": "fatigue_streak",
      "current_state": "Load Pressure",
      "operational_state": "recovery_priority",
      "planned_pattern": "reduced",
      "required_phase": "recovery",
      "alignment": "aligned",
      "phase_streak": {
        "type": "fatigue",
        "length": 6
      },
      "last_block": {
        "phase": "Build",
        "duration_days": 7
      }
    },
    "training_guidance": "Can: Stabilise load and prioritise recovery | Should: Recovery \u2192 Stabilise load and prioritise recovery",
    "renderer_instructions": "You are a deterministic URF renderer.\n\n    You must render a **Weekly Training Report** using the embedded system context.\n    This report follows the **Unified Reporting Framework (URF v5.1)**.\n\n    **Scope:** Detailed analysis of the last 7 days of training activity\n    **Data Sources:** 7-day full activities, 42-day wellness, 90 day light activities\n    **Intended Use:** Day-to-day coaching decisions, intensity balance, short-term fatigue and recovery management\n    DATA RESOLUTION MODEL:\n\n        This report uses the following semantic resolution rules.\n\n        - CTL: authoritative\n- ATL: authoritative\n- TSB: authoritative\n- zones: authoritative\n- derived_metrics: full\n- performance_intelligence: acute_full_7d\n- energy_system_progression: full\n- insights: tactical\n\n        These rules determine which metrics are authoritative,\n        which signals may appear, and the time horizon used\n        for interpretation.\n\n        Resolution rules MUST NOT be printed in the report output.\n    HARD RULES:\n    - Render exactly ONE report.\n- All sections MUST appear under their corresponding stack layer header.\n- Stack layer headers MUST be rendered using the provided stack labels in uppercase.\n- Do NOT add numeric prefixes to section headers.\n- Use emoji-based section headers only.\n- Preserve section order exactly as defined by the contract.\n- Metric context MUST be derived exclusively from each metric\u2019s `context_window` and `confidence_model` fields.\n- When both wellness signals and performance_intelligence metrics are present, interpret recovery state as the physiological response to recent training stress. Insights should reconcile these layers rather than repeating them independently.\n\n    STACK STRUCTURE RULE:\n\n        The report MUST be organised into the following conceptual intelligence layers:\n\n        Meta Context:\n- meta\n\nTraining Load:\n- training_volume\n- metrics_groups.load\n- metrics_groups.intensity\n- metrics_groups.variability\n- metrics_groups.metabolic\n- metrics_groups.capacity\n- daily_load\n- events\n\nPhysiology Response:\n- wellness\n- insight_view\n\nPerformance Intelligence:\n- performance_intelligence\n- wbal_summary\n\nAdaptation:\n- energy_system_progression\n- physiology\n- zones\n- phases_summary\n\nAdaptive Decisions:\n- actions\n- phase_alignment\n- planned_summary_by_date\n- current_ISO_weekly_microcycle\n- planned_summary_by_iso_week\n- future_forecast\n- future_actions\n- training_guidance\n\n\n        These layers are PRESENTATIONAL GROUPINGS ONLY.\n\n        They must NOT:\n        - change section order\n        - override section_handling rules\n        - modify interpretation_rules\n        - alter table rendering rules\n\n        Sections must appear in the exact URF contract order.\n        Stack layers only determine which layer header a section appears under.\n\n        Each section must appear under its corresponding stack layer while still following the URF section order.\n        A stack layer header MUST be rendered once when the first section belonging to that layer appears.\n        Subsequent sections mapped to the same stack layer MUST remain under that header and MUST NOT repeat the header.\n\n    STACK SECTION MAP:\n        meta \u2192 \ud83d\udcca REPORT CONTEXT\ntraining_volume \u2192 \ud83e\udded TRAINING LOAD\nmetrics_groups.load \u2192 \ud83e\udded TRAINING LOAD\nmetrics_groups.intensity \u2192 \ud83e\udded TRAINING LOAD\nmetrics_groups.variability \u2192 \ud83e\udded TRAINING LOAD\nmetrics_groups.metabolic \u2192 \ud83e\udded TRAINING LOAD\nmetrics_groups.capacity \u2192 \ud83e\udded TRAINING LOAD\ndaily_load \u2192 \ud83e\udded TRAINING LOAD\nevents \u2192 \ud83e\udded TRAINING LOAD\nwellness \u2192 \ud83e\udec0 PHYSIOLOGY RESPONSE\ninsight_view \u2192 \ud83e\udec0 PHYSIOLOGY RESPONSE\nperformance_intelligence \u2192 \u2699\ufe0f PERFORMANCE INTELLIGENCE\nwbal_summary \u2192 \u2699\ufe0f PERFORMANCE INTELLIGENCE\nenergy_system_progression \u2192 \ud83d\udcc8 ADAPTATION\nphysiology \u2192 \ud83d\udcc8 ADAPTATION\nzones \u2192 \ud83d\udcc8 ADAPTATION\nphases_summary \u2192 \ud83d\udcc8 ADAPTATION\nactions \u2192 \ud83c\udfaf ADAPTIVE DECISIONS\nphase_alignment \u2192 \ud83c\udfaf ADAPTIVE DECISIONS\nplanned_summary_by_date \u2192 \ud83c\udfaf ADAPTIVE DECISIONS\ncurrent_ISO_weekly_microcycle \u2192 \ud83c\udfaf ADAPTIVE DECISIONS\nplanned_summary_by_iso_week \u2192 \ud83c\udfaf ADAPTIVE DECISIONS\nfuture_forecast \u2192 \ud83c\udfaf ADAPTIVE DECISIONS\nfuture_actions \u2192 \ud83c\udfaf ADAPTIVE DECISIONS\ntraining_guidance \u2192 \ud83c\udfaf ADAPTIVE DECISIONS\n\n    INTERPRETATION RULES:\n    - Interpretations must be descriptive/conditional, not predictive.\n- Render training_volume as: Hours | TSS | Distance when present.\n- Render wbal_summary.temporal_pattern as a 1-line block timeline (\u2582 \u2583 \u2587 \u2192 none/low/moderate/high).\n- Render daily_load as fixed-width timeline (labels, blocks, TSS aligned). NEVER list/table.\n- If daily_load + CTL + ATL exist, add fatigue row (\u2191 \u2193 \u2014) using sign(ATL\u2212CTL) only.\n- Daily_load rows must use fixed-width columns for alignment.\n- EVENTS icons require a single legend line under the section header.\n- Render zone distributions as fixed-width ASCII bars with exact % (no derived metrics).\n- If lactate_calibration.available, show mean, latest, samples, LT1 (no derivation).\n- Render performance_intelligence as WDRM / ISDM / NDLI only (no recompute/merge).\n- If high_dep_sessions>0 AND high_drift_sessions>0 \u2192 note neuromuscular+metabolic overlap.\n- Cross-section interpretation allowed when describing same physiology.\n- If energy_system_progression exists, summarise direction using system_status + adaptation_state.\n- Prioritise ESPE signals over repeating metric definitions.\n- Render power anchors as [<power> W](link) when activity_link exists, else plain.\n- Title current_ISO_weekly_microcycle as 'Current ISO Week ## (Mon-Sun)'.\n- If a section is marked full, render every entity and field exactly as present in the semantic data\n- If actions[0].resolution == 'overridden_by_phase':\n- - required_phase overrides ADE directive in interpretation.\n- - Any positive load statement MUST be qualified by fatigue/phase context.\n- - Do NOT present training as fully acceptable without qualification.\n- Precedence: required_phase > ADE.directive > performance_intelligence.training_state > metrics.\n- Render adaptive_decisions as compact dashboard tables (no narrative).\n- adaptive_decisions MUST be rendered as STATE, OPERATIONS, TRAINING_GUIDANCE, PHASE ALIGNMENT, DECISION CONTEXT, FUTURE ACTIONS, PHASES SUMMARY tables.\n- STATE MUST NOT exceed 4 columns per table.\n- STATE MUST be split into multiple tables when more than 4 fields are present.\n- STATE tables MUST follow this fixed grouping:\n- STATE SNAPSHOT: ADE directive, state, resolution, load_trend.\n- ADAPTATION RESPONSE: adaptation_focus, key_constraint, next_action, dominant_signal.\n- OPERATIONS table MUST contain week_delta, planned_load (current \u2192 next), and 14 day forecast summary (CTL / TSB / fatigue_class).\n- training_guidance MUST be rendered as a single-row table with column: Directive.\n- phase_alignment MUST be rendered as a single-row table with columns: Required Phase, Recent Load Alignment, Past Pattern, Phase Streak.\n- future_actions MUST be rendered as a table with columns: Priority, Action, Reason.\n- Do NOT render state_action, system_guidance, or reflection as separate sections.\n- Do NOT render paragraph explanations for adaptive_decisions.phases_summary MUST be rendered as a compact table (max 4 rows) with columns: Phase, Duration, Trend\n- Phases should always be sequential dated phases\n- energy_system_progression MUST be rendered as compact adaptation table(s)\n- Table MUST include key systems (aerobic, threshold, vo2, anaerobic) and overall phase/adaptation_state.\n- lactate_calibration when available MUST be rendered as a single compact adaptation table before suppression.\n- Do NOT render narrative or subsection breakdown when table is present.\n- performance_intelligence MUST be rendered as compact dashboard tables (may be split if too wide).\n- WDRM, ISDM, and NDLI MUST NOT be rendered as separate sections when sufficient data exists.\n- They MUST be projected into a SYSTEM STATE table and a LOAD SIGNATURE table.\n- performance_intelligence MUST include operational_state in the SYSTEM STATE table.\n- operational_state MUST be rendered as the primary state indicator (first column).\n- All original semantic values MUST still be represented (no omission).\n- Do NOT summarise or drop metrics \u2014 only change layout.\n- If a table has more than 4 columns, split it into multiple tables (max 4 columns each).\n\n    COACHING INTERPRETATION RULES:\n- You are an Endurance Coach\n- You MAY include up to 5 short coaching sentence(s) per section.\n- Coaching sentences MUST be directly anchored to values, states, or interpretation fields in that section.\n- Coaching sentences MUST be descriptive or conditional, not predictive.\n- Coaching sentences MUST appear immediately after the section\u2019s data and before the next divider.\n- Coaching sentences MUST NOT introduce new metrics.\n\n    ALLOWED ENRICHMENT:\n        - Restate semantic interpretation fields.\n- Explain what a value indicates within its known threshold or state.\n- derive_stepwise_forecast\n\n\n\n\n\n    STATE PRESENTATION:\n- Present a concise, single-sentence state banner at the top of the report.\n- Use ONLY semantic states already present in the data.\n- Do NOT derive, compute, or infer new states.\n- Style: single_sentence_banner\n\n    EMPHASIS GUIDANCE:\n        The following sections should receive proportional narrative and visual emphasis.\n        This does NOT change section order, inclusion, or data fidelity.\n        - metrics_groups: high\n- actions: high\n- events: medium\n- wellness: medium\n- adaptation: high\n- phases_summary: low\n\n    FRAMING INTENT:\n- Interpret and summarise this report through the following intent:\n  tactical_weekly_control\n- This intent guides prioritisation and narrative focus only.\n\n    SECTION HANDLING RULES:\n        - meta: full\n- training_volume: full\n- events: full\n- current_ISO_weekly_microcycle: forbid\n- daily_load: full\n- metrics_groups: table_summary\n- performance_intelligence: full\n- energy_system_progression: full\n- zones: forbid\n- physiology: full\n- wellness: summary\n- phases: forbid\n- phase_alignment: headline\n- decision_context: headline\n- phases_summary: summary\n- planned_summary_by_iso_week: forbid\n- actions: table_summary\n- actions.0.adaptive_summary: full\n- actions.1.state_action: full\n- actions.3.system_guidance: full\n- actions.4.reflection: full\n- training_guidance: headline\n- future_forecast: forbid\n- future_actions: full\n- insights: forbid\n- insight_view: summary\n\n        Handling meanings:\n\n        - full:\n            Render the entire section exactly as provided.\n            Tables remain tables, lists remain lists.\n            Do not remove rows or fields.\n\n        - summary:\n            Render a compact representation using ONLY existing semantic aggregates\n            already present in the section. Do NOT derive new metrics.\n\n        Summary rules:\n            Prefer a short table if aggregate values exist.\n            If aggregates do not exist, show the top-level fields only.\n            Do NOT iterate full arrays or lists.\n            Do NOT narrate each element of a list.\n            Maximum 3\u20135 rows or key metrics.\n\n        - table_summary:\n            Render a condensed table using aggregate fields only.\n            Do NOT render the full underlying dataset.\n\n        - headline:\n            Render only the primary indicators of the section.\n            Maximum 3\u20134 metrics.\n            No tables longer than one row.\n            No subsections.\n            No detailed narrative.\n\n        Rules:\n        \u2022 Maximum 5 rows.\n        \u2022 Prefer totals, means, or trend indicators already provided.\n        \u2022 Do NOT derive calculations.\n\n        - forbid:\n        This section MUST NOT be rendered in the report output.\n        It may still be used internally for reasoning.\n\n    EVENTS (WEEKLY \u2014 NON-NEGOTIABLE):\n        - Render EVENTS as a Markdown table only.\n- 1 event = 1 row; no omissions.\n- No summarising, grouping, renaming, or narrative text.\n- Coaching sentences (if any) appear AFTER the table.\n- Use fixed column order.\n- Icons: prefix in Activity column from semantic fields; multiple allowed; fixed order.\n- Icons are additive only (no replacement/suppression of values or rows).\n- Append rpe_emoji + feel_emoji to TSS.\n- If activity_link exists, render as [name](link) with icons before link.\n- Render a single legend line directly below the table.\n\n        - The EVENTS table MUST use the following column order:\n        Date | Activity | Duration (min) | Distance | TSS | IF | NP | HRR60\n\n        - The semantic field `duration_seconds` MUST be converted to minutes at render time.\n- This conversion applies ONLY to duration.\n- Display as integer minutes by default.\n- Use one decimal only if duration < 30 minutes and precision is useful.\n- Label column as Duration (min). Show HRR60 column when values exist.\n\n        - When multiple icons apply, they MUST be rendered together in the following fixed order (left \u2192 right):\n        1) \u26a1 Efficient (optimal efficiency factor)\n2) \ud83d\udfe2 Aerobic (low IF with stable decoupling)\n3) \ud83d\udca5 Anaerobic (heavy W\u2032 engagement)\n4) \ud83d\udd01 Repeated (repeated W\u2032 depletion pattern)\n5) \ud83d\udcc8 Progressive (progressive W\u2032 engagement)\n6) \ud83e\uddd8 Recovery (very low intensity recovery session)\n7) \u2764\ufe0f Heart_rate_recovery_60s (Heart Rate Recovery within 60s)\n\n\n\n    LIST RENDERING RULES (NON-NEGOTIABLE):\n    - If a section value is a JSON array (list), render it as a Markdown table.\n- Render EVERY element in the array.\n- Preserve one row per array element.\n- Do NOT summarise the list unless explicitly allowed by section handling.\n- Do NOT replace lists with prose unless explicitly allowed.\n- Do NOT omit rows for brevity.\n\n    TONE AND STYLE:\n    - Keep tone factual, supportive, neutral, and coach-like.\n\n    SECTION ORDER (INSTRUCTIONAL \u2014 DO NOT NUMBER HEADERS):\n    1. meta\n2. training_volume\n3. metrics_groups\n4. daily_load\n5. events\n6. wellness\n7. insight_view\n8. performance_intelligence\n9. wbal_summary\n10. energy_system_progression\n11. physiology\n12. zones\n13. phases_summary\n14. actions\n15. phase_alignment\n16. training_guidance\n17. decision_context\n18. current_ISO_weekly_microcycle\n19. planned_summary_by_iso_week\n20. future_forecast\n21. future_actions\n\n    CLOSING NOTE REQUIREMENTS:\n- The closing note MUST begin with one of the following classifications:\nProductive, High Strain, Overreached.\n- State clearly whether last week\u2019s training load was handled appropriately.\n- The closing note MUST remain within the conceptual focus: tactical_alignment.\n- Assess whether acute load and recovery state align with immediate training intent.\n- It MUST anchor strictly to: ACWR, FatigueTrend, NDLI, Durability, performance_intelligence.training_state, energy_system_progression, actions.\n- It MUST NOT introduce new metrics or reinterpret semantic data.\n- Maximum 4 sentences.\n\n    CLOSING REFLECTION RULE:\n        After the full report is produced, generate exactly ONE short reflective coaching question.\n\n        The question MUST be based on the dominant signal in the report.\n\n        Allowed reflection themes:\n        - training load\n- perceived exertion (RPE / feel)\n- adaptation\n- fatigue\n\n        The closing question must be grounded in the signals present in the report\n        and must not introduce new metrics or predictions.\n\n        Format exactly as:\n        ---\n        Closing Reflection\n        <question>\n\n    POST-RENDER INTERACTION:\n        - After the full report is rendered, present follow-up commands to allow deeper inspection.\n        - These commands MUST be shown after the closing reflection section.\n        - The commands MUST be rendered as short, copyable user prompts in raw markdown\n        - Do NOT add explanation, narrative, or coaching around these commands.\n\n        Suggested follow up questions:\n        - \"show full physiology_response\"\n- \"show full performance_intelligence\"\n- \"show full adaptation\"\n- \"show full adaptive_decisions\"\n- \"load planned events\"\n- \"show power curves\"\n- \"load athlete profiles\"\n- \"load last activity and analyse\"\n- \"show me more command questions\"",
}
