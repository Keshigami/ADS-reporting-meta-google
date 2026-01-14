# GHL ROAS + Attribution Complete Setup Guide

Full instructions for setting up proper ad attribution and ROAS tracking in GoHighLevel for both Google Ads and Meta Ads.

---

## Part 0: Capture Attribution Data on Contacts (CRITICAL FIRST STEP)

> **Without attribution data on contacts, ROAS cannot be calculated.** This must be set up before anything else.

### How Attribution Works

> **Deep Dive:** [Understanding Attribution Source](https://help.gohighlevel.com/support/solutions/articles/48001219997-understanding-attribution-source)

When someone clicks your ad:

1. **Google Ads** adds `?gclid=xxx` to the URL
2. **Meta Ads** adds `?fbclid=xxx` to the URL
3. **UTM parameters** track source/medium/campaign

GHL must capture these when the contact is created.

### Step 0.1: Lead Entry Points

Contacts enter GHL through:

| Entry Point | Attribution Capture | Setup Required |
|-------------|---------------------|----------------|
| GHL Forms on Funnels | ✅ Automatic | Ensure no redirects strip params |
| GHL Calendars | ✅ Automatic | Add tracking to calendar URLs |
| Facebook Lead Ads | ⚠️ Requires Mapping | Map fields in FB Lead Ad integration |
| Manual Entry | ❌ No attribution | Avoid for ad-sourced leads |
| Third-Party Forms | ⚠️ Requires Hidden Fields | Add hidden fields for gclid/fbclid |

### Step 0.2: Verify GHL Forms Capture Attribution

1. Go to your funnel/landing page
2. Add `?gclid=TEST123&fbclid=TESTFB456&utm_source=google&utm_medium=cpc&utm_campaign=test` to the URL
3. Submit the form
4. Go to **Contacts** → Find the new contact
5. Check these fields exist and have values:
   - `gclid` or `Google Click ID`
   - `fbclid` or `Facebook Click ID`
   - `utm_source`, `utm_medium`, `utm_campaign`

### Step 0.3: Fix Facebook Lead Ads Attribution

Facebook Lead Ads don't pass gclid/fbclid automatically. To fix:

1. **Settings → Integrations → Facebook**
2. Select your connected Page
3. Go to **Lead Ad Mapping**
4. Ensure these are mapped:
   - Facebook Lead ID
   - Ad ID
   - Campaign ID
   - Form ID
5. For full attribution, also enable **Lead Ad Attribution** in Facebook:
   - Create UTM parameters in your Facebook Ad setup
   - Map them to GHL custom fields

### Step 0.4: Prevent URL Parameter Stripping

Common issues that strip gclid/fbclid:

- **Redirects** between pages
- **Thank you page redirects** that don't preserve params
- **URL shorteners**

**Fix:** Keep users on the same domain, use GHL's built-in thank-you pages, and test the full funnel.

### Step 0.5: Verify Contact Has Attribution

Before proceeding, confirm at least ONE test contact has:

| Field | Present? |
|-------|----------|
| `gclid` OR `fbclid` | ✅ |
| `utm_source` | ✅ |
| `utm_campaign` | ✅ |
| `source` (GHL source field) | ✅ |

**If these are empty on contacts, STOP HERE and fix this first.**

---

## Part 1: Google Ads Attribution (GCLID)

### What is GCLID?

GCLID (Google Click ID) is a unique identifier added to your URLs when someone clicks a Google ad. GHL uses this to attribute conversions back to the correct ad/campaign.

### Step 1.1: Enable Auto-Tagging in Google Ads

1. Log into **Google Ads**
2. Go to **Admin → Account Settings**
3. Expand **Auto-tagging**
4. Check ✓ **Tag the URL that people click through from my ad**
5. **Save**

### Step 1.2: Ensure GHL Forms Capture GCLID

GHL forms automatically capture GCLID if the URL contains it. To verify:

1. Test by visiting your funnel with `?gclid=test123` appended
2. Submit a form
3. Check the contact record → look for GCLID in attribution fields

### Step 1.3: Create Google Ads Conversion in GHL

1. **Marketing → Ad Manager → ⚙️ Settings**
2. **Platform Settings → Google Ads → Conversions tab**
3. Click **+ Create a new conversion**
4. Configure:

| Field | Value |
|-------|-------|
| **Name** | `Closed Won` (use this exact name) |
| **Source** | Converted Lead |
| **Count** | Every |
| **Value** | Dynamic - will set in workflow |
| **Conversion Window** | 90 days |

1. Click **Create**

### Step 1.4: Create Google Ads Workflow

1. **Automation → Workflows → + Create Workflow**
2. Name: `Send Closed Deals to Google Ads`

**Trigger:**

- Type: **Pipeline Stage Changed**
- Pipeline: Your sales pipeline
- Stage: **Closed** (your closed/won stage name)

**Action:**

- Type: **Add to Google AdWords**
- Conversion: Select `Closed Won`
- Value: `{{opportunity.monetaryValue}}`
- Currency: `USD`

1. Click **Publish**

---

## Part 1.5: Enable Google Ad Reporting Dashboard

Start seeing live Google Ad reporting directly inside GHL.

### Step 1.5.1: Connect Google Account

1. Go to **Settings → Integrations**.
2. Connect your Google account (ensure it has admin/manager access to the Google Ads account).

### Step 1.5.2: Configure Ad Account

1. Go to **Reporting → Google Ads**.
2. If prompted, select the correct **MCC Account ID** and **Client Account ID**.
3. **Save**.

> **Note:** We have already configured the UTM Tracking Template in Google Ads (completed for MEC).

---

## Part 1.8: Google Analytics 4 (GA4) Setup

Setup GA4 to cross-verify traffic data.

### Step 1.8.1: Get Measurement ID

1. Go to **Google Analytics → Admin**.
2. Select **Data Streams** → Web.
3. Copy the **Measurement ID** (starts with `G-`).

### Step 1.8.2: Install in GHL

1. Go to **Sites → Settings**.
2. Paste the GA4 Script in the **Head Tracking Code** section:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXXXX');
</script>
```

*(Replace `G-XXXXXXXXXX` with your ID)*

---

## Part 2: Meta Ads Attribution (fbclid + CAPI)

### What is fbclid?

Similar to GCLID, fbclid is Meta's click identifier. Combined with CAPI (Conversions API), this allows server-side conversion tracking.

### Step 2.1: Get Your Meta Pixel Credentials

1. Go to **Meta Events Manager** (business.facebook.com/events_manager)
2. Select your Pixel/Dataset
3. Copy the **Pixel ID** (15-16 digit number)
4. Go to **Settings → Generate Access Token**
5. Copy the **Access Token**

### Step 2.2: Store Credentials in GHL (Recommended)

1. **Settings → Custom Values**
2. Create new values:
   - Name: `meta_pixel_id` | Value: `[your pixel ID]`
   - Name: `meta_access_token` | Value: `[your access token]`

### Step 2.3: Create Meta CAPI Workflow

1. **Automation → Workflows → + Create Workflow**
2. Name: `Send Closed Deals to Meta Ads`

**Trigger:**

- Type: **Pipeline Stage Changed**
- Pipeline: Your sales pipeline
- Stage: **Closed**

**Action:**

- Type: **Facebook Conversion API** (or Meta Conversion API)
- Configure:

| Field | Value |
|-------|-------|
| **Pixel ID** | `{{custom_values.meta_pixel_id}}` or paste directly |
| **Access Token** | `{{custom_values.meta_access_token}}` or paste directly |
| **Event Name** | `Purchase` |
| **Event Value** | `{{opportunity.monetaryValue}}` |
| **Currency** | `USD` |

1. Click **Publish**

---

### Step 2.4: Install Browser Pixel Code (Required for Funnel Events)

While CAPI (Step 2.3) handles "Closed" deals, you need the Browser Pixel to track "PageViews" and "Leads" on the frontend.

1. **Meta Events Manager → Data Sources → Settings**.
2. Click **Set up Meta Pixel**.
3. Choose **Install code manually**.
4. Copy the Base Code.
5. In GHL: **Sites → Settings**.
6. Paste into **Head Tracking Code**.
7. **Save**.

## Part 1.9: Google Ad Precautionary Tracking Script (Fail-Safe)

*(Source: [How to set up Google Ad Precautionary Tracking Script](https://help.gohighlevel.com/support/solutions/articles/48001219356))*

This script ensures clicks are tracked even if the UTM template fails or is stripped.

1. **Google Ads > Tools & Settings > Bulk Actions > Scripts**.
2. Create a new script, name it "GHL Fail-Safe Tracking".
3. Paste the code below (Requires `lpurl` variable setup):
    - *See full code in the source article or Appendix A.*

---

## Part 1.10: Offline Conversion Actions (The "Secret Weapon")

*(Source: [How to set up Google Ad Conversion Actions](https://help.gohighlevel.com/support/solutions/articles/48001220947))*

This sends "Offline" signals (like specific Form Submits or Chat Widget leads) back to Google Ads as conversions.

1. **Google Ads**: Create "Import > Other data sources > Track conversions from clicks".
2. **Category**: "Converted Lead".
3. **GHL Workflow**:
    - **Trigger**: Form Submitted / Chat Widget Replied.
    - **Action**: "Add to Google Ads".
    - **Conversion Action**: Select the one you just created.

---

## Part 3: Agency & Advanced Reporting

### 3.1 Client Spend (Agency Only)

*(Source: [How to add Client Spend](https://help.gohighlevel.com/support/solutions/articles/48001220946))*
- **Purpose**: Show the client their Total Cost (Ad Spend + Your Management Fee).
- **Where**: Agency View > Reporting Settings.

### 3.2 Chat Widget Attribution

*(Source: [Chat Widget Attribution](https://help.gohighlevel.com/support/solutions/articles/48001175057))*
- **View**: Contact Detail > Activity Tab.
- **Note**: Chat leads often come from "Direct" or "Organic" unless they clicked an ad immediately before chatting.

---

## Part 2.5: Enable Facebook Ad Reporting Dashboard

Start seeing live Facebook Ad reporting directly inside GHL.

### Step 2.5.1: Connect Facebook Account

1. Go to **Settings → Integrations**.
2. Connect your Facebook account (ensure it has admin access to the Page and Ad Account).

### Step 2.5.2: Configure Ad Account

1. Go to **Reporting → Facebook Ads**.
2. Select the correct **Ad Account ID** from the dropdown.
3. **Save**.

> **Note:** The Pixel & CAPI setup (Part 2) feeds data into this dashboard to verify conversions.

---

## Part 3: Ensure Opportunities Have Revenue Values

> **CRITICAL**: ROAS = Revenue / Spend. Without revenue values, ROAS cannot be calculated.

### Required: Set Monetary Value on Every Deal

When moving an opportunity to "Closed":

1. Open the opportunity
2. Set **Monetary Value** to the actual deal amount (e.g., $5,000)
3. Then move to Closed stage

### Optional: Require Value Before Close (Workflow)

Create a workflow that prevents closing without a value:

1. Trigger: Pipeline Stage Changed → Closed
2. Condition: If `opportunity.monetaryValue` is empty
3. Action: Send internal alert OR move back to previous stage

---

## Part 4: Verification Checklist

### Google Ads

- [ ] Auto-tagging enabled in Google Ads account
- [ ] "Closed Won" conversion created in GHL Ad Manager
- [ ] Workflow published with "Add to Google AdWords" action
- [ ] Test: Create opportunity with $100 value → move to Closed → check workflow logs

### Meta Ads

- [ ] Pixel ID and Access Token obtained
- [ ] Workflow published with "Facebook Conversion API" action
- [ ] Test: Same as above, then check Meta Events Manager → Test Events tab

### Data Verification (Wait 24-48 hours after test)

- [ ] Google Ads → Tools → Conversions → shows your conversion
- [ ] Meta Events Manager → shows Purchase events with values
- [ ] GHL Ad Manager → Statistics → ROAS column populated

---

## Part 5: Channel-Separated Phone Tracking

For accurate call attribution, use separate GHL phone numbers for each channel:

| Channel | GHL Number | Use In |
|---------|------------|--------|
| Meta Ads | Number 1 (TBD) | All Facebook/Instagram ads |
| Google Ads | Number 2 (TBD) | All Google Search/Display ads |
| Local Service Ads | Number 3 (TBD) | Google LSA |
| Organic/Website | Number 4 (TBD) | Website, GMB, directories |

### Setup Steps

1. **Settings → Phone Numbers → Buy Number** (repeat 4x)
2. Name each clearly: `Meta Tracking`, `Google Tracking`, `LSA Tracking`, `Organic Tracking`
3. Configure forwarding to business main line
4. Update all ads/pages with respective numbers

**Cost:** $6-8/month (3-4 numbers × $2/each)

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| ROAS shows 0 or blank | No monetary value on opportunities | Add $ value to all closed deals |
| Google conversion not appearing | Conversion name mismatch | Name must match exactly (case-sensitive) |
| Meta events not tracking | Invalid access token | Regenerate token in Events Manager |
| Attribution not working | GCLID/fbclid stripped | Check for redirects stripping URL params |
| Calls not attributed | Using single number | Set up channel-separated numbers |

---

## Quick Reference: What Fires What

| Trigger | Meta Ads | Google Ads | LSA |
|---------|----------|-----------|-----|
| Lead submits form | CAPI Lead event | Add to AdWords | N/A (calls only) |
| Phone call | GHL logs (Meta #) | GHL logs (Google #) | GHL logs (LSA #) |
| **Deal closed (ROAS)** | CAPI Purchase event | Add to AdWords | Manual attribution |

For ROAS, the **closed deal** is what matters - that's where revenue comes from.
