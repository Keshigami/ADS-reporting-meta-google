# Weekly Ads Reporting System Specification

> **Comprehensive design for automated weekly paid ads reporting using n8n, Zapier, GHL, Notion, and LaTeX→PDF generation.**

---

## Table of Contents

1. [High-Level Architecture](#1-high-level-architecture)
2. [Detailed n8n Workflow](#2-detailed-n8n-workflow)
3. [Zapier Bridge Design](#3-zapier-bridge-design)
4. [LaTeX Template Specification](#4-latex-template-specification)
5. [Notion Database Design](#5-notion-database-design)
6. [GoHighLevel Configuration Plan](#6-gohighlevel-configuration-plan)

---

## 1. High-Level Architecture

### 1.1 System Overview Diagram (Text)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           WEEKLY ADS REPORTING SYSTEM                       │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────┐    ┌──────────────┐
│  Meta Ads    │    │  Google Ads  │
│    API       │    │    API       │
└──────┬───────┘    └──────┬───────┘
       │                   │
       └─────────┬─────────┘
                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              n8n (Self-Hosted)                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  WEEKLY CRON TRIGGER (Monday 9AM) or WEBHOOK (On-Demand)            │    │
│  └──────────────────────────────┬──────────────────────────────────────┘    │
│                                 ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  1. Fetch Active Clients from GHL/Notion                            │    │
│  │  2. Loop: For Each Client                                           │    │
│  │     ├─ Fetch Meta Ads Data (7 days + prior 7 days)                  │    │
│  │     ├─ Fetch Google Ads Data (7 days + prior 7 days)                │    │
│  │     ├─ Normalize & Merge Metrics                                    │    │
│  │     ├─ Compute Aggregates & WoW Deltas                              │    │
│  │     ├─ Identify Top/Bottom Campaigns (by ROAS/CPA)                  │    │
│  │     ├─ Detect Anomalies (spend/conversion spikes/drops)             │    │
│  │     ├─ Generate Optimization Suggestions (AI Node)                  │    │
│  │     ├─ Build LaTeX Document String                                  │    │
│  │     ├─ Call LaTeX→PDF API                                           │    │
│  │     ├─ Upload PDF to Google Drive                                   │    │
│  │     ├─ Update Notion "Ads Reports" Database                         │    │
│  │     ├─ Update GHL Contact Custom Fields                             │    │
│  │     └─ Send Email (Executive Summary + PDF)                         │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                 │                                           │
│  ┌──────────────────────────────┴──────────────────────────────────────┐    │
│  │  ERROR HANDLING: Slack/Discord Alert + Notion "Reporting Issues"   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  EXTERNAL SERVICES                                                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ LaTeX→PDF  │  │ Google Drive│  │   Notion    │  │   GoHighLevel       │  │
│  │ API        │  │ (Storage)   │  │ (Database)  │  │   (CRM)             │  │
│  │            │  │             │  │             │  │                     │  │
│  │ latex.ytotech│ │ Via n8n    │  │ Ads Reports │  │ • weekly_ads_json   │  │
│  │ .com or    │  │ Google Drive│  │ Database    │  │ • weekly_ads_roas   │  │
│  │ latexonline │ │ Node        │  │             │  │ • weekly_ads_spend  │  │
│  │ .cc        │  │             │  │             │  │ • weekly_report_url │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│  ZAPIER BRIDGE (Optional - GHL → n8n On-Demand Trigger)                      │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │  GHL Webhook/Button → Zapier → POST to n8n Webhook                     │ │
│  │  (Only used if GHL OAuth/webhook is simpler via Zapier)                │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Data Flow Summary

| Step | Source | Destination | Data |
|------|--------|-------------|------|
| 1 | Meta Ads API | n8n | Impressions, clicks, spend, conversions, CTR, CPC, CPA, ROAS |
| 2 | Google Ads API | n8n | Impressions, clicks, spend, conversions, CTR, CPC, CPA, ROAS |
| 3 | n8n (Code Node) | n8n | Normalized metrics, WoW deltas, anomalies, optimization suggestions |
| 4 | n8n | LaTeX→PDF API | LaTeX document string |
| 5 | LaTeX→PDF API | n8n | PDF binary |
| 6 | n8n | Google Drive | PDF file |
| 7 | Google Drive | n8n | Shareable PDF URL |
| 8 | n8n | Notion API | Report entry with metrics + PDF URL |
| 9 | n8n | GHL API | Custom fields update (JSON, ROAS, spend, PDF URL) |
| 10 | n8n | Email (SMTP/Gmail) | Executive summary HTML + PDF attachment |

### 1.3 Client Matching Strategy

Each client must have consistent identifiers across all systems:

| System | Client Identifier Field | Example |
|--------|------------------------|---------|
| GHL | `contact_id` or custom field `client_code` | `MEC001` |
| Notion | `Client Code` property in Clients database | `MEC001` |
| Meta Ads | Ad Account Name or custom naming convention | `MEC001 - MEC Builds` |
| Google Ads | Customer ID label or account name | `MEC001 - MEC Builds` |

---

## 2. Detailed n8n Workflow

### 2.1 Workflow Overview

**Workflow Name:** `Weekly Ads Report Generator`  
**Trigger:** Cron (Monday 9:00 AM) + Webhook (on-demand)  
**Execution:** Loop over all active clients

---

### 2.2 Node-by-Node Specification

#### Node 1: Cron Trigger
```
Name: Weekly Trigger
Type: Cron
Settings:
  - Mode: Every Week
  - Day: Monday
  - Hour: 9
  - Minute: 0
  - Timezone: America/Los_Angeles
Output: Trigger signal to start workflow
```

#### Node 2: Webhook Trigger (On-Demand)
```
Name: On-Demand Trigger
Type: Webhook
Settings:
  - HTTP Method: POST
  - Path: /weekly-ads-report
  - Authentication: Header Auth (X-Secret-Key)
Input Fields (expected from Zapier/GHL):
  - client_code: string (optional - if blank, run for all)
  - ghl_contact_id: string (optional)
Output: { client_code, ghl_contact_id, trigger_source: "webhook" }
```

#### Node 3: Merge Triggers
```
Name: Merge Triggers
Type: Merge
Settings:
  - Mode: Merge by position
  - Multiplex: true
Purpose: Combine cron and webhook triggers into single flow
```

#### Node 4: Fetch Active Clients
```
Name: Get Active Clients
Type: Notion - Query Database
Settings:
  - Database: Clients
  - Filter: { "property": "Status", "select": { "equals": "Active" } }
Output Fields:
  - client_code
  - client_name
  - ghl_contact_id
  - meta_ad_account_id
  - google_ads_customer_id
  - stakeholder_emails (array)
  - internal_team_emails (array)
```

#### Node 5: Loop Over Clients
```
Name: Loop Clients
Type: Split In Batches
Settings:
  - Batch Size: 1
Purpose: Process one client at a time for stability
```

#### Node 6: Set Date Range Variables
```
Name: Set Dates
Type: Set
Output Fields:
  - current_week_start: {{ $now.minus({ days: 7 }).startOf('day').toISO() }}
  - current_week_end: {{ $now.minus({ days: 1 }).endOf('day').toISO() }}
  - prior_week_start: {{ $now.minus({ days: 14 }).startOf('day').toISO() }}
  - prior_week_end: {{ $now.minus({ days: 8 }).endOf('day').toISO() }}
  - week_label: {{ $now.minus({ days: 7 }).toFormat('MMM d') }} - {{ $now.minus({ days: 1 }).toFormat('MMM d, yyyy') }}
```

#### Node 7: Fetch Meta Ads Data (Current Week)
```
Name: Meta Ads - Current Week
Type: HTTP Request
Settings:
  - URL: https://graph.facebook.com/v18.0/act_{{$json.meta_ad_account_id}}/insights
  - Method: GET
  - Authentication: OAuth2 (Meta Business)
  - Query Parameters:
    - level: campaign
    - fields: campaign_id,campaign_name,impressions,clicks,spend,actions,action_values,ctr,cpc,cost_per_action_type
    - time_range: { "since": "{{current_week_start}}", "until": "{{current_week_end}}" }
    - time_increment: 1
Output Fields (per campaign):
  - campaign_id
  - campaign_name
  - impressions
  - clicks
  - spend
  - conversions (extracted from actions)
  - revenue (extracted from action_values)
  - ctr
  - cpc
  - cpa (cost_per_action_type)
```

#### Node 8: Fetch Meta Ads Data (Prior Week)
```
Name: Meta Ads - Prior Week
Type: HTTP Request
(Same as Node 7, but with prior_week dates)
```

#### Node 9: Fetch Google Ads Data (Current Week)
```
Name: Google Ads - Current Week
Type: HTTP Request
Settings:
  - URL: https://googleads.googleapis.com/v14/customers/{{$json.google_ads_customer_id}}/googleAds:searchStream
  - Method: POST
  - Authentication: OAuth2 (Google Ads)
  - Body (GAQL):
    SELECT
      campaign.id,
      campaign.name,
      metrics.impressions,
      metrics.clicks,
      metrics.cost_micros,
      metrics.conversions,
      metrics.conversions_value,
      metrics.ctr,
      metrics.average_cpc,
      metrics.cost_per_conversion
    FROM campaign
    WHERE segments.date BETWEEN '{{current_week_start}}' AND '{{current_week_end}}'
Output Fields: Same structure as Meta (normalized in next node)
```

#### Node 10: Fetch Google Ads Data (Prior Week)
```
Name: Google Ads - Prior Week
Type: HTTP Request
(Same as Node 9, but with prior_week dates)
```

#### Node 11: Normalize & Merge Metrics
```
Name: Normalize Metrics
Type: Code (JavaScript)
Purpose: Standardize field names, convert units, merge platforms
Code:
```
```javascript
const metaCurrent = $input.all()[0].json.meta_current;
const metaPrior = $input.all()[0].json.meta_prior;
const googleCurrent = $input.all()[0].json.google_current;
const googlePrior = $input.all()[0].json.google_prior;

// Normalize Meta data
function normalizeMeta(data, platform = 'meta') {
  return data.map(c => ({
    platform,
    campaign_id: c.campaign_id,
    campaign_name: c.campaign_name,
    impressions: parseInt(c.impressions) || 0,
    clicks: parseInt(c.clicks) || 0,
    spend: parseFloat(c.spend) || 0,
    conversions: c.actions?.find(a => a.action_type === 'lead')?.value || 0,
    revenue: c.action_values?.find(a => a.action_type === 'purchase')?.value || 0,
    ctr: parseFloat(c.ctr) || 0,
    cpc: parseFloat(c.cpc) || 0,
    cpa: parseFloat(c.cost_per_action_type?.find(a => a.action_type === 'lead')?.value) || 0
  }));
}

// Normalize Google data
function normalizeGoogle(data, platform = 'google') {
  return data.map(c => ({
    platform,
    campaign_id: c.campaign.id,
    campaign_name: c.campaign.name,
    impressions: parseInt(c.metrics.impressions) || 0,
    clicks: parseInt(c.metrics.clicks) || 0,
    spend: (parseInt(c.metrics.costMicros) || 0) / 1000000,
    conversions: parseFloat(c.metrics.conversions) || 0,
    revenue: parseFloat(c.metrics.conversionsValue) || 0,
    ctr: parseFloat(c.metrics.ctr) || 0,
    cpc: (parseInt(c.metrics.averageCpc) || 0) / 1000000,
    cpa: (parseInt(c.metrics.costPerConversion) || 0) / 1000000
  }));
}

const currentWeek = [
  ...normalizeMeta(metaCurrent),
  ...normalizeGoogle(googleCurrent)
];

const priorWeek = [
  ...normalizeMeta(metaPrior),
  ...normalizeGoogle(googlePrior)
];

return [{ json: { currentWeek, priorWeek } }];
```
```
Output: { currentWeek: [...], priorWeek: [...] }
```

#### Node 12: Compute Aggregates & Deltas
```
Name: Compute Aggregates
Type: Code (JavaScript)
Purpose: Calculate totals, WoW changes, identify top/bottom campaigns
Code:
```
```javascript
const { currentWeek, priorWeek } = $input.first().json;

// Aggregate totals
function aggregate(campaigns) {
  return campaigns.reduce((acc, c) => ({
    total_spend: acc.total_spend + c.spend,
    total_conversions: acc.total_conversions + c.conversions,
    total_revenue: acc.total_revenue + c.revenue,
    total_clicks: acc.total_clicks + c.clicks,
    total_impressions: acc.total_impressions + c.impressions
  }), { total_spend: 0, total_conversions: 0, total_revenue: 0, total_clicks: 0, total_impressions: 0 });
}

const currentTotals = aggregate(currentWeek);
const priorTotals = aggregate(priorWeek);

// Calculate derived metrics
currentTotals.roas = currentTotals.total_spend > 0 
  ? (currentTotals.total_revenue / currentTotals.total_spend).toFixed(2) 
  : 0;
currentTotals.cpa = currentTotals.total_conversions > 0 
  ? (currentTotals.total_spend / currentTotals.total_conversions).toFixed(2) 
  : 0;
currentTotals.ctr = currentTotals.total_impressions > 0 
  ? ((currentTotals.total_clicks / currentTotals.total_impressions) * 100).toFixed(2) 
  : 0;
currentTotals.cpc = currentTotals.total_clicks > 0 
  ? (currentTotals.total_spend / currentTotals.total_clicks).toFixed(2) 
  : 0;

priorTotals.roas = priorTotals.total_spend > 0 
  ? (priorTotals.total_revenue / priorTotals.total_spend).toFixed(2) 
  : 0;
priorTotals.cpa = priorTotals.total_conversions > 0 
  ? (priorTotals.total_spend / priorTotals.total_conversions).toFixed(2) 
  : 0;

// Calculate WoW deltas
const deltas = {
  spend_delta: ((currentTotals.total_spend - priorTotals.total_spend) / (priorTotals.total_spend || 1) * 100).toFixed(1),
  conversions_delta: ((currentTotals.total_conversions - priorTotals.total_conversions) / (priorTotals.total_conversions || 1) * 100).toFixed(1),
  roas_delta: ((currentTotals.roas - priorTotals.roas) / (priorTotals.roas || 1) * 100).toFixed(1),
  cpa_delta: ((currentTotals.cpa - priorTotals.cpa) / (priorTotals.cpa || 1) * 100).toFixed(1)
};

// Add trend arrows
deltas.spend_arrow = parseFloat(deltas.spend_delta) > 0 ? '↑' : '↓';
deltas.conversions_arrow = parseFloat(deltas.conversions_delta) > 0 ? '↑' : '↓';
deltas.roas_arrow = parseFloat(deltas.roas_delta) > 0 ? '↑' : '↓';
deltas.cpa_arrow = parseFloat(deltas.cpa_delta) < 0 ? '↑' : '↓'; // Lower CPA is better

// Rank campaigns by ROAS
const rankedByROAS = [...currentWeek]
  .map(c => ({
    ...c,
    roas: c.spend > 0 ? (c.revenue / c.spend).toFixed(2) : 0,
    cpa: c.conversions > 0 ? (c.spend / c.conversions).toFixed(2) : 999999
  }))
  .sort((a, b) => b.roas - a.roas);

const top3Campaigns = rankedByROAS.slice(0, 3);
const bottom3Campaigns = rankedByROAS.slice(-3).reverse();

// Channel breakdown
const metaCampaigns = currentWeek.filter(c => c.platform === 'meta');
const googleCampaigns = currentWeek.filter(c => c.platform === 'google');

const metaTotals = aggregate(metaCampaigns);
const googleTotals = aggregate(googleCampaigns);

return [{
  json: {
    currentTotals,
    priorTotals,
    deltas,
    top3Campaigns,
    bottom3Campaigns,
    metaTotals,
    googleTotals,
    allCampaigns: rankedByROAS
  }
}];
```
```
Output: Aggregated metrics with deltas, rankings, and channel breakdowns
```

#### Node 13: Detect Anomalies
```
Name: Detect Anomalies
Type: Code (JavaScript)
Purpose: Flag unusual patterns that need attention
Code:
```
```javascript
const { currentTotals, priorTotals, deltas } = $input.first().json;

const anomalies = [];

// Spend spike with flat/declining conversions
if (parseFloat(deltas.spend_delta) > 30 && parseFloat(deltas.conversions_delta) < 5) {
  anomalies.push({
    type: 'SPEND_SPIKE_NO_CONVERSIONS',
    severity: 'HIGH',
    message: `Spend increased ${deltas.spend_delta}% but conversions only changed ${deltas.conversions_delta}%`,
    action: 'Review campaign targeting and exclude underperforming audiences'
  });
}

// Conversion drop with normal spend
if (parseFloat(deltas.conversions_delta) < -30 && Math.abs(parseFloat(deltas.spend_delta)) < 15) {
  anomalies.push({
    type: 'CONVERSION_DROP',
    severity: 'CRITICAL',
    message: `Conversions dropped ${Math.abs(deltas.conversions_delta)}% with stable spend`,
    action: 'Check pixel/tracking, review landing page, verify conversion events'
  });
}

// Zero conversions with significant spend
if (currentTotals.total_conversions === 0 && currentTotals.total_spend > 100) {
  anomalies.push({
    type: 'TRACKING_FAILURE',
    severity: 'CRITICAL',
    message: `$${currentTotals.total_spend} spent with ZERO conversions recorded`,
    action: 'URGENT: Verify pixel/conversion tracking is firing correctly'
  });
}

// ROAS crash
if (parseFloat(deltas.roas_delta) < -40) {
  anomalies.push({
    type: 'ROAS_CRASH',
    severity: 'HIGH',
    message: `ROAS dropped ${Math.abs(deltas.roas_delta)}% week-over-week`,
    action: 'Pause low-performing campaigns, reallocate budget to top performers'
  });
}

// CPA spike
if (parseFloat(deltas.cpa_delta) > 50) {
  anomalies.push({
    type: 'CPA_SPIKE',
    severity: 'MEDIUM',
    message: `CPA increased ${deltas.cpa_delta}% - leads are getting more expensive`,
    action: 'Review audience targeting, test new creatives, check competition'
  });
}

return [{ json: { ...$input.first().json, anomalies } }];
```
```
Output: Previous data + anomalies array
```

#### Node 14: Generate Optimization Suggestions (AI)
```
Name: Generate Action Items
Type: OpenAI / Claude (AI Node)
Settings:
  - Model: GPT-4 or Claude 3
  - System Prompt: "You are a paid ads optimization expert. Based on the weekly metrics provided, generate 5-8 specific, actionable optimization recommendations. Categorize each into: BUDGET, BIDDING, CREATIVE, or TRACKING. Be specific about which campaigns to adjust and by how much."
  - User Prompt:
    Client: {{$json.client_name}}
    
    Current Week Totals:
    - Spend: ${{$json.currentTotals.total_spend}}
    - Conversions: {{$json.currentTotals.total_conversions}}
    - ROAS: {{$json.currentTotals.roas}}x
    - CPA: ${{$json.currentTotals.cpa}}
    
    Week-over-Week Changes:
    - Spend: {{$json.deltas.spend_delta}}%
    - Conversions: {{$json.deltas.conversions_delta}}%
    - ROAS: {{$json.deltas.roas_delta}}%
    - CPA: {{$json.deltas.cpa_delta}}%
    
    Top 3 Campaigns (by ROAS):
    {{$json.top3Campaigns}}
    
    Bottom 3 Campaigns (by ROAS):
    {{$json.bottom3Campaigns}}
    
    Anomalies Detected:
    {{$json.anomalies}}
    
    Generate optimization recommendations in JSON format:
    {
      "budget_actions": [...],
      "bidding_actions": [...],
      "creative_actions": [...],
      "tracking_actions": [...]
    }

Output: { recommendations: { budget_actions, bidding_actions, creative_actions, tracking_actions } }
```

#### Node 15: Build LaTeX Document
```
Name: Build LaTeX
Type: Code (JavaScript)
Purpose: Construct complete LaTeX document string with all data
(See Section 4 for full LaTeX template)
Output: { latex_document: "\\documentclass{article}..." }
```

#### Node 16: Call LaTeX→PDF API
```
Name: Generate PDF
Type: HTTP Request
Settings:
  - URL: https://latex.ytotech.com/builds/sync
  - Method: POST
  - Content-Type: application/json
  - Body:
    {
      "compiler": "pdflatex",
      "resources": [
        {
          "main": true,
          "content": "{{$json.latex_document}}"
        }
      ]
    }
  - Response Format: Binary
Output: PDF binary data
```

#### Node 17: Upload to Google Drive
```
Name: Upload PDF
Type: Google Drive - Upload File
Settings:
  - File Name: {{client_code}}_Weekly_Report_{{week_label}}.pdf
  - Parent Folder: [Ads Reports Folder ID]
  - Binary Data: {{$binary.data}}
  - Share: Anyone with link can view
Output: { file_id, webViewLink, webContentLink }
```

#### Node 18: Update Notion Database
```
Name: Create Notion Entry
Type: Notion - Create Database Item
Settings:
  - Database: Ads Reports
  - Properties:
    - Client: (Relation to {{client_code}})
    - Week: {{week_label}}
    - Spend: {{currentTotals.total_spend}}
    - Conversions: {{currentTotals.total_conversions}}
    - ROAS: {{currentTotals.roas}}
    - CPA: {{currentTotals.cpa}}
    - WoW ROAS Change: {{deltas.roas_delta}}
    - WoW CPA Change: {{deltas.cpa_delta}}
    - Report PDF: {{webViewLink}}
    - Summary: "{{anomalies[0]?.message || 'Performance stable'}}"
    - Has Anomalies: {{anomalies.length > 0}}
    - Status: "Delivered"
```

#### Node 19: Update GHL Contact
```
Name: Update GHL
Type: HTTP Request
Settings:
  - URL: https://rest.gohighlevel.com/v1/contacts/{{ghl_contact_id}}
  - Method: PUT
  - Headers:
    - Authorization: Bearer {{$credentials.ghl_api_key}}
  - Body:
    {
      "customField": {
        "weekly_ads_json": "{{JSON.stringify({
          week: week_label,
          spend: currentTotals.total_spend,
          conversions: currentTotals.total_conversions,
          roas: currentTotals.roas,
          cpa: currentTotals.cpa,
          top_campaigns: top3Campaigns.map(c => c.campaign_name),
          anomalies: anomalies.map(a => a.message),
          action_items: recommendations
        })}}",
        "weekly_ads_roas": {{currentTotals.roas}},
        "weekly_ads_spend": {{currentTotals.total_spend}},
        "weekly_report_pdf_url": "{{webViewLink}}"
      }
    }
```

#### Node 20: Send Email Report
```
Name: Send Email
Type: Gmail / SMTP
Settings:
  - To: {{stakeholder_emails.join(', ')}}
  - CC: {{internal_team_emails.join(', ')}}
  - Subject: Weekly Ads Report: {{client_name}} | {{week_label}}
  - HTML Body:
    <h1>Weekly Performance Summary</h1>
    <h2>{{client_name}} | {{week_label}}</h2>
    
    <h3>Key Metrics</h3>
    <table>
      <tr><td>Spend</td><td>${{currentTotals.total_spend}} ({{deltas.spend_arrow}} {{deltas.spend_delta}}%)</td></tr>
      <tr><td>Conversions</td><td>{{currentTotals.total_conversions}} ({{deltas.conversions_arrow}} {{deltas.conversions_delta}}%)</td></tr>
      <tr><td>ROAS</td><td>{{currentTotals.roas}}x ({{deltas.roas_arrow}} {{deltas.roas_delta}}%)</td></tr>
      <tr><td>CPA</td><td>${{currentTotals.cpa}} ({{deltas.cpa_arrow}} {{deltas.cpa_delta}}%)</td></tr>
    </table>
    
    <h3>Top Performing Campaigns</h3>
    <ol>
      {{#each top3Campaigns}}
      <li>{{campaign_name}} - ROAS: {{roas}}x</li>
      {{/each}}
    </ol>
    
    <h3>Priority Actions This Week</h3>
    <ul>
      {{#each recommendations.budget_actions}}
      <li>💰 {{this}}</li>
      {{/each}}
      {{#each recommendations.creative_actions}}
      <li>🎨 {{this}}</li>
      {{/each}}
    </ul>
    
    <p><a href="{{webViewLink}}">📄 View Full PDF Report</a></p>
  - Attachments: [PDF binary if preferred over link]
```

#### Node 21: Error Handler
```
Name: Error Handler
Type: Error Trigger
Connected To: All nodes
Actions:
  1. Slack Notification:
     - Channel: #ads-reporting-errors
     - Message: "❌ Weekly report failed for {{client_name}}: {{$error.message}}"
  
  2. Notion Log Entry:
     - Database: Reporting Issues
     - Properties:
       - Client: {{client_code}}
       - Date: {{$now}}
       - Error: {{$error.message}}
       - Node: {{$error.node}}
       - Status: "Unresolved"
```

---

## 3. Zapier Bridge Design

### 3.1 When to Use Zapier

Use Zapier as a bridge **only** when:
- GHL webhook configuration is simpler through Zapier's native GHL integration
- You need a "Generate Report Now" button in GHL that triggers on-demand reports

### 3.2 Zapier Zap Specification

```
Zap Name: GHL → n8n Report Trigger

TRIGGER:
  App: GoHighLevel
  Event: Webhook (Custom)
  OR
  Event: Pipeline Stage Changed (if you want automatic trigger)
  Filter: Stage = "Generate Weekly Report" (custom stage)
  
  Output Fields:
    - contact_id
    - contact_email
    - contact_name
    - custom_field.client_code

ACTION:
  App: Webhooks by Zapier
  Event: POST
  URL: https://your-n8n-instance.com/webhook/weekly-ads-report
  Headers:
    - X-Secret-Key: {{your_secret_key}}
    - Content-Type: application/json
  Body (JSON):
    {
      "client_code": "{{contact.custom_field.client_code}}",
      "ghl_contact_id": "{{contact.id}}",
      "trigger_source": "ghl_manual",
      "requested_by": "{{contact.email}}"
    }
```

### 3.3 Security Recommendations

| Security Measure | Implementation |
|-----------------|----------------|
| Secret Key | Include `X-Secret-Key` header; validate in n8n webhook |
| IP Allowlisting | Allowlist Zapier's IP ranges in n8n or firewall |
| HTTPS Only | Ensure n8n webhook endpoint uses HTTPS |
| Rate Limiting | Limit to 10 requests per hour per client in n8n |

---

## 4. LaTeX Template Specification

### 4.1 Parameterized Template

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{array}
\usepackage{tikz}
\usepackage{fancyhdr}
\usepackage{hyperref}

% Brand Colors
\definecolor{primary}{HTML}{2563EB}
\definecolor{success}{HTML}{16A34A}
\definecolor{warning}{HTML}{EA580C}
\definecolor{danger}{HTML}{DC2626}

% Page Setup
\geometry{margin=1in}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\textcolor{primary}{\textbf{{{CLIENT_NAME}}}}}
\fancyhead[R]{Weekly Ads Report | {{WEEK_RANGE}}}
\fancyfoot[C]{\thepage}

\begin{document}

% ============================================
% EXECUTIVE SUMMARY (Page 1)
% ============================================
\section*{Executive Summary}

\begin{center}
\Large\textbf{{{CLIENT_NAME}} Weekly Performance}\\
\large {{WEEK_RANGE}}
\end{center}

\vspace{1em}

\subsection*{Overall Performance vs Goals}
{{GOAL_SUMMARY}}
% Example: "Achieved 127 leads at $42 CPL, exceeding target of 100 leads."

\vspace{1em}

\subsection*{Key Insights}
\begin{itemize}
{{KEY_INSIGHTS}}
% Example items:
% \item \textcolor{success}{$\uparrow$} ROAS improved 23\% due to new creative testing
% \item \textcolor{warning}{$\downarrow$} Google Search CPA increased 18\% - requires bid adjustment
% \item \textcolor{primary}{$\bullet$} New landing page launched mid-week
\end{itemize}

\vspace{1em}

\subsection*{Priority Actions for Next 7 Days}
\begin{enumerate}
{{ACTION_ITEMS_BRIEF}}
% Example:
% \item Increase budget on Meta Retargeting by 20\%
% \item Lower bids on Google Brand campaign by 15\%
% \item Pause underperforming creative "Summer Sale v2"
\end{enumerate}

\newpage

% ============================================
% CORE PERFORMANCE KPIS
% ============================================
\section*{Core Performance Metrics}

\begin{center}
\begin{tabular}{lccc}
\toprule
\textbf{Metric} & \textbf{This Week} & \textbf{Last Week} & \textbf{Change} \\
\midrule
Spend & {{SPEND_CURRENT}} & {{SPEND_PRIOR}} & {{SPEND_DELTA}} \\
Revenue & {{REVENUE_CURRENT}} & {{REVENUE_PRIOR}} & {{REVENUE_DELTA}} \\
Conversions & {{CONVERSIONS_CURRENT}} & {{CONVERSIONS_PRIOR}} & {{CONVERSIONS_DELTA}} \\
ROAS & {{ROAS_CURRENT}} & {{ROAS_PRIOR}} & {{ROAS_DELTA}} \\
CPA/CPL & {{CPA_CURRENT}} & {{CPA_PRIOR}} & {{CPA_DELTA}} \\
CTR & {{CTR_CURRENT}} & {{CTR_PRIOR}} & {{CTR_DELTA}} \\
CPC & {{CPC_CURRENT}} & {{CPC_PRIOR}} & {{CPC_DELTA}} \\
\bottomrule
\end{tabular}
\end{center}

\subsection*{Trend (Last 4 Weeks)}
{{TREND_CHART}}
% Can be a simple ASCII representation or embedded image if LaTeX API supports

\newpage

% ============================================
% CHANNEL BREAKDOWN
% ============================================
\section*{Channel Performance}

\subsection*{Meta Ads}
\begin{center}
\begin{tabular}{lcccc}
\toprule
\textbf{Campaign} & \textbf{Spend} & \textbf{Conversions} & \textbf{CPA} & \textbf{ROAS} \\
\midrule
{{META_CAMPAIGN_ROWS}}
\midrule
\textbf{Total} & {{META_TOTAL_SPEND}} & {{META_TOTAL_CONVERSIONS}} & {{META_AVG_CPA}} & {{META_AVG_ROAS}} \\
\bottomrule
\end{tabular}
\end{center}

\subsection*{Google Ads}
\begin{center}
\begin{tabular}{lcccc}
\toprule
\textbf{Campaign} & \textbf{Spend} & \textbf{Conversions} & \textbf{CPA} & \textbf{ROAS} \\
\midrule
{{GOOGLE_CAMPAIGN_ROWS}}
\midrule
\textbf{Total} & {{GOOGLE_TOTAL_SPEND}} & {{GOOGLE_TOTAL_CONVERSIONS}} & {{GOOGLE_AVG_CPA}} & {{GOOGLE_AVG_ROAS}} \\
\bottomrule
\end{tabular}
\end{center}

\subsection*{Top \& Bottom Performers}

\textbf{Top 3 Campaigns (by ROAS):}
\begin{enumerate}
{{TOP_CAMPAIGNS}}
\end{enumerate}

\textbf{Bottom 3 Campaigns (by ROAS):}
\begin{enumerate}
{{BOTTOM_CAMPAIGNS}}
\end{enumerate}

\newpage

% ============================================
% ANOMALIES & ISSUES
% ============================================
\section*{Anomalies \& Issues Detected}

{{#if ANOMALIES}}
\begin{itemize}
{{ANOMALIES}}
% Example:
% \item \textcolor{danger}{\textbf{CRITICAL:}} Zero conversions recorded with \$1,200 spend - check pixel
% \item \textcolor{warning}{\textbf{HIGH:}} Spend increased 45\% with only 3\% conversion increase
\end{itemize}
{{else}}
\textcolor{success}{No significant anomalies detected this week.}
{{/if}}

\newpage

% ============================================
% RECOMMENDED ACTIONS
% ============================================
\section*{Recommended Actions for Next 7 Days}

\subsection*{Budget Adjustments}
\begin{itemize}
{{BUDGET_ACTIONS}}
\end{itemize}

\subsection*{Bidding \& Targeting}
\begin{itemize}
{{BIDDING_ACTIONS}}
\end{itemize}

\subsection*{Creative \& Offer}
\begin{itemize}
{{CREATIVE_ACTIONS}}
\end{itemize}

\subsection*{Technical / Tracking}
\begin{itemize}
{{TRACKING_ACTIONS}}
\end{itemize}

\vspace{2em}
\hrule
\vspace{1em}
\begin{center}
\textit{Report generated automatically on {{GENERATION_DATE}}}\\
\small Questions? Contact your account manager.
\end{center}

\end{document}
```

### 4.2 Placeholder Mapping (n8n → LaTeX)

| Placeholder | n8n Data Source | Example Value |
|-------------|----------------|---------------|
| `{{CLIENT_NAME}}` | `$json.client_name` | "MEC Builds LLC" |
| `{{WEEK_RANGE}}` | `$json.week_label` | "Dec 9 - Dec 15, 2024" |
| `{{SPEND_CURRENT}}` | `${{currentTotals.total_spend.toFixed(2)}}` | "$4,250.00" |
| `{{ROAS_CURRENT}}` | `${currentTotals.roas}x` | "3.42x" |
| `{{SPEND_DELTA}}` | `${deltas.spend_delta}% ${deltas.spend_arrow}` | "+12.5% ↑" |
| `{{META_CAMPAIGN_ROWS}}` | Loop generating LaTeX table rows | "Brand Awareness & \$500 & 12 & \$41.67 & 2.8x \\\\" |
| `{{ACTION_ITEMS_BRIEF}}` | `recommendations.budget_actions.slice(0,3)` | "\\item Increase Meta retargeting by 20\\%" |

---

## 5. Notion Database Design

### 5.1 "Ads Reports" Database Schema

| Property Name | Type | Description |
|--------------|------|-------------|
| Name | Title | Auto-generated: `{Client} - Week of {Date}` |
| Client | Relation | Links to Clients database |
| Week Start | Date | Start of reporting week |
| Week End | Date | End of reporting week |
| Spend | Number (Currency) | Total ad spend for the week |
| Conversions | Number | Total conversions |
| Revenue | Number (Currency) | Total revenue attributed |
| ROAS | Number | Return on ad spend |
| CPA | Number (Currency) | Cost per acquisition |
| CTR | Number (Percent) | Click-through rate |
| WoW ROAS Change | Number (Percent) | Week-over-week ROAS delta |
| WoW CPA Change | Number (Percent) | Week-over-week CPA delta |
| WoW Conversions Change | Number (Percent) | Week-over-week conversions delta |
| Report PDF | URL | Google Drive link to PDF |
| Has Anomalies | Checkbox | True if anomalies detected |
| Anomaly Summary | Text | Brief description of issues |
| Top Campaign | Text | Best performing campaign name |
| Status | Select | "Generating", "Delivered", "Reviewed" |
| Action Items | Text (Multi-line) | Key actions for next week |
| Notes | Text (Multi-line) | Internal notes |

### 5.2 Saved Views for Team Decisions

#### View 1: "Accounts with Declining ROAS (Last 3 Weeks)"
```
Filter:
  - WoW ROAS Change < 0 (current week)
  - [Rollup from last 3 entries] Average ROAS Change < -10%
Sort: WoW ROAS Change (ascending)
Columns: Client, ROAS, WoW ROAS Change (3 week avg), Spend, Anomaly Summary
```

#### View 2: "Accounts with CPA Worsening >20% WoW"
```
Filter:
  - WoW CPA Change > 20
Sort: WoW CPA Change (descending)
Columns: Client, CPA, WoW CPA Change, Conversions, Top Campaign, Action Items
```

#### View 3: "Reports with Open Action Items"
```
Filter:
  - Action Items is not empty
  - Status != "Reviewed"
Sort: Week Start (descending)
Columns: Client, Week Start, ROAS, CPA, Action Items, Status
```

#### View 4: "Critical Anomalies This Week"
```
Filter:
  - Has Anomalies = true
  - Week Start = This Week
Sort: Spend (descending)
Columns: Client, Spend, Conversions, Anomaly Summary, Report PDF
```

#### View 5: "Weekly Dashboard (Current Week)"
```
Filter:
  - Week Start = This Week
Sort: Client (A-Z)
Columns: Client, Spend, Conversions, ROAS, CPA, WoW ROAS Change, Status
Gallery Card Preview: Show ROAS prominently with trend arrow
```

---

## 6. GoHighLevel Configuration Plan

### 6.1 Custom Fields Setup

Create in **Settings → Custom Fields → Contacts**:

| Field Name | Field ID | Type | Description |
|------------|----------|------|-------------|
| Weekly Ads JSON | `weekly_ads_json` | Long Text | JSON blob with all weekly metrics |
| Weekly Ads ROAS | `weekly_ads_roas` | Number | Latest week ROAS for quick view |
| Weekly Ads Spend | `weekly_ads_spend` | Number | Latest week spend |
| Weekly Report URL | `weekly_report_pdf_url` | Text | URL to latest PDF report |
| Report History | `report_history_urls` | Long Text | JSON array of last 4 report URLs |
| Action Items Summary | `weekly_action_items` | Long Text | Current week's priority actions |
| Last Report Date | `last_report_date` | Date | When last report was generated |

### 6.2 GHL Dashboard Configuration

Create a **Custom Dashboard Widget** (if using GHL Agency features):

**"Weekly Ads Snapshot" Widget:**
- Display: Latest ROAS, Spend, Conversions for each active client
- Color coding: Green if ROAS > 3x, Yellow if 2-3x, Red if < 2x
- Click-through: Opens contact with full custom field data

### 6.3 Pipeline Stage for On-Demand Reports

Create a **"Request Report" Pipeline** or stage:

| Stage Name | Purpose | Trigger |
|-----------|---------|---------|
| Request Weekly Report | Manual trigger point | Moving contact here triggers Zapier |

When contact enters this stage:
1. Zapier webhook fires
2. n8n generates report
3. n8n moves contact back to original stage (or "Report Delivered")

### 6.4 Automated GHL Workflow Tasks

Create **GHL Workflow** triggered by n8n custom field update:

```
Trigger: Contact Field Changed → weekly_ads_json updated

Condition 1: If {{contact.weekly_ads_json}} contains "CRITICAL"
Action: Create Task
  - Title: "URGENT: Review {{contact.name}} ads - critical issue detected"
  - Assigned To: Account Manager
  - Due: Today
  - Priority: High

Condition 2: If {{contact.weekly_ads_roas}} < 2
Action: Create Task
  - Title: "Low ROAS Alert: {{contact.name}} at {{contact.weekly_ads_roas}}x"
  - Assigned To: Ads Specialist
  - Due: Tomorrow

Condition 3: If {{contact.weekly_action_items}} contains "budget"
Action: Create Task
  - Title: "Budget Action Required: {{contact.name}}"
  - Description: {{contact.weekly_action_items}}
  - Assigned To: Media Buyer
  - Due: Within 2 days
```

### 6.5 GHL Notes Template

Update contact notes automatically with structured weekly summary:

```
=== WEEKLY ADS REPORT: {{week_range}} ===

📊 PERFORMANCE SNAPSHOT
• Spend: ${{spend}} ({{spend_delta}})
• ROAS: {{roas}}x ({{roas_delta}})
• Conversions: {{conversions}} ({{conversions_delta}})
• CPA: ${{cpa}} ({{cpa_delta}})

🏆 TOP CAMPAIGN: {{top_campaign}}
⚠️ WATCH: {{bottom_campaign}}

📋 ACTION ITEMS:
{{action_items_list}}

📄 Full Report: {{pdf_url}}
=====================================
```

### 6.6 Report History Access

Store last 4 report URLs in `report_history_urls` field as JSON array:

```json
[
  {"week": "Dec 9-15", "url": "https://drive.google.com/..."},
  {"week": "Dec 2-8", "url": "https://drive.google.com/..."},
  {"week": "Nov 25-Dec 1", "url": "https://drive.google.com/..."},
  {"week": "Nov 18-24", "url": "https://drive.google.com/..."}
]
```

n8n logic to maintain this:
```javascript
// In n8n before updating GHL
const currentHistory = JSON.parse(contact.report_history_urls || '[]');
currentHistory.unshift({ week: week_label, url: pdf_url });
const updatedHistory = currentHistory.slice(0, 4); // Keep only last 4
```

---

## Appendix A: Error Handling Strategy

| Error Type | Detection | Response |
|-----------|-----------|----------|
| API Rate Limit | HTTP 429 response | Retry with exponential backoff (wait 60s, 120s, 240s) |
| Auth Failure | HTTP 401/403 | Alert Slack, log to Notion, skip client |
| No Data Returned | Empty API response | Log warning, generate report with "No data available" note |
| LaTeX Compilation Error | API error response | Fallback to simple text PDF or skip PDF generation |
| GHL Update Failure | HTTP 4xx/5xx | Retry once, then log error and continue with email |
| Notion Update Failure | API error | Log to backup sheet, alert team |

---

## Appendix B: Metric Definitions

| Metric | Formula | Notes |
|--------|---------|-------|
| ROAS | Revenue ÷ Spend | Target: >3x for most businesses |
| CPA/CPL | Spend ÷ Conversions | Lower is better |
| CTR | (Clicks ÷ Impressions) × 100 | Benchmark: 1-2% for display, 3-5% for search |
| CPC | Spend ÷ Clicks | Varies by industry |
| Conversion Rate | (Conversions ÷ Clicks) × 100 | Landing page quality indicator |
| WoW Delta | ((Current - Prior) ÷ Prior) × 100 | Percentage change week-over-week |

---

## Appendix C: Implementation Checklist

### Phase 1: Infrastructure Setup
- [ ] Configure Meta Business API access and credentials
- [ ] Configure Google Ads API access and credentials
- [ ] Set up LaTeX→PDF API account (latex.ytotech.com or alternative)
- [ ] Create Google Drive folder for report storage
- [ ] Configure n8n credentials for all services
- [ ] Create Notion "Ads Reports" database with schema above
- [ ] Create GHL custom fields

### Phase 2: n8n Workflow Development
- [ ] Build and test Meta Ads data fetch nodes
- [ ] Build and test Google Ads data fetch nodes
- [ ] Implement normalization Code node
- [ ] Implement aggregation and delta calculation
- [ ] Implement anomaly detection logic
- [ ] Configure AI node for optimization suggestions
- [ ] Build LaTeX template generation
- [ ] Test PDF generation end-to-end
- [ ] Implement Google Drive upload
- [ ] Implement Notion database update
- [ ] Implement GHL API update
- [ ] Implement email sending
- [ ] Add error handling and Slack notifications

### Phase 3: Zapier Bridge (if used)
- [ ] Create GHL → Zapier trigger
- [ ] Configure Zapier → n8n webhook action
- [ ] Test on-demand report generation
- [ ] Document security measures

### Phase 4: Testing & Validation
- [ ] Test with one client (full cycle)
- [ ] Validate PDF formatting and accuracy
- [ ] Validate Notion database entries
- [ ] Validate GHL custom field updates
- [ ] Validate email delivery and formatting
- [ ] Test error handling scenarios
- [ ] Run full workflow for all clients

### Phase 5: Documentation & Training
- [ ] Document workflow for team
- [ ] Train account managers on GHL dashboards
- [ ] Train team on Notion views for decision-making
- [ ] Create runbook for troubleshooting

---

*Document Version: 1.0*  
*Last Updated: December 22, 2024*  
*Author: Automated System Design*
