# DoorGuard Ultra™ 🔐
### Enterprise Security Suite v12.0 — *Because opening a door should never be easy*

> **AISC Oops-a-thon submission** · Theme: Over-Secured System

---

## What is this?

A satirical web app that makes you complete **7 absurd security checks** just to open a regular door.

The twist? **The door was already open the whole time. Since 2019. No one checked.**

---

## The 7 Checks

| Step | Name | What happens |
|------|------|-------------|
| 1 | **CAPTCHA** | Sometimes asks you to select "your deepest regrets" |
| 2 | **Fax OTP** | Sends a 6-digit code to your fax machine (hint: it shows you the code) |
| 3 | **AI Vibe Check** | VibeNet™ analyzes your "Stack Overflow visits today" and "variable naming sentiment" |
| 4 | **Face Scan** | Compares your face to your Facebook profile from 2011 |
| 5 | **Terms & Conditions** | 847 pages. Section 7 just says "The door is just a door." |
| 6 | **Countdown** | 10 seconds to confirm. If you hesitate, all progress resets. |
| 7 | **Access Granted** | The door opens. It was already open. |

---

## Run It

No install. No server. No dependencies.

```bash
git clone https://github.com/YOUR_USERNAME/doorguard-ultra
cd doorguard-ultra
# just open index.html in any browser
open index.html
```

Or just double-click `index.html`.

---

## Project Structure

```
doorguard-ultra/
├── index.html              # Entry point
├── css/
│   ├── base.css            # Design tokens, resets, typography helpers
│   ├── layout.css          # Statusbar, app grid, door panel, step tracker
│   ├── components.css      # Buttons, badges, captcha, OTP, vibe, face, terms
│   ├── modals.css          # Modal overlay and box styles
│   └── animations.css      # All keyframe animations
└── js/
    ├── utils.js            # delay(), toast(), randomPick(), randInt(), randFloat()
    ├── state.js            # AppState — single source of truth
    ├── ui.js               # UI controller — modals, step tracker, door, clock
    ├── main.js             # Pipeline orchestrator + DOMContentLoaded bootstrap
    └── steps/
        ├── captcha.js      # Step 1: CAPTCHA (normal + existential)
        ├── otp.js          # Step 2: Fax OTP
        ├── vibe.js         # Step 3: AI Vibe Analysis
        ├── face.js         # Step 4: Facial expression scan
        ├── terms.js        # Step 5: Terms & Conditions
        ├── countdown.js    # Step 6: Final countdown
        └── success.js      # Step 7: Access granted
```

---

## Tech Stack

- **Vanilla HTML/CSS/JS** — zero frameworks, zero dependencies
- **No build step** — just open and run
- Works on any modern browser

---

## Theme

**Over-Secured System** — A system designed to perform a simple task (opening a door) that constantly doubts, questions, and second-guesses the user in unnecessary and unpredictable ways.

---

*Made for AISC community events. All security vulnerabilities are intentional.*
