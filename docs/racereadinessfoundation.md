The foundation for the Race Readiness Dashboard (which you referred to as the RaceRaceinessDashboard) is built on the Unified Reporting Framework (URF) v5.1 and the Montis Intelligence Stack.
The primary logic is a "State-First" evaluation that prioritizes the "Sunrise State"—the athlete's physiological condition specifically on the morning of the race, calculated by analyzing the "Sunset" (end-of-day) state of the day prior to the event.

🧭 The Foundation: Five Intelligence Layers

The dashboard evaluates each "marker" (Diagnostic Card) using these five Montis stack intelligence layers:

- Training Load
- Physiology Response
- Performance Intelligence
- Adaptation Tracking
- Adaptive Decision Engine

Training Load (Banister Model): Uses CTL, ATL, and TSB to determine Form.

Physiology Response: Integrates wellness signals (HRV, Sleep) and the ADE (Adaptive Decision Engine) resolved taper state.

Performance Intelligence (PI):
ISDM (Durability): Analyzes HR-Power decoupling to assess resistance to late-race fatigue.
NDLI (Neural Density): Measures the clustering of high-intensity work in the final 7 days.
WDRM (Anaerobic Repeatability): Evaluates supra-threshold priming and anaerobic reserve behavior.
Adaptation (ESPE Alignment): Compares the athlete's current physiological profile (e.g., "Endurance Specialist") against the specific demands of the race type.
Adaptive Decisions: Synthesizes these signals into a final Readiness Score (0-100) and identifies Limiting Factors.


📏 Rules for Evaluation (Foundation for each Marker)
Each marker on the dashboard is governed by specific rules hardcoded in the RaceReadinessDashboard.tsx component, often weighted by the Race Profile (e.g., a "Long Endurance" event has different targets than a "Short/Intense" one).

1. Load & Form (Freshness)
The Rule: Evaluates TSB (Training Stress Balance) at the race "Sunrise".
Thresholds:
Peak: TSB > 12.
Target Achieved: TSB is within the specific race_profile.targets.tsb range.
Detraining: CTL Drop > 20 (indicates a blank forecast or excessive load loss).
Fatigued: TSB < -10.

2. Durability (Efficiency)
The Rule: Uses the ISDM model to analyze decoupling (drift) relative to the race priority.
Thresholds:
Elite: Stable state + Drift < 3.0%.
Sub-optimal: Drift > Moderate bounds (usually 6.0%) or "Drifting" state if durability is a priority for the race.

3. Neural Readiness (Sharpness)
The Rule: Monitors clustering of high-intensity work (NDLI) in the final 7 days.
Thresholds:
Sharp: NDLI ≥ 2 sessions + WDRM > 150kJ (primed for anaerobic hits).
Loaded: NDLI ≥ 5 (danger zone: neural fatigue/over-clustering).
Flat: NDLI/WDRM = 0 (lack of recent high-intensity activation).

4. System Alignment (Specificity)
The Rule: Matches the ESPE Curve Profile (e.g., All-Rounder, Specialist) against the race's priority_systems.
Thresholds:
Matched: If the profile (e.g., "Endurance Specialist") contains the priority requirements of the race (e.g., "Aerobic").

5. Taper Quality (Execution)
The Rule: Measures the magnitude of the CTL Drop from peak to race day.
Thresholds:
Optimal: Taper is "optimal" (via ADE) OR CTL Drop > 6 with TSB > 10.
Incomplete: Even if load has dropped, if NDLI ≥ 5, the taper is marked as incomplete due to residual intensity demand.

🧮 Final Scoring Logic
The Readiness Score starts at a baseline of 90. It applies "modifiers" rather than a flat average:
Perfect TSB Alignment: +5 points.
Neural Overload (NDLI ≥ 5): -15 points (higher penalty if event profile requires low neural load).
Durability Drift: Down to -15 points if durability is a priority for the event.
Detraining Penalty: Points deducted equal to the severity of ctlDrop (capped at -60).