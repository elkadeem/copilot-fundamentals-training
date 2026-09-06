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

Triage daily: confirm impact and workaround, assign severity and priority, then assign an owner and next action.

### Severity levels
| Severity | Meaning |
| --- | --- |
| Low | Minor annoyance with an easy workaround. |
| Medium | Meaningful impact with a workaround. |
| High | Blocks key workflows or causes data loss. |

### Priority levels
| Priority | Meaning |
| --- | --- |
| P0 | Active widespread outage, security incident, or data loss; respond immediately. |
| P1 | Major customer impact or blocked key workflow; address next. |
| P2 | Meaningful impact with a workaround; schedule this planning cycle. |
| P3 | Minor impact or improvement; address when capacity allows. |

### Default severity-to-priority mapping
High → P1 (P0 for active data loss); Medium → P2; Low → P3. Use P0 for an active critical incident, regardless of initial severity.

### How to triage in 60 seconds
1. Confirm impact and workaround.
2. Assign severity.
3. Apply the default priority (or P0).
4. Assign owner and next action.
