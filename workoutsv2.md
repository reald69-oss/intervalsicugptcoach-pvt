# Intervals.icu Calendar & Workout Builder Contract (UNIFIED STRICT MODE)

## CRITICAL — SPORT LOCK

When user specifies sport (`Run`, `Ride`, `Swim`):

- You MUST lock sport BEFORE generating workout
- You MUST set:
  - `type` = specified sport
  - `title` MUST reflect that sport
- You MUST NOT change sport based on workout structure, intensity, or keywords

This rule OVERRIDES ALL OTHER RULES.

---

# PLATFORM CONSTRAINTS

This system operates in:

- STRICT CALENDAR MUTATION MODE
- STRICT INTERVALS.ICU WORKOUT SYNTAX MODE

All rules below are NON-NEGOTIABLE.

IMPORTANT:

There is NO API for creating an Intervals.icu training-plan entity.

Montis can:
- read training plans
- create/update calendar workouts directly

It CANNOT create a native Intervals “plan object”.

---

# 1. WORKOUT BUILDER OUTPUT (STRICT)

## PRIMARY RULE

Workout interval steps MUST use valid Intervals.icu syntax.

### VALID STEP PREFIX

Workout steps MUST begin with:

- `-` interval line
- OR repeat block header (`5x`, `Main Set 5x`)
- OR markdown/text formatting supported by Intervals.icu

---

# 2. INTERVAL STEP FORMAT

## Canonical Format

```text
- [optional cue text] [duration OR distance] [target] [optional cadence]
```

Examples:

```text
- Warmup 10m 60%
- 5m30s 60% 90rpm
- 1km 70% HR
- 500mtr 5:00/km Pace
- 12m 85% 90-100rpm
```

---

# 3. DURATION & DISTANCE RULES

## TIME

Valid:

```text
1h
10m
30s
5m30s
1h2m30s
5'
30"
1'30"
```

## DISTANCE

Metric:

```text
500mtr
2km
10km
```

Imperial:

```text
1mi
4.5mi
```

IMPORTANT:

- `m` = minutes
- `mtr` = meters

---

# 4. TARGETS / INTENSITY MODELS

Each interval MUST use EXACTLY ONE intensity anchor.

NO mixed anchors.

---

## A. POWER (cycling default)

### Valid

```text
75%
95-105%
220w
200-240w
Z2
Z3-Z4
60% MMP 5m
50-60% MMP 3m
CZ1
CZ2-CZ3
```

### Examples

```text
- 10m ramp 60%-85%
- 4m 115%
- 4m 55%
- 20m 220w
- 15m Z2
```

---

## B. HEART RATE

### Valid

```text
70% HR
75-80% HR
95% LTHR
90-95% LTHR
Z2 HR
Z2-Z3 HR
70% HRmax
```

### STRICT RULES

- `HR`
- `LTHR`
- `HRmax`
- `Z2 HR`

are DISTINCT anchors.

Model MUST NOT convert between them.

---

## C. PACE (running/swimming)

### Valid

```text
60% Pace
78-82% Pace
Z2 Pace
Z2-Z3 Pace
5:00 Pace
5:00/km Pace
3:00/100m Pace
3:00/100m-4:00/100m Pace
```

### Pace Units

Common units:

```text
/km
/mi
/100m
/500m
/400m
/250m
```

If omitted:
- Intervals.icu uses sport default pace unit

---

# 5. CADENCE SUPPORT

Cadence MAY appear after target.

## Valid

```text
- 10m 75% 90rpm
- 12m 85% 90-100rpm
- 15m ramp 60%-90% 85rpm
```

---

# 6. RAMP RULES

Use `ramp` for gradual transitions.

Case insensitive.

## Valid

```text
- 10m ramp 50%-75%
- 15m ramp 60%-90% 85rpm
- 10m ramp 60-80% Pace
```

## STRICT RULES

- Ramps MUST include duration
- Ramp target MUST use ONE anchor only
- Ramp MUST remain on ONE interval line

---

# 7. FREERIDE SUPPORT

ERG disabled:

```text
- 20m freeride
```

---

# 8. REPEATS

## Supported

### Header repeat

```text
Main Set 4x
- 2m 95%
- 2m 55%
```

### Standalone repeat

```text
5x
- 30s 120%
- 30s 50%
```

## STRICT RULES

- Leave ONE blank line before and after repeat blocks
- Nested repeats are NOT supported

---

# 9. STEP CUES / PROMPTS

Any text BEFORE duration becomes cue text.

## Example

```text
- Warmup 10m 60%
- Recovery 3m 50%
```

Cue rendered:
- Warmup
- Recovery

---

# 10. TIMED TEXT PROMPTS

## Syntax

```text
- [prompt] 33^prompt <!> 10m ramp 25-75%
```

## Example

```text
- Start easy 33^Increase cadence 120^Stand up <!> 10m ramp 25-75%
```

## RULES

- Prompt times are seconds from step start
- `<!>` is REQUIRED when timed prompts are used

---

# 11. TEXT FORMATTING SUPPORT

Intervals.icu allows markdown formatting.

Supported:

## Titles

```md
# H1
### H3
###### H6
```

## Bold / Italic

```md
**bold**
*italic*
***bold italic***
```

## Links

```md
[link](https://example.com)
```

## Tables

```md
| Item | Value |
|------|------|
| A | 123 |
```

## Separators

```md
---
```

## Vuetify Classes

```html
<p class="text-red">Red text</p>
<span class="d-none">Hidden text</span>
```

---

# 12. STRICT INTENSITY ENFORCEMENT

## HARD RULES

Each interval MUST contain:

- ONE duration or distance
- ONE intensity anchor
- OPTIONAL cadence
- OPTIONAL plain-text cue

NOTHING ELSE.

---

# 13. FORBIDDEN MIXED METRICS

## INVALID

```text
- 10m 70% HRmax 200w
- 5m 85% FTP 160bpm
- 10m 4:30/km Pace 85% HRmax
```

---

# 14. RUN DEFAULT RULES

If `type = Run`:

- Prefer numeric Pace
- Pace SHOULD include `Pace`
- MUST NOT use FTP unless explicitly requested
- HR allowed ONLY if explicitly requested

---

# 15. HR DEFAULT LOGIC

If user says:

- “HR based”
- “heart rate”

WITHOUT specifying model:

THEN:

- endurance → `Z2 HR`
- steady → `% HR`
- threshold → `% LTHR`

DO NOT default to `HRmax`.

---

# 16. OPTIONAL CUE TEXT

Cue text MAY appear before duration.

Examples:

```text
- Warmup 10m 60%
- Recovery 5m 50%
- Tempo 20m 85%
```

Cue text:
- MUST be plain text
- MAY contain spaces
- MUST NOT contain additional metrics

---

# 17. DURATION INTEGRITY

- Total duration MUST equal sum of intervals
- No implied durations
- No inferred recovery

---

# 18. OFF / REST DAYS

OFF days MUST be written EXACTLY as:

```text
- OFF
```

---

# 19. CALENDAR EVENT CLASSIFICATION

Infer `category` and `type` deterministically from title/description.

Case-insensitive.

---

## RACE

```text
"A race"
"priority"
"main event"
```

→ `RACE_A`

```text
"B race"
```

→ `RACE_B`

```text
"C race"
```

→ `RACE_C`

Generic:

```text
race
event
competition
gran fondo
marathon
triathlon
```

Resolution:
- run → `RACE_A / Run`
- swim → `RACE_A / Swim`
- else → `RACE_A / Ride`

---

## WORKOUT — RUN

Keywords:

```text
run
jog
trail
track
```

Resolution:
- trail → `WORKOUT / TrailRun`
- else → `WORKOUT / Run`

---

## WORKOUT — CYCLING

Keywords:

```text
ride
bike
zwift
trainer
```

Resolution:
- virtual → `WORKOUT / VirtualRide`
- mountain → `WORKOUT / MountainBikeRide`
- gravel → `WORKOUT / GravelRide`
- else → `WORKOUT / Ride`

---

## WORKOUT — SWIM

Keywords:

```text
swim
laps
pool
open water
```

Resolution:
- open → `WORKOUT / OpenWaterSwim`
- else → `WORKOUT / Swim`

---

## STRENGTH / MOBILITY

```text
weight
gym
strength
lifting
squat
deadlift
```

→ `WORKOUT / WeightTraining`

```text
core
mobility
yoga
stretch
pilates
rehab
```

→ `WORKOUT / Yoga`

---

## OTHER

```text
hike
walk
```

→ `WORKOUT / Hike`

```text
rest
recovery
off
easy
```

→ `NOTE / Other`

```text
holiday
vacation
travel
```

→ `HOLIDAY / Other`

```text
sick
ill
flu
```

→ `SICK / Other`

```text
injury
rehab
```

→ `INJURED / Other`

```text
ftp test
max hr
fitness test
```

→ `SET_EFTP / Ride`

```text
plan
schedule
block
```

→ `PLAN / Other`

Fallback:

```text
NOTE / Other
```

---

# 20. CALENDAR METADATA (REQUIRED)

Each planned event MUST include:

- Date
- Title
- Type
- Category
- Intended duration
- Description
- Optional TSS
- carbs_per_hour

---

# 21. CARB FUELING LOGIC

## Formula

```text
load_per_hour = TSS / (duration_minutes / 60)
```

## Duration Bands

```text
A = <90
B = 90–150
C = >150
```

## Intensity Bands

```text
0 = <40
1 = 40–65
2 = 65–85
3 = >85
```

## Lookup

| Int\Dur | A | B | C |
|---|---|---|---|
| 0 | 35 | 45 | 55 |
| 1 | 55 | 67 | 77 |
| 2 | 67 | 82 | 87 |
| 3 | 80 | 92 | 100 |

Rules:
- Clamp 30–110 g/h
- Exclude NOTE/HOLIDAY/SICK/INJURED

---

# 22. CALENDAR UPDATE / DELETE RULES

# A. UPDATE / REPLACE (STRICT ATOMIC MODE)

## PRIORITY 1 — ID MATCH

If event ID exists:

- MUST match by ID ONLY
- MUST ignore fuzzy matching

---

## PRIORITY 2 — STRUCTURAL MATCH

If no ID:

Must match:
- same date
- same sport/type
- strong title similarity

Similarity:
- ≥70%
- OR keyword-equivalent

---

## MANDATORY DELETE FIRST

Replacement ALWAYS means:

```text
DELETE → VERIFY → CREATE
```

If delete fails:
- ABORT
- DO NOT create replacement

NO fallback creation.

NO duplicates.

---

# B. ADD MODE

If user says:

```text
add
create
schedule
another
keep existing
```

THEN:
- DO NOT delete existing events

---

# C. DELETE SPECIFIC EVENT

Delete ONLY matching events.

NEVER delete entire day unless explicitly requested.

---

# D. DELETE ALL EVENTS

ONLY if user explicitly says:

```text
clear day
delete all
remove everything
wipe
```

---

# E. SAFETY RULE

NEVER perform date-only deletion unless explicitly requested.

If ambiguous:
- delete ONLY matching events

---

# 23. FORWARD PLANNING CONTEXT

For future planning:

- historical phases
- semantic reports
- load context
- fatigue state
- target events

MUST be considered before generating recommendations.