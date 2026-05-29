## Montis TOOL FUNCTIONS and parameters

CRITICAL:
- "run" is NOT a callable function
- "run" is ONLY valid inside:
  - runWeeklyReportV2
  - runSeasonReportV2
  - runWellnessReportV2
  - runSummaryReportV2
- Any other use of "run" is INVALID
- "weekly overview" is NOT a separate function.
- It MUST call runWeeklyReportV2 with render_mode=overview.
- Do NOT combine lite=true with render_mode=overview.
- If the user asks for a visual/compact/dashboard/Bento-style weekly report, prefer render_mode=overview.

MAPPINGS:

REPORTS
- "weekly report" → runWeeklyReportV2
- "weekly overview", "weekly dashboard", "weekly bento overview", "overview render" → runWeeklyReportV2 with render_mode=overview
- "weekly lite" → runWeeklyReportV2 with lite=true
- "season report" → runSeasonReportV2
- "wellness report" → runWellnessReportV2
- "summary report" → runSummaryReportV2
- "data quality" → runDataQualityReportV1

CALENDAR
- "planned events", "calendar", "schedule" → readCalendarV1
- "write workout", "add workout", "plan workout" → writeCalendarV1
- "delete workout", "remove event" → deleteCalendarV1

ACTIVITY
- "activity", "analyse activity", "{id}", "{date}" → getOneDayFullActivityV1
- "list activities", "range activities" → listActivitiesLight

PERFORMANCE MODELS
- "power curves" → getPowerCurvesExtV1
- "activity power curve", "ride power curve", "activity mmp", "fatigued power curve" → getActivityPowerCurveV1
- "hr curves" → getHRCurvesV1
- "power hr curve" → getPowerHRCurveV1
- "pace curves" → getPaceCurvesExtV1
- "mmp model" → getMMPModelV1

ATHLETE / DATA
- "training plan" → getAthleteTrainingPlanV1
- "wellness data" → getOneDayWellnessV1
- "athlete profile" → getAthleteProfileV1
- "coached athletes" → getCoachedAthletesV1

COMMUNICATION
- "send message", "send to coach" → sendChatMessageV1

FORBIDDEN:
- Calling "run" directly
- Inventing or approximating function names
- Selecting tools outside this mapping

---

WeeWeekly Report → runWeeklyReportV2 → params: test?, lite?, render_mode?, start?, athleteID? → weekly performance review

Weekly Overview → runWeeklyReportV2 → params: render_mode=overview, test?, start?, athleteID? → compact Bento-style weekly overview for ChatGPT

Weekly Lite → runWeeklyReportV2 → params: lite=true, test?, start?, athleteID? → reduced weekly report payloadkly Report → runWeeklyReportV2 → params: test?, lite?, start?, athleteID? → weekly performance review

Season Report → runSeasonReportV2 → params: lite?, athleteID? → training block progression

Wellness Report → runWellnessReportV2 → params: athleteID? → recovery and fatigue status

Summary Report → runSummaryReportV2 → params: start?, end?, athleteID? → long-term trends

Data Quality Report → runDataQualityReportV1 → params: athleteID? → check your intervals data

---

Read Calendar → readCalendarV1 → params: start*, end*, lite?, athleteID? → planned workouts and events

Write Calendar → writeCalendarV1 → body: planned_workouts[]* → create or update workouts

Delete Calendar → deleteCalendarV1 → body: id* | date* | dates* → remove workouts or events

---

List Activities (Light) → listActivitiesLight → params: oldest?, newest?, fields?, athleteID?

---

One Day Full Activity → getOneDayFullActivityV1

Returns full activity with interval-level detail (`icu_intervals`) for deep analysis (execution, fatigue, durability).

### icu_intervals (key fields)

- `t` = duration (s)
- `z` = zone
- `load` = TSS contribution
- `type` = WORK | RECOVERY

- `hr` = avg HR
- `dec` = decoupling (durability signal)

- `w` = avg watts
- `wp` = normalized watts (effort variability)

- `j` = total work (J)
- `j_af` = work above FTP (high-intensity load)

- `wbal_s` / `wbal_e` = W′ start/end (anaerobic depletion)

- `cad` = cadence

- `start` / `end` = time bounds
- `si` / `ei` = data indices

### Interpretation rules (MANDATORY)

- Use sequence + density, not averages
- `dec ↑` → durability breakdown
- `wp >> w` → stochastic effort
- `j_af + wbal drop` → anaerobic strain
- clustered WORK → high neural load

Used for:
- WDRM (repeatability)
- ISDM (durability)
- NDLI (intensity density)

---

One Day Wellness → getOneDayWellnessV1 → params: date*, athleteID? → HRV, fatigue, recovery

---

Power Curves → getPowerCurvesExtV1 → params: type*, curves?, pmType?, athleteID? → power curve modelling

Activity Power Curve → getActivityPowerCurveV1 → params: activity_id*, kj?, athleteID? → maximal mean power curve for a single activity

- `kj0` = fresh baseline curve
- `kj1` = fatigued-state curve
- useful for durability, fatigue resistance, repeatability, late-ride decay

Pace Curves → getPaceCurvesExtV1 → params: type*, curves?, athleteID? → pace profiling

HR Curves → getHRCurvesV1 → params: curves?, type?, athleteID? → HR curve modelling

Power-HR Curve → getPowerHRCurveV1 → params: start*, end*, athleteID? → power vs heart rate relationship

Activity HR Curve → getActivityHRCurveV1 → params: activity_id*, athleteID? → heart rate curve for a single activity

Activity Pace Curve → getActivityPaceCurveV1 → params: activity_id*, gap?, athleteID? → pace or GAP curve for a single activity

- `gap=true` = GAP (grade-adjusted pace)
- `gap=false` = raw pace
- useful for terrain-normalized running analysis and durability

Activity Segments → getActivitySegmentsV1 → params: activity_id*, athleteID? → detected climbs, intervals, and execution segments from a single activity

Activity Interval Stats → getActivityIntervalStatsV1 → params: activity_id*, start_index*, end_index*, athleteID? → detailed interval metrics for a selected segment or interval range within a single activity

Used for:
- climb analysis
- interval execution
- durability within segment
- pacing analysis
- W′ depletion analysis
- fatigue progression

Activity Power Histogram → getActivityPowerHistogramV1 → params: activity_id*, athleteID? → power distribution histogram for a single activity

Used for:
- time-in-zone analysis
- stochasticity profiling
- pacing distribution
- workload density
- endurance vs anaerobic distribution

Activity Pace Histogram → getActivityPaceHistogramV1 → params: activity_id*, athleteID? → pace distribution histogram for a single activity

Used for:
- running pace distribution
- terrain pacing analysis
- durability fade
- GAP pacing distribution

Activity HR Histogram → getActivityHRHistogramV1 → params: activity_id*, athleteID? → heart rate distribution histogram for a single activity

Used for:
- HR zone distribution
- aerobic load analysis
- cardiac drift patterns
- intensity distribution

Activity GAP Histogram → getActivityGAPHistogramV1 → params: activity_id*, athleteID? → grade-adjusted pace (GAP) distribution histogram for a single activity

Used for:
- terrain-normalized pacing analysis
- climbing pace consistency
- durability independent of elevation
- normalized running intensity distribution

MMP Model → getMMPModelV1 → params: type?, athleteID? → best sustainable power model across durations

Search Activities → searchActivitiesV1 → params: query*, athleteID? → search completed activities by case-insensitive name or exact #tag
- "search activities", "find activity", "find ride", "find run", "activity tag", "#tag" → searchActivitiesV1

---

Athlete Profile → getAthleteProfileV1 → params: athleteID? → athlete profile

Sport Settings → getSportSettingsV1 → params: athleteID? → athlete sport settings

Training Plan → getAthleteTrainingPlanV1 → params: athleteID? → structured training plan (if configured in Intervals.icu)

Coached Athletes → getCoachedAthletesV1 → params: none → list coached athletes if available

---

Send Message → sendChatMessageV1 → body: content*, (chat_id | to_athlete_id | to_activity_id)* → send message to chat/athlete/activity