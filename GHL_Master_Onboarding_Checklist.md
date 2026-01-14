# GHL Master Onboarding Checklist

**BMM's Complete Client Setup — Start to Finish**

Use this as your single source of truth when onboarding a new client or auditing an existing sub-account.

---

## 📋 Phase Overview

| Phase | Category | Time Est. |
|:---:|:---|:---:|
| 1 | Prerequisites & Access | 30 min |
| 2 | Sub-Account Creation | 15 min |
| 3 | Pipelines & Custom Fields | 30 min |
| 4 | Tag Strategy | 15 min |
| 5 | **Tracking Setup** (Ads + Attribution) | 60 min |
| 6 | Workflows (8 Standard) | 45 min |
| 7 | Calendar & Templates | 30 min |
| 8 | Reputation & Reporting | 20 min |
| 9 | Verification & Go-Live | 30 min |

**Total Estimated Time: ~4.5 hours**

---

## ✅ Phase 1: Prerequisites & Access

Before anything else, collect:

### Client Information

- [ ] Business Name
- [ ] Timezone
- [ ] Primary Contact (Email + Phone)
- [ ] Website URL
- [ ] Industry

### Brand Assets

- [ ] Logo (PNG, transparent, 500px+)
- [ ] Brand Colors (hex codes)
- [ ] Business Address

### Platform Access

- [ ] Google Ads access granted (Admin)
- [ ] Meta Business Manager access granted
- [ ] GMB access (for reputation)
- [ ] Google Ads Conversion ID: `AW-__________`
- [ ] Meta Pixel ID: `__________`

---

## ✅ Phase 2: Sub-Account Creation

### 2.1 Create Sub-Account

**Path:** `Agency > Sub-Accounts > + Add Sub-Account`

- [ ] Business name entered
- [ ] Timezone set correctly
- [ ] Sub-account created

### 2.2 Initial Branding

**Path:** `Settings > Business Profile`

- [ ] Logo uploaded
- [ ] Business name set
- [ ] Address entered

---

## ✅ Phase 3: Pipelines & Custom Fields

### 3.1 Sales Pipeline (8 Stages)

**Path:** `Opportunities > Pipelines > + Add Pipeline`

| Stage | Order |
|:---|:---:|
| New Lead | 1 |
| Contacted | 2 |
| Qualified | 3 |
| Appointment Booked | 4 |
| Proposal Sent | 5 |
| Negotiation | 6 |
| Closed Won | 7 |
| Closed Lost | 8 |

- [ ] Sales pipeline created
- [ ] All 8 stages added

### 3.2 Custom Fields

**Path:** `Settings > Custom Fields > Contact`

**Attribution Fields (7):**

| Field | Type |
|:---|:---|
| utm_source | Single Line Text |
| utm_medium | Single Line Text |
| utm_campaign | Single Line Text |
| utm_content | Single Line Text |
| utm_term | Single Line Text |
| gclid | Single Line Text |
| fbclid | Single Line Text |

- [ ] 7 UTM/attribution fields created

**Business Fields:**

| Field | Type |
|:---|:---|
| Lead Value | Number |
| Industry | Dropdown |
| Service Interest | Multi-Select |

- [ ] Business fields created

---

## ✅ Phase 4: Tag Strategy

**Path:** `Settings > Tags`

**Convention:** `[category]_[value]`

### Pre-Create These Tags

- [ ] `source_google`
- [ ] `source_meta`
- [ ] `source_lsa`
- [ ] `source_organic`
- [ ] `status_hot`
- [ ] `status_warm`
- [ ] `status_cold`
- [ ] `nurture_active`
- [ ] `nurture_complete`

---

## ✅ Phase 5: Tracking Setup

> **Detailed Guide:** [GHL_Ultimate_Tracking_Guide.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_Ultimate_Tracking_Guide.md)

### 5.1 Connect Ad Platforms

**Path:** `Settings > Integrations`

- [ ] Google Ads connected
- [ ] Google Ads account selected in Reporting
- [ ] Meta (Facebook) connected
- [ ] Meta Ad Account selected in Reporting

### 5.2 Google Ads Tracking Template

**Path:** Google Ads > Account Settings > Tracking

```
{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignname}&utm_content={adgroupname}&utm_term={keyword}&campaign_id={campaignid}&ad_group_id={adgroupid}&ad_id={creative}
```

- [ ] Tracking template pasted
- [ ] Auto-tagging enabled

### 5.3 Meta Ads UTM Parameters

**Path:** Ads Manager > Ad Level > URL Parameters

```
utm_source=facebook&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&campaign_id={{campaign.id}}
```

- [ ] UTM parameters added to all ads

### 5.4 Form Hidden Fields

**Path:** Funnel > Form > Settings > Pre-fill

Add hidden fields mapped to custom fields:

- [ ] utm_source
- [ ] utm_medium
- [ ] utm_campaign
- [ ] utm_content
- [ ] utm_term
- [ ] gclid
- [ ] fbclid

### 5.5 Call Tracking

**Option A: Static Numbers (For Ads)**
**Path:** `Settings > Phone Numbers > Buy Number`

- [ ] CLIENT-GOOGLE purchased
- [ ] CLIENT-META purchased
- [ ] CLIENT-LSA purchased (if applicable)
- [ ] CLIENT-ORGANIC purchased

**Option B: Number Pool (For Website)**
**Path:** `Settings > Phone Numbers > Number Pool`

- [ ] Number Pool created (4+ numbers)
- [ ] Swap script added to Footer Tracking

---

## ✅ Phase 6: Workflows (8 Standard)

**Path:** `Automation > Workflows`

| # | Workflow | Trigger | Created |
|:---:|:---|:---|:---:|
| 1 | Lead Response | Form Submitted | [ ] |
| 2 | Lead Nurture | Tag: nurture_active | [ ] |
| 3 | Appointment Reminder | Appt Booked | [ ] |
| 4 | No-Show Follow-Up | Appt No Show | [ ] |
| 5 | Review Request | Pipeline → Closed Won | [ ] |
| 6 | Stale Lead Reactivation | 30 days inactive | [ ] |
| 7 | ROAS - Google | Contact Created | [ ] |
| 8 | ROAS - Meta | Contact Created | [ ] |

> **Workflow Details:** [GHL_SubAccount_Setup_Standard.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_SubAccount_Setup_Standard.md) — Phase 4

---

## ✅ Phase 7: Calendar & Templates

### 7.1 Discovery Call Calendar

**Path:** `Calendars > + Add`

- [ ] Calendar created (30 min duration)
- [ ] Availability set
- [ ] Reminders configured (24hr + 1hr)

### 7.2 Templates

**Path:** `Marketing > Templates`

- [ ] Welcome Email created
- [ ] Appointment Confirmation SMS created
- [ ] Appointment Reminder SMS created
- [ ] Review Request SMS created

---

## ✅ Phase 8: Reputation & Reporting

### 8.1 Reputation

**Path:** `Reputation > Settings`

- [ ] Google review link configured
- [ ] Review workflow (#5) active

### 8.2 Dashboard

**Path:** `Dashboard > Widgets`

- [ ] Pipeline Value widget added
- [ ] Leads This Month widget added
- [ ] Revenue widget added

---

## ✅ Phase 9: Verification & Go-Live

### 9.1 Test Lead Submission

- [ ] Click test ad URL with UTMs
- [ ] Submit form on landing page
- [ ] Verify contact created in CRM
- [ ] Verify attribution in contact Activity tab
- [ ] Verify custom fields populated

### 9.2 Test Call Tracking

- [ ] Open funnel in incognito
- [ ] Verify phone number swaps (if using pool)
- [ ] Make test call
- [ ] Verify call in Reporting > Call Report

### 9.3 Test Workflows

- [ ] Verify Lead Response workflow fired
- [ ] Create test opportunity ($100)
- [ ] Move to Closed Won
- [ ] Verify ROAS workflow fired

### 9.4 Final Checks

- [ ] All workflows published (not draft)
- [ ] All forms have hidden fields
- [ ] Client has portal access (if applicable)

---

## 📚 Reference Documents

| Document | Purpose |
|:---|:---|
| [GHL_Ultimate_Tracking_Guide.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_Ultimate_Tracking_Guide.md) | Detailed tracking & attribution setup |
| [GHL_SubAccount_Setup_Standard.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_SubAccount_Setup_Standard.md) | Full sub-account configuration |
| [GHL_Workflow_Setup_Steps.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_Workflow_Setup_Steps.md) | Detailed ROAS workflow instructions |

---

**Created by:** Banner Mountain Media  
**Last Updated:** January 2026
