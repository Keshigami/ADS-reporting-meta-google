# ADS Reporting System - Meta & Google

Automated weekly ads reporting system for digital agencies using n8n, Notion, GoHighLevel, and PDF generation.

## Overview

This repository contains the design specifications and implementation guides for an automated weekly ads reporting system that:

- Pulls data from Meta Ads and Google Ads APIs
- Generates professional PDF reports per client
- Stores reports in Google Drive and Notion
- Updates GoHighLevel CRM with key metrics
- Emails stakeholders with executive summaries

## Documentation

| Document | Description |
|----------|-------------|
| [Executive Summary](Executive_Summary_Weekly_Ads_System.md) | High-level overview for decision makers with stack options |
| [Technical Specification](Weekly_Ads_Reporting_System_Specification.md) | Detailed n8n workflow, Notion schema, GHL config, LaTeX templates |

## Recommended Stack

- **Data Aggregation**: Supermetrics ($99/mo)
- **Automation**: n8n (self-hosted)
- **PDF Generation**: Carbone.io ($50/mo)
- **Storage**: Google Drive
- **CRM**: GoHighLevel
- **Database**: Notion

## Project Status

- [x] System architecture designed
- [x] n8n workflow specified (20+ nodes)
- [x] LaTeX template created
- [x] Notion database schema defined
- [x] GHL configuration documented
- [ ] Supermetrics setup
- [ ] Carbone.io integration
- [ ] n8n workflow implementation
- [ ] Testing with pilot client
- [ ] Full rollout

## License

Proprietary - Internal Use Only
