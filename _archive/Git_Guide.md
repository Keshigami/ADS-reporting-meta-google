# Git Guide
## For ADS Reporting System Repository

---

## Repository Info

**URL:** https://github.com/Keshigami/ADS-reporting-meta-google  
**Branch:** main  
**Local Path:** `d:\Operations\Meta & Google ADS`

---

## Quick Commands

### Check Status
```powershell
git status
```
See what files have changed

---

### Pull Latest Changes
```powershell
git pull
```
Get updates from GitHub before making changes

---

### Save Your Changes (Commit & Push)

```powershell
# Step 1: Stage all changes
git add -A

# Step 2: Commit with message
git commit -m "Your description of changes"

# Step 3: Push to GitHub
git push
```

---

### View Recent History
```powershell
git log -n 5
```
Shows last 5 commits

---

## Common Scenarios

### Scenario: Made changes, need to save them

```powershell
# 1. Check what changed
git status

# 2. Stage changes
git add -A

# 3. Commit (describe what you did)
git commit -m "Updated call tracking options"

# 4. Push to GitHub
git push
```

---

### Scenario: Need to get teammate's updates

```powershell
git pull
```

If you get a conflict, ask for help or see troubleshooting below.

---

### Scenario: Undo changes to a file (before committing)

```powershell
# Undo changes to a specific file
git checkout -- filename.md

# Undo ALL uncommitted changes (careful!)
git checkout -- .
```

---

### Scenario: See what changed in a file

```powershell
git diff filename.md
```

---

## File Types in This Repo

| Type | Extensions | Purpose |
|------|------------|---------|
| Documentation | `.md` | Guides, specs, summaries |
| Workflows | `.json` | n8n workflow exports |
| Config | `.gitignore` | Files to exclude from Git |

---

## Best Practices

### Commit Messages
Good examples:
- `Add call tracking documentation`
- `Update workflow to include phone metrics`
- `Fix typo in setup guide`

Bad examples:
- `update`
- `fixed stuff`
- `asdf`

### When to Commit
- After completing a logical unit of work
- Before leaving for the day
- Before making risky changes

### When to Pull
- First thing when you start working
- Before pushing to avoid conflicts

---

## Troubleshooting

### "Please tell me who you are"
```powershell
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### "Updates were rejected"
Someone else pushed changes. Pull first, then push:
```powershell
git pull
git push
```

### Merge conflict
Open the conflicting file, look for:
```
<<<<<<< HEAD
your changes
=======
their changes
>>>>>>> origin/main
```
Edit to keep what you want, remove the markers, then:
```powershell
git add -A
git commit -m "Resolved merge conflict"
git push
```

---

## Team Access

To give someone access:
1. Go to GitHub repo → Settings → Collaborators
2. Add their GitHub username
3. They'll get an invite email

---

## Files in Repository

```
ADS-reporting-meta-google/
├── README.md                    - Project overview
├── .gitignore                   - Files to ignore
│
├── WORKFLOWS/
│   ├── n8n_workflow_weekly_ads_report.json
│   └── n8n_workflow_ad_account_discovery.json
│
├── SETUP/
│   ├── SETUP_GUIDE.md
│   └── notion_database_schemas.md
│
├── CALL TRACKING/
│   ├── Call_Tracking_Options_For_Jake.md
│   ├── Call_Tracking_Strategy.md
│   └── Phone_Number_Porting_Guide.md
│
├── REFERENCE/
│   ├── Executive_Summary_Weekly_Ads_System.md
│   ├── Weekly_Ads_Reporting_System_Specification.md
│   └── Budget_Stack_Free_Alternatives.md
│
└── NOTES/
    └── Conversation_Summary_Dec22.md
```

---

## Need Help?

- **Git basics:** https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
- **GitHub Docs:** https://docs.github.com
- **Ask in Slack/Discord**

---

*Last Updated: December 22, 2024*
