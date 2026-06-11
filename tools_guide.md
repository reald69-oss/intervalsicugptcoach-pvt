# 🧭 MONTIS MCP TOOLSET — NATURAL LANGUAGE GUIDE

## 📊 Reporting Tools

### Weekly Report
- Reviews your last 7 days of training
- Shows load, fatigue, recovery, durability, intensity balance
- Gives clear coaching decisions for what to do next
- Use this when you want: **weekly coaching + direction**

---

### Weekly Overview
- Compact dashboard-style weekly summary
- Highlights key load, recovery and performance metrics
- Optimized for quick review
- Use this when you want: **a concise weekly snapshot**

---

### Weekly Workflow
- Coaching workflow dashboard
- Combines performance, readiness, planning and next actions
- Designed to support coaching decisions
- Use this when you want: **what should I do next?**

---

### Season Report
- Reviews your last ~90 days
- Identifies phases such as Base, Build and Recovery
- Tracks long-term progress and system development
- Use this when you want: **big-picture progression**

---

### Wellness Report
- Focuses on recovery and readiness
- Uses HRV, resting HR, fatigue signals
- Use this when you want: **recovery status**

---

### Summary Report
- Lets you analyze any date range
- Compares trends across specific periods
- Use this when you want: **custom comparisons**

---

### Data Quality Check
- Checks for missing or inconsistent data
- Helps ensure your analysis is accurate
- Use this when: **something feels off**

---

### Connection Status
- Checks that Montis can access your Intervals.icu data
- Validates MCP authentication and athlete resolution
- Use this when: **something does not look connected**

---

## 📅 Planning & Calendar Tools

### View Planned Workouts
- Shows upcoming sessions
- Helps you understand your weekly structure
- Use this when: **reviewing your plan**

---

### Update Calendar
- Create or update planned calendar events
- Allows precise workout scheduling
- Use this when: **adjusting your training plan**

---

### Delete Calendar Events
- Remove specific workouts or blocks from the calendar
- Use this when: **clearing space or correcting your plan**

---

### Workout Library
- Access saved workout templates and planned workouts
- Primarily used by workout-building workflows
- Useful for reviewing available workout structures

---

## 🏃 Activity Analysis Tools

### Analyze Specific Activity or Day
- Deep dive into one workout or one day
- Shows intervals, power, heart rate, pacing and effort breakdown
- Use this when: **reviewing a specific session**

---

### List Recent Activities
- Shows a lightweight history of recent workouts
- Use this when: **scanning your training history**

---

### Search Activities
- Search completed activities by name or exact tag
- Name search is case-insensitive
- Tag search is exact when the query starts with `#`
- Returns matching activity IDs and metadata
- Use this when: **finding a specific past session**

---

### Activity HR Curve
- Heart rate curve for a single activity
- Use this to analyze physiological response for a specific session

---

### Activity Pace Curve
- Pace or GAP curve for a single activity
- `gap=true` = GAP
- `gap=false` = raw pace
- Useful for terrain-normalized running analysis and durability

---

### Activity Segments
- Detected climbs, intervals and execution segments from a single activity
- Provides indexes for curve analysis and interval stats
- Use this when: **breaking a session into meaningful parts**

---

### Activity Interval Stats
- Detailed interval metrics for a selected segment or index range
- Used for climb analysis, interval execution, durability, pacing, W′ depletion and fatigue progression

---

### Activity Power Histogram
- Power distribution histogram for a single activity
- Useful for time-in-zone, stochasticity and workload density

---

### Activity Pace Histogram
- Pace distribution histogram for a single activity
- Useful for running pace distribution, terrain pacing and durability fade

---

### Activity HR Histogram
- Heart-rate distribution histogram for a single activity
- Useful for HR zones, aerobic load and cardiac drift patterns

---

### Activity GAP Histogram
- Grade-adjusted pace distribution histogram for a single activity
- Useful for terrain-normalized pacing and climbing consistency

---

### Activity Best Efforts
- Finds best efforts inside a specific activity
- Supports power and heart-rate streams
- Useful for identifying peak intervals and standout efforts

---

### Activity Map
- Returns route geometry and map information
- Useful for route inspection and geographic analysis
- Use this when: **reviewing where an activity occurred**

---

### Terrain Execution Analysis
- Analyzes trail and running activities by terrain segment
- Evaluates pacing, climbing, descending and execution quality
- Useful for race-course and trail analysis
- Use this when: **understanding how terrain affected performance**

---

## ⚙️ Performance Analysis Tools

### Power Curve Analysis
- Shows your best power across durations
- Tracks performance trends
- Use this when: **checking fitness changes**

---

### Activity Power Curve
- Maximal mean power curve for a single activity
- `kj0` = fresh baseline curve
- `kj1` = fatigued-state curve
- Useful for durability, fatigue resistance, repeatability and late-ride decay

---

### Pace Curve Analysis
- Shows pace vs duration performance
- Use this when: **analyzing run or swim fitness**

---

### Heart Rate Curve Analysis
- Shows how your heart rate behaves across efforts
- Use this when: **understanding cardiovascular response**

---

### Power vs Heart Rate Analysis
- Compares effort vs physiological response
- Helps detect efficiency and fatigue
- Use this when: **checking aerobic efficiency**

---

### Maximum Effort Model
- Shows your best sustained outputs across durations
- Defines your true performance capacity
- Use this when: **understanding your limits**

---

### Shared Event & Course Analysis
- Reads Intervals shared events and race courses
- Can load full course data including route and terrain information
- Useful for race preparation and course forecasting
- Use this when: **analyzing a future event or race course**

---

## 👤 Athlete Data Tools

### Athlete Profile
- Shows key athlete settings such as FTP, HR zones and weight
- Use this when: **checking baseline metrics**

---

### Sport Settings
- Shows how training zones are defined
- Use this when: **validating zones**

---

### Training Plan
- Shows any structured plan already configured
- Use this when: **reviewing an existing plan**

---

## 👥 Coaching Tools

### Coaching Roster
- Custom feature for coaches
- Returns a list of athletes managed by the coach
- Returns null if coaching setup is not configured
- Use this when: **managing an athlete roster**

---

## 🚫 Removed / Not Available

### Chat / Send Message
- Chat and send-message tools are not currently available in MCP
- Do not route message requests to a tool

---

## 🎯 Simple Summary

- **Reports** → explain what’s happening
- **Activity tools** → explain why
- **Performance tools** → show trends
- **Planning tools** → change what you do
- **Data tools** → ensure accuracy
- **Course tools** → prepare for events and terrain

---

## 🧠 One Line

This system lets you:
> **analyze training, understand physiology, inspect activities and courses, and adjust the plan from real data**