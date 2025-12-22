# Setup Guide
## Weekly Ads Reporting System

---

## Prerequisites

- Local n8n instance running
- Google Workspace account
- Meta Business account with API access
- Google Ads account with API access
- GoHighLevel account with API key
- Notion account
- (Optional) Slack workspace

---

## Step 1: Create Notion Databases

1. **Open Notion** and create a new page called "Ads Reporting"

2. **Create "Clients" Database** (see `notion_database_schemas.md` for properties)
   - Add at least one test client with:
     - Status: Active
     - Meta Ad Account ID
     - Google Ads Customer ID
     - Stakeholder Emails

3. **Create "Client Reports" Database**
   - Add relation to Clients

4. **Create "Agency Dashboard" Database**

5. **Get Database IDs** from URLs:
   ```
   https://notion.so/yourworkspace/DATABASE_ID?v=...
                                    ^^^^^^^^^^^^
   ```

---

## Step 2: Create Google Drive Folder

1. Go to Google Drive
2. Create folder: `Ads Reports`
3. Get folder ID from URL:
   ```
   https://drive.google.com/drive/folders/FOLDER_ID
                                          ^^^^^^^^^
   ```

---

## Step 3: Configure n8n Credentials

In n8n → Settings → Credentials, create:

### Notion API
- Type: Notion API
- Internal Integration Token: Create at https://www.notion.so/my-integrations
- Share databases with your integration!

### Google OAuth2 (for Docs, Drive, Gmail)
- Type: Google OAuth2 API
- Client ID & Secret from Google Cloud Console
- Scopes: `https://www.googleapis.com/auth/drive`, `https://www.googleapis.com/auth/documents`, `https://www.googleapis.com/auth/gmail.send`

### Meta Marketing API
- Type: Facebook Graph API
- Create app at https://developers.facebook.com
- Get access token with `ads_read` permission

### Google Ads API
- Type: Google Ads OAuth2
- Developer token from Google Ads API Center
- Client ID & Secret from Google Cloud Console

### GHL API
- Type: Header Auth
- Header Name: `Authorization`
- Header Value: `Bearer YOUR_GHL_API_KEY`

### Slack (Optional)
- Type: Slack OAuth2
- Create app at https://api.slack.com/apps

---

## Step 4: Set Environment Variables

In n8n → Settings → Variables (or `.env` file):

```
NOTION_CLIENTS_DB_ID=abc123...
NOTION_REPORTS_DB_ID=def456...
NOTION_AGENCY_DB_ID=ghi789...
GOOGLE_DRIVE_REPORTS_FOLDER_ID=1ABC...
AGENCY_TEAM_EMAILS=jake@agency.com,team@agency.com
```

---

## Step 5: Import Workflow

1. In n8n → Workflows → Import from File
2. Select `n8n_workflow_weekly_ads_report.json`
3. Workflow will load with placeholder credentials
4. Click each node with ⚠️ and assign your credentials
5. Save workflow

---

## Step 6: Update Credential IDs

The workflow JSON has placeholder credential IDs. You need to update these:

| Placeholder | Replace With |
|-------------|--------------|
| `NOTION_CRED_ID` | Your Notion credential ID |
| `GOOGLE_DOCS_CRED_ID` | Your Google Docs OAuth2 ID |
| `GOOGLE_DRIVE_CRED_ID` | Your Google Drive OAuth2 ID |
| `META_CRED_ID` | Your Meta API credential ID |
| `GOOGLE_ADS_CRED_ID` | Your Google Ads OAuth2 ID |
| `GHL_CRED_ID` | Your GHL Header Auth ID |
| `GMAIL_CRED_ID` | Your Gmail OAuth2 ID |
| `SLACK_CRED_ID` | Your Slack credential ID |

---

## Step 7: Test with One Client

1. Ensure you have one Active client in Notion with valid ad account IDs
2. In n8n, click "Execute Workflow"
3. Watch the execution - check each node's output
4. Verify:
   - [ ] Data fetched from Meta and Google
   - [ ] PDF created in Google Drive
   - [ ] Notion entry created in Client Reports
   - [ ] GHL contact updated
   - [ ] Email sent to stakeholders
   - [ ] Agency Dashboard updated
   - [ ] Slack notification received

---

## Step 8: Enable Schedule

1. In n8n, open the workflow
2. Toggle the workflow to **Active** (top right)
3. The "Weekly Monday 9AM" trigger will now run automatically

---

## Troubleshooting

### "Invalid access token" for Meta
- Regenerate token in Meta Business Suite
- Ensure token has `ads_read` permission

### "Permission denied" for Google
- Re-authorize OAuth2 in n8n
- Check scopes include Drive, Docs, Gmail

### "Database not found" for Notion
- Ensure database is **shared** with your integration
- Check database ID is correct (from URL)

### No data returned
- Check date ranges are correct
- Verify ad account IDs match exactly
- Ensure there was actual ad activity in the date range

---

## Webhook for On-Demand Reports

To trigger a report manually via webhook:

```bash
curl -X POST https://your-n8n-instance.com/webhook/weekly-ads-report \
  -H "Content-Type: application/json" \
  -d '{"client_code": "MEC001"}'
```

---

## File Structure

```
d:\Operations\Meta & Google ADS\
├── README.md
├── Executive_Summary_Weekly_Ads_System.md
├── Weekly_Ads_Reporting_System_Specification.md
├── Budget_Stack_Free_Alternatives.md
├── n8n_workflow_weekly_ads_report.json    ← Import this into n8n
├── notion_database_schemas.md              ← Reference for Notion setup
└── SETUP_GUIDE.md                          ← This file
```

---

## Support

Questions? Check the following:
- n8n Community: https://community.n8n.io
- Notion API Docs: https://developers.notion.com
- Meta Marketing API: https://developers.facebook.com/docs/marketing-apis
- Google Ads API: https://developers.google.com/google-ads/api/docs/start
