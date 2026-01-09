# GHL Workflow Setup - Populate Campaign Data

## Problem

Your campaign CSVs have blank columns because GHL isn't sending conversion data back to Google/Meta.

| Column | Status | Fix |
|--------|--------|-----|
| Leads | 0 | Create Lead workflow |
| Revenue | $0 | Create Purchase/Closed Won workflow |
| Sales | 0 | Same as Revenue |
| ROI % | 0% | Calculated from Revenue |
| CPL | $0 | Calculated from Leads |

---

## Workflow 1: Google Ads - Lead Conversion

**Purpose:** Populates the "Leads" column

### Step A: Create Conversion Action in GHL

1. **Marketing → Ad Manager → ⚙️ (gear icon)**
2. **Platform Settings → Google Ads → Conversions**
3. Click **+ Create a new conversion**
4. Settings:
   - **Name:** `Lead`
   - **Source:** Website
   - **Count:** One
   - **Value:** $0 (or your estimated lead value)
   - **Window:** 30 days
5. Click **Create**

### Step B: Create Workflow

1. **Automation → Workflows → + Create Workflow**
2. Name: `Google Ads - Track Lead`

**Trigger:**

- Type: **Contact Created**
- OR: **Form Submitted** (if you want specific forms only)

**Action:**

- Type: **Add to Google AdWords**
- Conversion: Select `Lead`
- Value: Leave at default or set fixed amount

1. Click **Publish**

---

## Workflow 2: Google Ads - Closed Won (Revenue)

**Purpose:** Populates the "Revenue" and "Sales" columns

### Step A: Create Conversion Action

1. Same path: **Marketing → Ad Manager → ⚙️ → Google Ads → Conversions**
2. Click **+ Create a new conversion**
3. Settings:
   - **Name:** `Closed Won`
   - **Source:** CRM
   - **Count:** Every
   - **Value:** Will be dynamic
   - **Window:** 90 days
4. Click **Create**

### Step B: Create Workflow

1. **Automation → Workflows → + Create Workflow**
2. Name: `Google Ads - Track Closed Won`

**Trigger:**

- Type: **Pipeline Stage Changed**
- Pipeline: (Select your sales pipeline)
- From Stage: Any
- To Stage: **Closed** (or your won stage name)

**Action:**

- Type: **Add to Google AdWords**
- Conversion: Select `Closed Won`
- Value: `{{opportunity.monetaryValue}}`
- Currency: `USD`

1. Click **Publish**

---

## Workflow 3: Meta Ads - Lead

**Purpose:** Sends lead events to Meta for "Leads" tracking

### Step A: Get Meta Credentials

1. Go to **Meta Events Manager** → Your Pixel
2. Copy **Pixel ID:** `1215094690084897`
3. **Settings → Generate Access Token** → Copy token

### Step B: Create Workflow

1. **Automation → Workflows → + Create Workflow**
2. Name: `Meta Ads - Track Lead`

**Trigger:**

- Type: **Contact Created**
- OR: **Form Submitted**

**Action:**

- Type: **Facebook Conversion API**
- Pixel ID: `1215094690084897`
- Access Token: (paste your token)
- Event: `Lead`
- Leave value empty for leads

1. Click **Publish**

---

## Workflow 4: Meta Ads - Purchase (Revenue)

**Purpose:** Sends revenue data to Meta for ROAS calculation

### Step B: Create Workflow

1. **Automation → Workflows → + Create Workflow**
2. Name: `Meta Ads - Track Purchase`

**Trigger:**

- Type: **Pipeline Stage Changed**
- Pipeline: (Select your sales pipeline)
- To Stage: **Closed**

**Action:**

- Type: **Facebook Conversion API**
- Pixel ID: `1215094690084897`
- Access Token: (paste your token)
- Event: `Purchase`
- Value: `{{opportunity.monetaryValue}}`
- Currency: `USD`

1. Click **Publish**

---

## Critical Requirement: Monetary Values

For Revenue/ROAS to work, every closed opportunity MUST have a monetary value set.

1. Go to **Opportunities**
2. Open any "Closed" stage opportunity
3. Set the **Monetary Value** field (e.g., $5,000)

**Without this, revenue will always be $0!**

---

## After Setup: Testing

1. Create a test lead (submit form on your funnel)
2. Create a test opportunity with $100 value → move to Closed
3. Check **Automation → Logs** to verify workflows fired
4. Wait 24-48 hours
5. Re-export CSVs - Leads/Revenue should now populate

---

## Summary Checklist

### Conversion Workflows (Populates CSV Columns)

| Workflow | Trigger | Action | Column Populated |
|----------|---------|--------|------------------|
| Google - Lead | Contact Created | Add to Google AdWords (Lead) | Leads, CPL |
| Google - Closed Won | Pipeline Stage → Closed | Add to Google AdWords (Closed Won) | Revenue, Sales, ROI |
| Meta - Lead | Contact Created | Facebook CAPI (Lead) | Leads, CPL |
| Meta - Purchase | Pipeline Stage → Closed | Facebook CAPI (Purchase) | Revenue, Sales, ROI |

### Phone Tracking (Separate Numbers by Channel)

| Channel | GHL Number | Purpose |
|---------|------------|---------|
| Meta Ads | TBD | Track calls from Facebook/Instagram ads |
| Google Ads | TBD | Track calls from Google Search/Display |
| LSA | TBD | Track calls from Local Service Ads |
| Organic | TBD | Track calls from website/GMB |

**Cost:** $6-8/month (3-4 numbers × $2/each)
