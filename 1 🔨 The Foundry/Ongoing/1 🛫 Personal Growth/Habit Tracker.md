# Habit Tracker

Track daily habits and visualize your progress over time.

---

## How to Use

1. **Open today's daily note** - Click the calendar icon or press `Cmd+P` → "Open today's daily note"
2. **Mark completed habits** - Add `1` after the `::` for each habit you completed
3. **Charts update automatically** as you log more days

**Example:**
```
gratitude:: 1
meditation:: 1
exercise::
```

---

## This Month

### Morning Routine
```tracker
searchType: dvField
searchTarget: gratitude, meditation, candle
datasetName: Gratitude, Meditation, Candle
folder: /
month:
    startWeekOn: Mon
    color: green
```

### Health Habits
```tracker
searchType: dvField
searchTarget: exercise, stretch
datasetName: Exercise, Stretch
folder: /
month:
    startWeekOn: Mon
    color: blue
```

### Creative
```tracker
searchType: dvField
searchTarget: drawing
datasetName: Drawing
folder: /
month:
    startWeekOn: Mon
    color: purple
```

### Relationship
```tracker
searchType: dvField
searchTarget: camille_checkin
datasetName: Camille Check-in
folder: /
month:
    startWeekOn: Mon
    color: pink
```

---

## Summary (Last 30 Days)

```tracker
searchType: dvField
searchTarget: gratitude, meditation, exercise, drawing, camille_checkin
datasetName: Gratitude, Meditation, Exercise, Drawing, Camille
folder: /
summary:
    template: "Total completions: {{sum()}}"
```

---

## Habit Details

| Habit | Target | How to Log |
|-------|--------|------------|
| 🙏 Gratitude | Daily | `gratitude:: 1` |
| 🧘 Meditation | Daily | `meditation:: 1` |
| 🕯️ Light Candle | Daily | `candle:: 1` |
| 💪 Exercise | 5x/week | `exercise:: 1` |
| 🧘 Stretch | Daily | `stretch:: 1` |
| ✏️ Drawing | 5x/week | `drawing:: 1` |
| 💬 Camille Check-in | Daily | `camille_checkin:: 1` |

---

## Related

- [[Templates/Daily Note Template]] - Template for daily notes
- [[Daily Practices & Reminders]] - Daily rituals
- [[Wellness Hub]] - Health hub
