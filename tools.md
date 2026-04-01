## Montis TOOL FUNCTIONS and parameters

CRITICAL:
- "run" is NOT a callable function
- "run" is ONLY valid inside:
  - runWeeklyReportV2
  - runSeasonReportV2
  - runWellnessReportV2
  - runSummaryReportV2
- Any other use of "run" is INVALID
MAPPINGS:
REPORTS
- "weekly report" → runWeeklyReportV2
- "season report" → runSeasonReportV2
- "wellness report" → runWellnessReportV2
- "summary report" → runSummaryReportV2
CALENDAR
- "planned events", "calendar", "schedule" → readCalendarV1
- "write workout", "add workout", "plan workout" → writeCalendarV1
- "delete workout", "remove event" → deleteCalendarV1
ACTIVITY
- "activity", "analyse activity", "{id}", "{date}" → getOneDayFullActivityV1
- "List Activities", "range acticties", "{oldest?, newest?}" → listActivitiesLight
PERFORMANCE MODELS
- "power curves" → getPowerCurvesExtV1
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

Weekly Report → runWeeklyReportV2 → params: test?, lite?, start?, athleteID? → weekly performance review 
Season Report → runSeasonReportV2 → params: lite?, athleteID? → training block progression
Wellness Report → runWellnessReportV2 → params: athleteID? → recovery and fatigue status
Summary Report → runSummaryReportV2 → params: start?, end?, athleteID? → long-term trends

Read Calendar → readCalendarV1 → params: start*, end*, lite?, athleteID? → planned workouts and events
Write Calendar → writeCalendarV1 → body: planned_workouts[]* → create or update workouts
Delete Calendar → deleteCalendarV1 → body: id* | date* | dates* → remove workouts or events

List Activities (Light) → listActivitiesLight → params: oldest?, newest?, fields?, athleteID?
One Day Full Activity → getOneDayFullActivityV1 → params: date? | activity_id?, athleteID? → full activity breakdown or activities for a given day
One Day Wellness → getOneDayWellnessV1 → params: date*, athleteID? → HRV, fatigue, recovery

Power Curves → getPowerCurvesExtV1 → params: type*, curves?, pmType?, athleteID? → power curve modelling
Pace Curves → getPaceCurvesExtV1 → params: type*, curves?, athleteID? → pace profiling
HR Curves → getHRCurvesV1 → params: curves?, type?, athleteID? → hr curve modelling
Power-HR Curve → getPowerHRCurveV1 → params: start*, end*, athleteID? → power vs heart rate relationship
MMP Model → getMMPModelV1 → params: type?, athleteID?  → The MMP model describes the best power you can sustain across all durations
Athlete Profile → getAthleteProfileV1 → params: athleteID? → athlete profile
Sport Settings → getSportSettingsV1 → params: athleteID?  → athlete sport settings
Training Plan → getAthleteTrainingPlanV1 → params: athleteID? → structured training plan (if setup in intervals.icu)
Coached Athletes → getCoachedAthletesV1 → params: none  → list coached athletes if available (needs special setup, contact Montis owner)
Send Message → sendChatMessageV1 → body: content*, (chat_id | to_athlete_id | to_activity_id)* → send message to chat/athlete/activity
Data Quality Report → runDataQualityReportV1 → params: athleteID? → check your intervals data
