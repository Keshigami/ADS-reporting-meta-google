# Complete GHL Attribution & Tracking Setup Guide

## Overview

This guide covers end-to-end attribution tracking in GoHighLevel to ensure every lead, call, and closed deal is properly attributed to its source (Meta Ads, Google Ads, LSA, Organic).

---

## Part 1: Understanding GHL Attribution

### How Attribution Works in GHL

GHL tracks attribution based on the **first session** when a visitor lands on a tracked page/funnel. It automatically records:

- Landing URL
- UTM parameters (utm_source, utm_medium, utm_campaign, utm_content, utm_term)
- Device and browser info
- Date/time of visit
- GCLID (Google Click ID)
- FBCLID (Facebook Click ID)

### Where Attribution Data Lives

| Location | What You See |
|----------|--------------|
| Contact Records | Source, UTMs, GCLID/FBCLID |
| Reporting → Attribution | Aggregated by campaign/source |
| Opportunities | Revenue attributed to source |
| Ad Manager → Statistics | ROAS, CPL by campaign |

---

## Part 2: UTM Parameter Setup

### Step 2.1: Create Attribution Custom Fields

1. **Settings → Custom Fields → + Add Custom Field**
2. Create folder named `Attribution`
3. Add these **Single Line** fields:
   - `utm_source`
   - `utm_medium`
   - `utm_campaign`
   - `utm_content`
   - `utm_term`
   - `gclid`
   - `fbclid`

### Step 2.2: Add Hidden Fields to Forms

1. **Sites → Forms → Select your form**
2. Go to **Custom Fields** tab
3. Drag each Attribution field into the form
4. Set each field to **Hidden**
5. GHL auto-populates from URL parameters

### Step 2.3: UTM Naming Conventions

Use consistent naming across all platforms:

| Parameter | Google Ads | Meta Ads | LSA |
|-----------|------------|----------|-----|
| utm_source | google | facebook | google_lsa |
| utm_medium | cpc | paid_social | lsa |
| utm_campaign | {campaign_name} | {campaign_name} | local_services |

**No special characters or emojis in UTM values!**

---

## Part 3: Google Ads Attribution (GCLID)

### Step 3.1: Enable Auto-Tagging

1. Log into **Google Ads**
2. **Settings → Account Settings**
3. Enable **Auto-Tagging**
4. This adds `?gclid=xxx` to all ad clicks

### Step 3.2: Create GCLID Custom Field

Already done in Step 2.1, but verify:

- Field name: `gclid`
- Type: Single Line
- Hidden on forms

### Step 3.3: Create Conversion Actions in GHL Ad Manager

1. **Marketing → Ad Manager → ⚙️ Settings**
2. **Platform Settings → Google Ads → Conversions**
3. Click **+ Create a new conversion**

Create these conversions:

| Name | Source | Count | Value | Window |
|------|--------|-------|-------|--------|
| Lead | Website | One | $0 | 30 days |
| Qualified Lead | Converted Lead | One | $100 | 60 days |
| Closed Won | Purchase | Every | Dynamic | 90 days |

1. These sync to Google Ads automatically via API

### Step 3.4: Create Google Ads Workflow

**Workflow: Send Leads to Google Ads**

1. **Automation → Workflows → + Create**
2. Name: `Google Ads - Track Lead`

**Trigger:**

- Type: Form Submitted
- Form: (Select your lead form)

**Action:**

- Type: Add to Google AdWords
- Conversion: Lead

1. **Publish**

---

**Workflow: Send Closed Deals to Google Ads**

1. **Automation → Workflows → + Create**
2. Name: `Google Ads - Track Closed Won`

**Trigger:**

- Type: Pipeline Stage Changed
- Pipeline: (Your sales pipeline)
- To Stage: Closed/Won

**Action:**

- Type: Add to Google AdWords
- Conversion: Closed Won
- Value: `{{opportunity.monetaryValue}}`
- Currency: USD

1. **Publish**

---

## Part 4: Meta Ads Attribution (FBCLID + CAPI)

### Step 4.1: Get Meta Credentials

1. Go to **Meta Business Manager → Events Manager**
2. Select your Pixel/Dataset
3. Copy **Pixel ID**: `1215094690084897`
4. **Settings → Generate Access Token** → Copy token

### Step 4.2: Store Credentials in GHL

1. **Settings → Custom Values**
2. Create new values:

| Name | Value |
|------|-------|
| `meta_pixel_id` | 1215094690084897 |
| `meta_access_token` | (your access token) |

### Step 4.3: Add Pixel to Funnels (Optional - for PageView)

1. **Sites → Funnels → Select funnel**
2. **Settings → Head Tracking Code**
3. Paste Meta Pixel code

### Step 4.4: Create Meta CAPI Workflows

**Workflow: Send Leads to Meta**

1. **Automation → Workflows → + Create**
2. Name: `Meta Ads - Track Lead`

**Trigger:**

- Type: Form Submitted

**Action:**

- Type: Facebook Conversion API
- Pixel ID: `{{custom_values.meta_pixel_id}}`
- Access Token: `{{custom_values.meta_access_token}}`
- Event: Lead

1. **Publish**

---

**Workflow: Send Purchases to Meta**

1. **Automation → Workflows → + Create**
2. Name: `Meta Ads - Track Purchase`

**Trigger:**

- Type: Pipeline Stage Changed
- To Stage: Closed/Won

**Action:**

- Type: Facebook Conversion API
- Pixel ID: `{{custom_values.meta_pixel_id}}`
- Access Token: `{{custom_values.meta_access_token}}`
- Event: Purchase
- Value: `{{opportunity.monetaryValue}}`
- Currency: USD

1. **Publish**

---

## Part 5: Opportunity Monetary Value

> **CRITICAL**: Without monetary values, ROAS = 0

### Step 5.1: Create Monetary Custom Field (Optional)

If you need dynamic pricing from forms:

1. **Settings → Custom Fields → + Add**
2. Object: Opportunity
3. Type: Monetary
4. Name: `Deal Value`

### Step 5.2: Ensure Value Is Set

Train team or automate:

- Every opportunity moved to Closed MUST have `monetaryValue` set
- Use workflow to block stage change if value is $0

**Workflow: Block Zero-Value Closes**

1. Trigger: Pipeline Stage Changed → Closed
2. Condition: If `opportunity.monetaryValue` equals 0
3. Action: Move back to previous stage + send internal alert

---

## Part 6: Phone Call Attribution

For accurate call tracking by channel, use separate GHL numbers.

| Channel | GHL Number Name | Used In |
|---------|-----------------|---------|
| Meta Ads | `MEC-META` | All Meta ad creatives |
| Google Ads | `MEC-GOOGLE` | Google Search/Display ads |
| LSA | `MEC-LSA` | Local Service Ads |
| Organic | `MEC-ORGANIC` | Website, GMB, directories |

### Setup Steps

1. **Settings → Phone Numbers → Buy Number** (×4)
2. Name each clearly
3. Configure forwarding to main business line
4. Update all ads with respective numbers

**Cost:** $8/month (4 × $2)

---

## Part 7: Verification Checklist

### Integration Checks

- [ ] **Settings → Integrations → Google** shows Connected (green)
- [ ] **Settings → Integrations → Facebook** shows Connected (green)
- [ ] Google Ads auto-tagging enabled
- [ ] Meta Pixel installed on funnels

### Custom Fields Checks

- [ ] Attribution folder exists in Custom Fields
- [ ] `gclid`, `fbclid`, `utm_source`, `utm_medium`, `utm_campaign` fields created
- [ ] Hidden fields added to all lead capture forms

### Workflow Checks

- [ ] `Google Ads - Track Lead` workflow published
- [ ] `Google Ads - Track Closed Won` workflow published
- [ ] `Meta Ads - Track Lead` workflow published
- [ ] `Meta Ads - Track Purchase` workflow published

### Test Submission

1. Visit funnel with test params:

   ```
   ?gclid=TEST123&fbclid=TESTFB456&utm_source=test&utm_campaign=attribution_test
   ```

2. Submit form
3. Check contact record for:
   - [ ] `gclid` = TEST123
   - [ ] `fbclid` = TESTFB456
   - [ ] `utm_source` = test
   - [ ] `utm_campaign` = attribution_test

### Data Flow Test

1. Create test opportunity with $100 value
2. Move to Closed stage
3. Check **Automation → Logs** - workflows should show execution
4. Wait 24-48 hours
5. Check Google Ads → Conversions
6. Check Meta Events Manager → Test Events

---

## Part 8: Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| ROAS = 0 | No monetaryValue on opportunities | Set $ value before closing deals |
| No leads in Google Ads | Workflow not triggering | Check workflow trigger conditions |
| Meta events not tracking | Invalid access token | Regenerate in Events Manager |
| Attribution empty on contacts | URL params stripped | Check for redirects, test full funnel |
| GCLID not captured | Form missing hidden field | Add gclid as hidden field |
| Wrong campaign attribution | UTM naming inconsistent | Standardize UTM conventions |

---

## Quick Reference: Complete Data Flow

```
User clicks ad
    ↓
URL has gclid/fbclid + UTMs
    ↓
User submits GHL form
    ↓
Hidden fields capture parameters
    ↓
Contact created with attribution
    ↓
"Form Submitted" workflow fires
    ↓
Lead sent to Google Ads + Meta (CAPI)
    ↓
Lead becomes opportunity
    ↓
Opportunity moved to Closed (with $value)
    ↓
"Pipeline Stage Changed" workflow fires
    ↓
Closed Won sent to Google Ads + Meta (with value)
    ↓
ROAS calculated in Ad Manager
```

---

*Last Updated: January 8, 2026*
