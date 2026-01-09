# Prompt for Claude Desktop

Please copy and paste the following prompt into Claude Desktop to resolve your n8n workflow issue:

***

Fix and complete my n8n workflow "AI marketing report" (ID: `dehdebZNl23vsgoX`) at `http://localhost:5678`.

## Current Problem

The workflow has broken tool references to sub-workflows that don't exist. Remove the AI Agent approach and rebuild with direct connections.

## Desired Architecture

Please implement the following simplified flow:

```
Trigger (Weekly Monday 9AM + Manual)
     │
     ▼
Set Date Range (last 7 days variables)
     │
┌────┼────┐
▼    ▼    ▼
Google   Meta    GHL
Ads      Ads     Opps
│    │    │
▼    ▼    ▼
Process  Process Process
│    │    │
└────┼────┘
     ▼
Merge All Data
     │
     ▼
Calculate ROAS (Code Node)
     │
     ▼
Discord (Send Weekly Report)
```

## Node Requirements

1. **Triggers**:
   - Schedule Trigger: Weekly, Monday at 9:00 AM.
   - Manual Trigger: Webhook or Manual Execute for testing.

2. **Date Setup**:
   - Calculate `start_date` and `end_date` for the last 7 days.

3. **Data Sources (Parallel Branches)**:
   - **Google Ads**:
     - Pull campaign performance: spend, clicks, conversions, conversions_value.
     - **Credential**: Use existing `googleAdsOAuth2Api`.
     - **Customer ID**: `3300525230`
     - **Developer Token**: `fzQ2U5IcU4ZH0vBDn4Slww`
   - **Meta Ads**:
     - Pull account insights: spend, clicks, actions (leads), action_values.
     - **Credential**: Use existing ID `z8gP5ZZAbWdJ6ONT` (Facebook Graph API).
     - **Account ID**: `act_54337533`
   - **GoHighLevel (GHL)**:
     - Pull opportunities with status "won" to calculate true revenue.
     - **API**: `https://services.leadconnectorhq.com`
     - **Location ID**: `FrSOvqFDYNjesCMYVuAc`
     - **API Key**: `pit-da630dfd-7851-468f-b86e-0cbc9b8e4399`

4. **Data MERGE & Processing**:
   - Merge data from all three sources into a single item.

5. **Calculation (Code Node)**:
   - **Total Spend** = Google Spend + Meta Spend.
   - **Total Revenue** = Sum of GHL Opportunity Values (Status: Won).
   - **Total Leads** = Google Conversions + Meta Actions (Leads).
   - **ROAS** = Revenue / Spend.
   - **CPL** = Spend / Leads.
   - Format logic to handle division by zero.

6. **Output (Discord)**:
   - Send a formatted message to Channel `1423013870456274944`.
   - Format:

     ```
     **WEEKLY ROAS REPORT** (Dec X - Dec Y)

     **OVERALL**
     Total Ad Spend: $1,247.50
     Total Leads: 23
     Revenue: $52,019
     ROAS: 41.7x
     CPL: $54.24

     **BY PLATFORM**
     Google Ads | $847.50 | 15 leads | $56.50 CPL
     Meta Ads   | $400.00 | 8 leads  | $50.00 CPL
     ```

## Output Required

Please generate the full **JSON** for this n8n workflow so I can copy and paste it directly into n8n.
