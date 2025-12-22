# ADS Reporting System - Meta & Google

Automated weekly ads reporting system for digital agencies using **local n8n**, Notion, GoHighLevel, and Google Docs PDF generation.

## Overview

This system generates **two types of weekly reports**:

1. **Client Reports** - Professional PDFs sent to each client with KPIs, campaign breakdown, and recommendations
2. **Agency Dashboard** - Internal summary across all clients with health status and anomaly tracking

```
┌──────────────┐     ┌──────────────┐
│  Meta Ads    │     │  Google Ads  │
└──────┬───────┘     └──────┬───────┘
       └─────────┬─────────┘
                 ▼
       ┌─────────────────────┐
       │   n8n (Local)       │
       │  Weekly Cron 9 AM   │
       └─────────┬───────────┘
                 │
    ┌────────────┼────────────┐
    ▼            ▼            ▼
┌────────┐  ┌────────┐  ┌──────────┐
│ PDF    │  │ Notion │  │ GHL      │
│ Report │  │ DB     │  │ Update   │
└────────┘  └────────┘  └──────────┘
```

## Quick Start

1. **Import workflow**: `n8n_workflow_weekly_ads_report.json` → n8n
2. **Create Notion databases**: See `notion_database_schemas.md`
3. **Configure credentials**: See `SETUP_GUIDE.md`
4. **Test with one client**
5. **Enable weekly schedule**

## Files

| File | Purpose |
|------|---------|
| `n8n_workflow_weekly_ads_report.json` | **Import this into n8n** |
| `SETUP_GUIDE.md` | Step-by-step setup instructions |
| `notion_database_schemas.md` | Notion database property specs |
| `Executive_Summary_Weekly_Ads_System.md` | Overview for decision makers |
| `Weekly_Ads_Reporting_System_Specification.md` | Full technical spec |
| `Budget_Stack_Free_Alternatives.md` | Cost comparison and alternatives |

## Stack (FREE)

| Component | Tool | Cost |
|-----------|------|------|
| Automation | n8n (local) | $0 |
| Data Pull | Direct APIs | $0 |
| PDF Generation | Google Docs → PDF | $0 |
| Storage | Google Drive | $0 |
| Dashboard | Notion | $0 |
| CRM | GoHighLevel | (existing) |
| **Total** | | **$0/month** |

## Project Status

- [x] System architecture designed
- [x] n8n workflow created (20+ nodes)
- [x] Notion database schemas defined
- [x] GHL configuration documented
- [x] Setup guide written
- [ ] API credentials configured
- [ ] Notion databases created
- [ ] Test with pilot client
- [ ] Full rollout

## License

Proprietary - Internal Use Only
