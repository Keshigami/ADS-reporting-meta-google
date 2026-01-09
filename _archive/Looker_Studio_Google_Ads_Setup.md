# Looker Studio Setup for Google Ads
## With Call Tracking Integration

---

## Overview

Looker Studio (formerly Google Data Studio) is **free** and connects directly to Google Ads. It can display:
- All standard ad metrics (spend, clicks, conversions)
- **Phone call data** (if Google forwarding numbers enabled)
- Beautiful client-facing dashboards

---

## Step 1: Create Looker Studio Report

### Go to Looker Studio
```
lookerstudio.google.com
```

### Create New Report
1. Click **"+ Create"** → **"Report"**
2. Name it: `[Client Name] - Google Ads Report`

---

## Step 2: Connect Google Ads Data

### Add Data Source
1. Click **"Add data"**
2. Search for **"Google Ads"**
3. Click **Google Ads connector**
4. Authorize access to Google Ads
5. Select the **client's Google Ads account**
6. Click **"Add"**

---

## Step 3: Choose Metrics (Including Calls)

### Available Call Metrics

| Metric | Field Name | Description |
|--------|------------|-------------|
| Phone calls | `Phone calls` | Total calls from ads |
| Phone impressions | `Phone impressions` | Times phone # was shown |
| Phone through rate | `Phone through rate` | % who called after seeing |
| Cost per phone call | `Cost / phone call` | Spend ÷ calls |

### Standard Metrics to Add

| Metric | Description |
|--------|-------------|
| Cost | Total ad spend |
| Clicks | Link clicks |
| Impressions | Views |
| CTR | Click-through rate |
| Conversions | All conversion types |
| Cost / conversion | CPA |

---

## Step 4: Build the Dashboard

### Recommended Layout

```
┌─────────────────────────────────────────────────────────────┐
│  [CLIENT LOGO]    GOOGLE ADS REPORT    [Date Range]        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│   │  SPEND  │  │ CLICKS  │  │  CALLS  │  │   CPA   │       │
│   │ $1,250  │  │   892   │  │   47    │  │ $26.60  │       │
│   └─────────┘  └─────────┘  └─────────┘  └─────────┘       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   PERFORMANCE OVER TIME                                     │
│   ┌─────────────────────────────────────────────────────┐   │
│   │  📈 Line chart: Spend, Clicks, Calls by day        │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   CAMPAIGN BREAKDOWN                    CALL PERFORMANCE    │
│   ┌───────────────────────┐            ┌─────────────────┐  │
│   │ Campaign    Spend     │            │ Calls: 47       │  │
│   │ Brand       $450      │            │ Cost/Call: $8.50│  │
│   │ Services    $550      │            │ Avg Duration: 3m│  │
│   │ Retarget    $250      │            └─────────────────┘  │
│   └───────────────────────┘                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Step 5: Add Scorecards for Key Metrics

### Create Scorecard for Calls
1. Click **"Add a chart"** → **"Scorecard"**
2. Metric: **Phone calls**
3. Comparison: Previous period
4. Style: Large number with comparison arrow

### Create Scorecard for Cost Per Call
1. Add another Scorecard
2. Create calculated field:
   - Name: `Cost per Call`
   - Formula: `Cost / Phone calls`

---

## Step 6: Add Time Series Chart

1. Click **"Add a chart"** → **"Time series"**
2. Dimension: **Date**
3. Metrics:
   - Cost
   - Phone calls
   - Conversions
4. Date range: Last 30 days

---

## Step 7: Add Campaign Table

1. Click **"Add a chart"** → **"Table"**
2. Dimension: **Campaign**
3. Metrics:
   - Cost
   - Clicks
   - Phone calls
   - Cost per phone call
   - Conversions
4. Sort by: Cost (descending)

---

## Step 8: Add Filters

### Date Range Filter
1. Click **"Add a control"** → **"Date range control"**
2. Place at top of report
3. Default: Last 30 days

### Campaign Filter (Optional)
1. Click **"Add a control"** → **"Drop-down list"**
2. Dimension: Campaign
3. Allows: Select All or specific campaign

---

## Step 9: Style & Brand

### Add Client Logo
1. **Insert** → **Image**
2. Upload client logo

### Set Colors
1. **Theme and layout** → **Theme**
2. Set primary color to client brand color
3. Or use preset themes

### Add Title
1. **Insert** → **Text**
2. Add report title

---

## Step 10: Share with Client

### Option A: Share Link
```
File → Share → Get link → Viewer access
```
Send link to client

### Option B: Schedule Email
```
File → Email delivery schedule
```
- Set frequency: Weekly
- Set day: Monday
- Add recipients
- Attach as PDF or link

### Option C: Embed in Client Portal
```
File → Embed report → Copy iframe code
```
Paste into client's Notion or website

---

## Template Quick Start

Instead of building from scratch:

1. Go to: **lookerstudio.google.com/gallery**
2. Search: **"Google Ads"**
3. Find a template you like
4. Click **"Use template"**
5. Connect your client's Google Ads account
6. Customize as needed

---

## Metrics Reference

### Call Metrics Available in Looker Studio

| Metric Name | What It Shows |
|-------------|---------------|
| Phone calls | Number of calls from ads |
| Phone impressions | Times phone number was displayed |
| Phone through rate | Calls ÷ Phone impressions |
| All conv. value per phone call | Revenue per call |

### Creating Custom Call Metrics

**Cost per Call:**
```
Cost / Phone calls
```

**Call Rate (% of clicks that result in call):**
```
Phone calls / Clicks
```

---

## Troubleshooting

### "Phone calls" metric shows 0 or is missing

**Cause:** Google forwarding numbers not enabled

**Fix:**
1. Go to Google Ads → Assets → Call
2. Enable "Use a Google forwarding number"
3. Wait 24-48 hours for data to appear

### Data not updating

**Cause:** Looker Studio caches data

**Fix:**
1. Right-click on chart
2. Click "Refresh data"
3. Or: File → Report settings → Data freshness → Every hour

---

## Sample Report URL Structure

After creating, your report URL will look like:
```
https://lookerstudio.google.com/reporting/[REPORT-ID]/page/[PAGE-ID]
```

Share this with clients for view-only access.

---

*Last Updated: December 22, 2024*
