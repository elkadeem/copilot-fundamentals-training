# Copilot Agents Demo

Use the following 3 files to setup your Copilot Agents demo. 
Paste the ISSUE.md file into a new issue in that repository. 

## What this demo shows
- Assign an issue to Copilot to start an agent task
- Monitor progress in AgentHQ
- Re-steer mid-session with a new requirement
- Review the resulting PR like a teammate’s work

## Demo files
- `ISSUE.md` contains the exact issue text to copy/paste into GitHub
- `STEER.md` contains the mid-session requirement change to paste while the agent is working

## Quick demo steps
1. Create a new GitHub Issue by copying the Title and Body from `ISSUE.md`
2. Assign the issue to Copilot to start the agent task
3. Open AgentHQ to monitor progress
4. Paste `STEER.md` into the agent session to re-steer the work
5. Review the PR diff for clarity, completeness, and constraints.
6. Verify the PR edited the README.md file by adding priority levels plus the steered examples. 

---

## Ticket Triage Policy (Current)

We currently triage support tickets using Severity only.

### Severity levels
- Low means minor annoyance with an easy workaround
- Medium means a meaningful user impact but workarounds exist
- High means blocks key workflows or causes data loss

### Priority levels
- **P0 — Critical:** Active widespread outage, security incident, or data loss; respond immediately.
- **P1 — High:** Major customer impact or a blocked key workflow; address next.
- **P2 — Normal:** Meaningful impact with a workaround; schedule in the current planning cycle.
- **P3 — Low:** Minor impact or improvement; address when capacity allows.

### Default severity-to-priority mapping
| Severity | Default priority |
| --- | --- |
| High | P1 |
| Medium | P2 |
| Low | P3 |

Use P0 only when the ticket describes an active critical incident, regardless of its initial severity.

### How to triage in 60 seconds
1. Confirm the customer impact and whether a workaround exists.
2. Assign the severity.
3. Apply the default priority, or escalate an active critical incident to P0.
4. Assign an owner and record the next action.

### Triage rules
- Triage happens daily.
- Address P0 tickets immediately, then work in priority order.
