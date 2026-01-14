# GHL Ultimate Tracking & Attribution Guide

**The Single Source of Truth for Advertising Data, Attribution, and ROAS.**

This guide consolidates all tracking protocols into one workflow. Follow these steps to ensure every dollar spent in Google and Meta is accurately tracked to a Lead and Sale in HighLevel.

---

## ⚡ Quick Start Checklist

Use this to verify setup is complete. Each phase listed below.

| Phase | Task | Status |
| :--- | :--- | :---: |
| 0 | Prerequisites gathered | [ ] |
| 1 | Understand First/Latest Attribution | [ ] |
| 1.5 | Custom fields created in GHL | [ ] |
| 2 | Google Ads connected + tracking template installed | [ ] |
| 3 | Facebook connected + UTM parameters set | [ ] |
| 3.5 | Funnel tracking code installed (Pixel + gtag) | [ ] |
| 4 | Dashboard verified | [ ] |
| 5 | 4 ROAS Workflows created (Lead + Closed Won) | [ ] |
| 5.5 | Number Pool created + script installed | [ ] |
| 5.6 | External site tracking (if WordPress/Wix) | [ ] |
| 5.7 | Trigger links created for key campaigns | [ ] |
| 5.8 | Email domain + tracking configured | [ ] |
| 6 | Full verification test completed | [ ] |

> **For Existing Clients:** Skip to [Appendix B: Sub-Account Audit Checklist](#-appendix-b-sub-account-audit-checklist)

---

## 🔐 Phase 0: Prerequisites

Before starting, gather these credentials and access:

### 0.1 Access Requirements

- [ ] **GHL Sub-Account Admin Access** — Settings > Integrations page accessible
- [ ] **Google Ads Admin Access** — Account Settings and Tracking visible
- [ ] **Meta Business Manager Access** — Events Manager accessible
- [ ] **Meta Pixel ID** — Found in Events Manager > Data Sources
- [ ] **Google Ads Conversion ID** — Format: `AW-XXXXXXXXXX`
- [ ] **Google Ads Conversion Labels** — One per conversion action (Lead, Purchase)

### 0.2 Recommended: Have Ready

- [ ] Client's primary phone number (for call tracking setup)
- [ ] Landing page URLs you'll be tracking
- [ ] Pipeline stage names (especially "Closed Won" stage name)

---

## 📑 Phase 1: The Foundation (Attribution Logic)

Before connecting ads, you must understand *how* HighLevel tracks people.

### 1.1 First vs. Latest Attribution

Every contact has two attribution records.

- **First Attribution:** The verified *first* interaction. Never changes.
- **Latest Attribution:** The *most recent* interaction. Updates constantly.

![First and Latest Attribution](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155015178854/original/LaAFs5bfFxyo0Su56GWkBEkyyD7o2l6oQA.png?1702496706)

### 1.2 Where to Find It

Go to **Contacts > Select Contact > Scroll to Activity (Bottom Right)**.

![Locating Attribution Data](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48247964170/original/VSgXZHb-pBWW3cGC7emsU4xKKLFyaKQJ3g.gif?1661800754)

---

## �️ Phase 1.5: Create Custom Fields in GHL

Before forms can capture UTM data, you must create custom contact fields.

### 1.5.1 Create Attribution Fields

1. Go to **Settings > Custom Fields > Contact**
2. Click **+ Add Field** for each of the following:

| Field Name | Field Type | Internal Name |
| :--- | :--- | :--- |
| UTM Source | Single Line Text | `utm_source` |
| UTM Medium | Single Line Text | `utm_medium` |
| UTM Campaign | Single Line Text | `utm_campaign` |
| UTM Content | Single Line Text | `utm_content` |
| UTM Term | Single Line Text | `utm_term` |
| Google Click ID | Single Line Text | `gclid` |
| Facebook Click ID | Single Line Text | `fbclid` |

- [ ] All 7 custom fields created

> **Why This Matters:** Forms can only save data to fields that exist. Without these, UTM parameters are lost.

---

## �🎯 Phase 2: Google Ads Setup

### 2.1 Connect the Account

- [ ] Go to **Settings > Integrations**
- [ ] Connect your Google Account (Must have Admin access)
- [ ] Go to **Reporting > Google Ads Settings**
- [ ] Select your **MCC Account** (if applicable) and **Client Account**

![Google Ads Integration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48241724794/original/41FtCevRGsKvW2aJupKjPEfYRnjb_h9fcA.png?1659031996)

### 2.2 Install the Tracking Template (CRITICAL)

For Google Ads to "talk" to GHL, you must use this specific UTM template.

**Copy This Code:**

```
{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignname}&utm_content={adgroupname}&utm_term={keyword}&campaign_id={campaignid}&ad_group_id={adgroupid}&ad_id={creative}
```

- [ ] Go to **Google Ads > Settings > Account Settings > Tracking**
- [ ] Paste into "Tracking template" field
- [ ] Click Save

### 2.3 Enable Auto-Tagging

- [ ] Go to **Google Ads > Settings > Account Settings > Auto-tagging**
- [ ] Ensure "Tag the URL that people click through from my ad" is **ON**

> **Why Auto-Tagging:** Automatically appends `gclid` to URLs, enabling Enhanced Conversions.

### 2.4 The "Fail-Safe" Script (Optional)

Sometimes UTMs get stripped. Add this script for extra reliability.

- [ ] Go to **Google Ads > Tools > Bulk Actions > Scripts**
- [ ] Create a script named "GHL Fail-Safe"
- [ ] *(See Appendix A for full code)*

---

## 📘 Phase 3: Facebook Ads Setup

### 3.1 Connect & Enable

- [ ] Go to **Settings > Integrations > Connect Facebook**
- [ ] Go to **Reporting > Facebook Ads Settings**
- [ ] Select the correct Ad Account

![Facebook Integration Settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261752780/original/KL8jbKqo5KzHh_3uSbiTvx0kcQ6nTuYmrQ.png?1667831557)

### 3.2 UTM Parameters (The "Blue" Source)

Facebook tracking requires specific parameters to be identified as "Paid Social".

**Copy This Code:**

```
utm_source=facebook&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&campaign_id={{campaign.id}}
```

- [ ] Go to **Ads Manager > Ad Level > Tracking > URL Parameters**
- [ ] Paste the UTM string above
- [ ] Apply to all active ads

![Facebook UTM Builder](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48173301734/original/RKnA2Zuqw5UV4fyM_U3CSt4L6gkkNmCJHw.png?1640200443)

---

## 🔧 Phase 3.5: Funnel Tracking Code

This is the actual code that must be placed on your funnel pages to capture tracking data.

### 3.5.1 Meta (Facebook) Pixel

Add this to the `<head>` of every funnel page:

```html
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=YOUR_PIXEL_ID&ev=PageView&noscript=1"/></noscript>
```

**Fire These Events:**

| Page | Event Code |
| :--- | :--- |
| Form Submit / Thank You | `fbq('track', 'Lead');` |
| Purchase Complete | `fbq('track', 'Purchase', {value: X, currency: 'USD'});` |

---

### 3.5.2 Google Ads (gtag.js)

Add this to the `<head>` of every funnel page:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-XXXXXXXXXX');
</script>
```

**Fire These Events:**

```javascript
// On form submission (Lead)
gtag('event', 'conversion', {'send_to': 'AW-XXXXXXXXXX/CONVERSION_LABEL'});

// On purchase (with value)
gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXXX/CONVERSION_LABEL',
    'value': 100.00,
    'currency': 'USD'
});
```

---

### 3.5.3 UTM Parameter Capture (Hidden Form Fields)

Add these hidden fields to your forms to capture attribution data into GHL:

```html
<input type="hidden" name="utm_source" id="utm_source">
<input type="hidden" name="utm_medium" id="utm_medium">
<input type="hidden" name="utm_campaign" id="utm_campaign">
<input type="hidden" name="utm_content" id="utm_content">
<input type="hidden" name="utm_term" id="utm_term">
<input type="hidden" name="gclid" id="gclid">
<input type="hidden" name="fbclid" id="fbclid">
```

Add this script to auto-populate from URL:

```javascript
// Auto-populate hidden fields from URL params
const urlParams = new URLSearchParams(window.location.search);
['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid', 'fbclid'].forEach(param => {
    const field = document.getElementById(param);
    if (field && urlParams.get(param)) {
        field.value = urlParams.get(param);
    }
});
```

---

### 3.5.4 Quick Reference: What Goes Where

| Page Type | Meta Pixel | Google gtag | Conversion Event |
| :--- | :--- | :--- | :--- |
| Landing Page | ✅ PageView | ✅ Config | None |
| Thank You / Confirmation | ✅ PageView | ✅ Config | Lead (both) |
| Purchase Complete | ✅ PageView | ✅ Config | Purchase (both, with value) |

---

## 📊 Phase 4: Reporting & Optimization

Once connected, your data feeds into the Reporting Dashboard.

### 4.1 The Dashboard

Located at **Reporting > Google Ads**. This is your "Command Center".

![Google Ads Dashboard](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48249248484/original/BVS_7NnRNEQp3b4qJgSWEcs3kymdNOhDkw.png?1662394187)

### 4.2 Interpreting the Data

| Metric | Definition | Action |
| :--- | :--- | :--- |
| **Impressions/Clicks** | Top of funnel volume. | Low? Check bids/creative. |
| **Cost (Spend)** | Pulled from Google API. | High? Check efficiency. |
| **Leads** | Pulled from GHL Forms. | Low? Check Landing Page. |
| **Revenue** | Opportunities marked "Won". | Low? Check Sales Team. |
| **ROAS** | Revenue / Cost. | **The North Star Metric.** |

---

## 🛠 Phase 5: Workflows & Server-Side Tracking

This phase connects GHL events to ad platforms for ROAS calculation.

### 5.1 Required Conversion Workflows

Create these 4 workflows to send conversion data back to Google and Meta:

| # | Workflow Name | Trigger | Action | Populates |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Google Ads - Track Lead | Contact Created | Add to Google AdWords (Lead) | Leads, CPL |
| 2 | Google Ads - Track Closed Won | Pipeline → Closed | Add to Google AdWords (Closed Won) | Revenue, ROAS |
| 3 | Meta Ads - Track Lead | Contact Created | Facebook CAPI (Lead) | Leads |
| 4 | Meta Ads - Track Purchase | Pipeline → Closed | Facebook CAPI (Purchase) | Revenue, ROAS |

- [ ] Workflow 1 created and published
- [ ] Workflow 2 created and published
- [ ] Workflow 3 created and published
- [ ] Workflow 4 created and published

> **Detailed Steps:** See [GHL_Workflow_Setup_Steps.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_Workflow_Setup_Steps.md) for full step-by-step instructions.

> **Critical:** For Revenue to work, every closed opportunity MUST have a monetary value set!

### 5.2 Chat Widget Attribution

Leads from Chat Widgets often show as DIRECT unless they clicked an ad immediately before.

- **Verification:** Check the Contact Activity log to see the "Referrer" URL.

### 5.3 Client Spend (Agency Pro)

If you charge a management fee, you can hide the raw ad cost and show "Client Spend".

- **Setting:** Agency Settings > Reporting > Client Spend Markup.

---

## 📞 Phase 5.5: Call Tracking Setup

There are two methods for call tracking. Use **both** for complete coverage.

### Option A: Static Tracking Numbers (For Ads)

Purchase dedicated numbers for each ad channel. Use these in ad call extensions and creatives.

**Path:** `Settings > Phone Numbers > Buy Number`

| Channel | Number Label | Where to Use |
| :--- | :--- | :--- |
| Google Ads | `CLIENT-GOOGLE` | Google call extensions, search ads |
| Meta Ads | `CLIENT-META` | Facebook/Instagram ad creatives |
| LSA | `CLIENT-LSA` | Local Service Ads profile |
| Organic | `CLIENT-ORGANIC` | GMB, website footer, direct |

- [ ] Google Ads tracking number purchased
- [ ] Meta Ads tracking number purchased
- [ ] LSA tracking number purchased (if applicable)
- [ ] Organic tracking number purchased
- [ ] Numbers applied to respective ad platforms

> **Cost:** ~$6-8/month (3-4 numbers × $2/each)

---

### Option B: Number Pools (Dynamic Website Tracking)

Number Pools use Dynamic Number Insertion (DNI) to swap phone numbers at the visitor level, enabling **keyword-level call attribution** on your website/funnel.

**Path:** `Settings > Phone Numbers > Number Pool > Add Number Pool`

1. **Tracking Type:** Select `Visitors Activity` (tracks PPC keywords, sources, etc.)
2. **Pool Size:** Minimum 4 numbers (more = better accuracy for high traffic)
3. **Forwarding Number:** Enter client's main business line
4. **Swapping Number:** The number currently displayed on the website (will be replaced dynamically)

- [ ] Number Pool created with 4+ numbers
- [ ] Forwarding number set to main business line
- [ ] Swapping number matches website display number

### 5.5.2 Install the Swap Script

1. After creating the pool, click **Get Code** to copy the snippet
2. Go to your funnel/website in GHL
3. Navigate to **Settings > Tracking Code > Footer Tracking**
4. Paste the snippet code

> **Important:** The script must be in the **Footer** (body), not the Header.

- [ ] Swap script copied from Number Pool
- [ ] Script pasted in Footer Tracking Code

### 5.5.3 Verify Call Tracking

1. Open your funnel in an **Incognito/Private browser**
2. The phone number should dynamically change to a pool number
3. Make a test call — verify it appears in **Reporting > Call Report**

- [ ] Phone number swaps correctly on page load
- [ ] Test call appears in Call Report with source attribution

> **Supported Formats:** `111-222-3333`, `(111) 222-3333`, `111.222.3333`

---

## 🌐 Phase 5.6: External Site Tracking

For clients with WordPress, Wix, or custom websites (not GHL-hosted).

### 5.6.1 Get the GHL Tracking Script

**Path:** `Settings > Business Profile > Tracking Code`

Copy the universal tracking script. It looks like:

```html
<script src="https://widgets.leadconnectorhq.com/loader.js" 
        data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" 
        data-widget-id="YOUR_WIDGET_ID"></script>
```

### 5.6.2 Install on WordPress (Recommended Method)

1. Install plugin: **"Insert Headers and Footers"** (WPCode)
2. Go to **Settings > WPCode > Header & Footer**
3. Paste GHL tracking script in **Header** section
4. Save changes

- [ ] WPCode plugin installed
- [ ] GHL tracking script pasted in header
- [ ] Changes saved

### 5.6.3 Install via Google Tag Manager

1. Create **Custom HTML Tag** in GTM
2. Paste the full GHL tracking script
3. Trigger: All Pages
4. Publish container

> **Warning:** Ensure `data-widget-id` attribute is preserved. GTM may strip it.

### 5.6.4 Form Compatibility Note

GHL tracking only captures form submissions from actual `<form>` HTML elements.

| Form Builder | Works? |
|--------------|--------|
| WPForms | ✅ Yes |
| Gravity Forms | ✅ Yes |
| Elementor Forms | ⚠️ May not work (uses divs) |
| Divi Forms | ⚠️ May not work |

---

## 🔗 Phase 5.7: Trigger Links

Trigger Links track clicks in emails/SMS and can automatically start workflows.

### 5.7.1 Create a Trigger Link

**Path:** `Marketing > Trigger Links > + Create`

1. **Name:** Descriptive name (e.g., "Promo Click - January Sale")
2. **Redirect URL:** Final destination after click
3. **Save**

### 5.7.2 Use in Campaigns

Insert trigger links in:

- Email campaigns
- SMS messages
- WhatsApp messages

When clicked:

- Activity logged in contact timeline
- Can trigger automated workflows

### 5.7.3 Trigger Workflow on Click

1. Go to **Automation > Workflows > + Create**
2. **Trigger:** `Trigger Link Clicked`
3. Select your trigger link
4. Add follow-up actions (send email, add tag, notify team, etc.)

- [ ] Trigger links created for key CTAs
- [ ] Workflows connected to trigger link clicks

---

## ✉️ Phase 5.8: Email Tracking Setup

Ensure email opens and clicks are tracked properly.

### 5.8.1 Configure Dedicated Sending Domain

**Path:** `Settings > Email Services > Dedicated Domain`

1. Add your sending domain (e.g., `mail.clientdomain.com`)
2. Add DNS records: SPF, DKIM, DMARC
3. Verify domain

- [ ] Dedicated domain added
- [ ] DNS records configured
- [ ] Domain verified

### 5.8.2 Enable Click & Open Tracking

**Path:** `Settings > Email Services > Tracking`

- [ ] **Open Tracking:** Enabled
- [ ] **Click Tracking:** Enabled

> **Note:** These settings affect deliverability. Most clients should have both ON.

---

## ✅ Phase 6: Verification Checklist

Before going live, verify the entire setup end-to-end.

### 6.1 Test Lead Submission

- [ ] Click an ad (or use UTM test URL)
- [ ] Submit a form on the landing page
- [ ] Check **Contacts** in GHL — new contact appears
- [ ] Check contact's **Activity** tab — Attribution shows correct source
- [ ] Check contact's **Custom Fields** — UTM values populated

### 6.2 Test Call Tracking

- [ ] Open funnel in incognito browser
- [ ] Verify phone number swapped to pool number
- [ ] Make test call
- [ ] Check **Reporting > Call Report** — call appears with source

### 6.3 Verify Workflow Execution

- [ ] Go to **Automation > Logs**
- [ ] Confirm the Lead workflow fired for your test contact
- [ ] Create a test opportunity with $100 value
- [ ] Move to "Closed Won" stage
- [ ] Confirm the Closed Won workflow fired

### 6.4 Verify Ad Platform Data (24-48 hours later)

- [ ] Check **Google Ads > Tools > Conversions** — test conversion appears
- [ ] Check **Meta Events Manager > Test Events** — test event appears
- [ ] Check **GHL > Reporting > Google Ads** — Leads column populated

### 6.5 Common Issues

| Symptom | Likely Cause | Fix |
| :--- | :--- | :--- |
| Attribution shows "Direct" | UTM params missing | Check tracking template |
| Custom fields empty | Fields not on form | Add hidden fields to form |
| No conversions in Google | Workflow not firing | Check Automation Logs |
| Revenue always $0 | Opportunity value blank | Set monetary value |
| Phone not swapping | Script in wrong location | Move to Footer Tracking |
| Calls not in report | Pool not configured | Verify Number Pool setup |

---

## 📋 Appendix B: Sub-Account Audit Checklist

Use this for **overhauling existing client sub-accounts**. Print and check off each item.

### Platform Connections

| Component | Location | Status |
|-----------|----------|:------:|
| Google Ads Connected | Settings > Integrations | [ ] |
| Google Ads Account Selected | Reporting > Google Ads Settings | [ ] |
| Meta Connected | Settings > Integrations | [ ] |
| Meta Ad Account Selected | Reporting > Facebook Ads Settings | [ ] |

### UTM Tracking

| Component | Location | Status |
|-----------|----------|:------:|
| Google Tracking Template | Google Ads > Account Settings > Tracking | [ ] |
| Auto-Tagging Enabled | Google Ads > Account Settings | [ ] |
| Meta UTM Parameters | Ads Manager > Ad Level > URL Parameters | [ ] |

### GHL Configuration

| Component | Location | Status |
|-----------|----------|:------:|
| 7 Custom Fields Created | Settings > Custom Fields > Contact | [ ] |
| Hidden Fields on All Forms | Funnel > Form > Hidden Fields | [ ] |
| Number Pool Created (4+) | Settings > Phone Numbers > Number Pool | [ ] |
| Swap Script Installed | Funnel > Settings > Footer Tracking | [ ] |

### Workflows

| Component | Location | Status |
|-----------|----------|:------:|
| Google Lead Workflow | Automation > Workflows | [ ] |
| Google Closed Won Workflow | Automation > Workflows | [ ] |
| Meta Lead Workflow | Automation > Workflows | [ ] |
| Meta Purchase Workflow | Automation > Workflows | [ ] |

### Email Configuration

| Component | Location | Status |
|-----------|----------|:------:|
| Dedicated Domain Added | Settings > Email Services | [ ] |
| SPF/DKIM/DMARC Configured | DNS Provider | [ ] |
| Click Tracking Enabled | Settings > Email Services > Tracking | [ ] |
| Open Tracking Enabled | Settings > Email Services > Tracking | [ ] |

---

## Appendix A: Fail-Safe Script

```javascript
function main() {
  var TrackingTemplate = "{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={CampaignName}&utm_content={AdGroupName}&utm_term={keyword}&campaign_id={campaignid}&ad_group_id={adgroupid}&ad_id={creative}";
  var _CAMPAIGN_CONTAINS = "";
  var _ADGROUP_CONTAINS = "";
  var STATUS = "ENABLED";
  // ... (Full script available in GHL Article 48001219356)
}
```

*(Note: Full script omitted for brevity, ensure you copy the referenced article version.)*

---

## Related Documents

- [GHL_Workflow_Setup_Steps.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_Workflow_Setup_Steps.md) — Detailed workflow creation guide
- [Ad_Tracking_Audit_Checklist.md](file:///d:/Operations/Meta%20&%20Google%20ADS/Ad_Tracking_Audit_Checklist.md) — Quick audit for existing setups
- [Call_Tracking_Strategy.md](file:///d:/Operations/Meta%20&%20Google%20ADS/Call_Tracking_Strategy.md) — Phone tracking deep dive
- [LSA_Tracking_Guide.md](file:///d:/Operations/Meta%20&%20Google%20ADS/LSA_Tracking_Guide.md) — Local Service Ads specific setup
