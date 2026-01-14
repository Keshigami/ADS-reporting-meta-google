# GHL Sub-Account Setup Standard

**BMM's Standard Operating Procedure for GoHighLevel Client Accounts**

This guide standardizes all GHL sub-account configurations for consistent operations, accurate reporting, and scalable client management.

---

## ⚡ Quick Start Checklist

| Phase | Task | Status |
| :--- | :--- | :---: |
| 0 | Prerequisites gathered | [ ] |
| 1 | Pipelines created (Sales + Onboarding) | [ ] |
| 2 | Custom fields created | [ ] |
| 3 | Tag strategy implemented | [ ] |
| 4 | 8 standard workflows created | [ ] |
| 5 | Calendar & booking configured | [ ] |
| 6 | Email/SMS templates created | [ ] |
| 7 | Reputation management setup | [ ] |
| 8 | Reporting dashboard configured | [ ] |
| 9 | White-label settings applied | [ ] |

> **For Existing Clients:** Skip to [Appendix: Sub-Account Audit Checklist](#-appendix-sub-account-audit-checklist)

---

## 🔐 Phase 0: Prerequisites

Before creating the sub-account, gather:

### 0.1 Client Information

- [ ] Business Name
- [ ] Timezone
- [ ] Primary Contact Email
- [ ] Primary Contact Phone
- [ ] Website URL
- [ ] Industry/Vertical

### 0.2 Assets Needed

- [ ] Logo (PNG, transparent background, min 500px)
- [ ] Brand colors (hex codes)
- [ ] Business address
- [ ] Social media URLs

### 0.3 Access Credentials

- [ ] Google Ads access (for ROAS tracking)
- [ ] Meta Business Manager access
- [ ] GMB access (for reputation management)

---

## 📊 Phase 1: Pipeline Setup

Create standardized pipelines for consistent reporting.

### 1.1 Sales Pipeline

**Path:** `Opportunities > Pipelines > + Add Pipeline`

**Name:** `Sales`

| Stage | Order | Purpose |
| :--- | :---: | :--- |
| New Lead | 1 | Fresh inquiry, not yet contacted |
| Contacted | 2 | First contact attempted |
| Qualified | 3 | Meets criteria, potential fit |
| Appointment Booked | 4 | Discovery call scheduled |
| Proposal Sent | 5 | Quote/proposal delivered |
| Negotiation | 6 | Active price/scope discussions |
| Closed Won | 7 | Deal signed ✅ |
| Closed Lost | 8 | Deal lost ❌ |

- [ ] Sales pipeline created with 8 stages
- [ ] Stages ordered correctly
- [ ] Default pipeline set to Sales

### 1.2 Onboarding Pipeline (Optional)

**Name:** `Onboarding`

| Stage | Order | Purpose |
| :--- | :---: | :--- |
| Kickoff Scheduled | 1 | Onboarding call set |
| Assets Received | 2 | Logos, access, content collected |
| Setup In Progress | 3 | Building campaigns |
| Client Review | 4 | Awaiting approval |
| Live | 5 | Campaigns active ✅ |

- [ ] Onboarding pipeline created (if applicable)

### 1.3 Opportunity Settings

**Path:** `Settings > Opportunities`

- [ ] Default currency: `USD`
- [ ] Default pipeline: `Sales`

---

## 🏷️ Phase 2: Custom Fields

### 2.1 UTM/Attribution Fields

> **See:** [GHL_Ultimate_Tracking_Guide.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_Ultimate_Tracking_Guide.md) — Phase 1.5

**Path:** `Settings > Custom Fields > Contact`

| Field Name | Type |
| :--- | :--- |
| utm_source | Single Line Text |
| utm_medium | Single Line Text |
| utm_campaign | Single Line Text |
| utm_content | Single Line Text |
| utm_term | Single Line Text |
| gclid | Single Line Text |
| fbclid | Single Line Text |

- [ ] 7 UTM fields created

### 2.2 Business Fields

| Field Name | Type | Purpose |
| :--- | :--- | :--- |
| Lead Value | Number | Estimated deal value |
| Industry | Dropdown | Client vertical |
| Service Interest | Multi-Select | Which services they want |
| Assigned Rep | Dropdown | Team member responsible |
| Lead Score | Number | Qualification score (1-100) |

- [ ] Business fields created

---

## 🏷️ Phase 3: Tag Strategy

Use consistent naming for automation and reporting.

### 3.1 Naming Convention

**Format:** `[category]_[value]`

| Category | Examples | Use For |
| :--- | :--- | :--- |
| `source_` | `source_google`, `source_meta`, `source_lsa`, `source_organic` | Traffic source |
| `service_` | `service_ads`, `service_seo`, `service_web` | Service interest |
| `status_` | `status_hot`, `status_warm`, `status_cold` | Lead temperature |
| `campaign_` | `campaign_spring2026`, `campaign_promo` | Campaign tracking |
| `stage_` | `stage_qualified`, `stage_proposal` | Pipeline triggers |

### 3.2 Required Tags (Pre-Create)

**Path:** `Settings > Tags`

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

## ⚙️ Phase 4: Standard Workflows

Create these 8 essential workflows.

### 4.1 Workflow Summary

**Path:** `Automation > Workflows > + Create Workflow`

| # | Workflow Name | Trigger | Key Actions |
| :---: | :--- | :--- | :--- |
| 1 | Lead Response | Form Submitted | Instant SMS + Email welcome |
| 2 | Lead Nurture | Tag Added: `nurture_active` | 5-day drip sequence |
| 3 | Appointment Reminder | Appointment Booked | SMS 24hr + 1hr before |
| 4 | No-Show Follow-Up | Appointment Status: No Show | SMS + Email to reschedule |
| 5 | Review Request | Pipeline → Closed Won | Wait 7 days, request review |
| 6 | Stale Lead Reactivation | 30 days no activity | Re-engagement sequence |
| 7 | ROAS - Google | Contact Created | Add to Google Ads |
| 8 | ROAS - Meta | Contact Created | Facebook CAPI |

### 4.2 Workflow Details

#### Workflow 1: Lead Response

**Trigger:** Form Submitted (any form)

**Actions:**

1. Wait 1 minute
2. Send SMS: "Hi {{contact.first_name}}, thanks for reaching out! We'll be in touch shortly."
3. Send Email: Welcome email with next steps
4. Add Tag: `nurture_active`
5. Internal notification to team

- [ ] Lead Response workflow created and published

#### Workflow 2: Lead Nurture

**Trigger:** Tag Added → `nurture_active`

**Actions:**

1. Day 1: Email with value content
2. Day 2: SMS check-in
3. Day 3: Email case study
4. Day 5: Final follow-up email
5. Add Tag: `nurture_complete`
6. Remove Tag: `nurture_active`

- [ ] Lead Nurture workflow created and published

#### Workflow 3: Appointment Reminder

**Trigger:** Customer Booked Appointment

**Actions:**

1. Send confirmation SMS immediately
2. Wait until 24 hours before → Send SMS reminder
3. Wait until 1 hour before → Send SMS reminder

- [ ] Appointment Reminder workflow created and published

#### Workflow 4: No-Show Follow-Up

**Trigger:** Appointment Status → No Show

**Actions:**

1. Send SMS: "We missed you! Let's reschedule: [booking link]"
2. Wait 24 hours
3. Send Email: Reschedule offer
4. Add Tag: `status_cold`

- [ ] No-Show Follow-Up workflow created and published

#### Workflow 5: Review Request

**Trigger:** Pipeline Stage Changed → Closed Won

**Actions:**

1. Wait 7 days
2. Send SMS: "How was your experience? Leave us a review: [review link]"
3. Wait 3 days (if no review)
4. Send Email: Review reminder

- [ ] Review Request workflow created and published

#### Workflow 6: Stale Lead Reactivation

**Trigger:** Contact → Last Activity > 30 days

**Filter:** Tag does not contain `status_cold`

**Actions:**

1. Send Email: "We haven't heard from you..."
2. Wait 3 days
3. Send SMS: Re-engagement nudge
4. Add Tag: `status_cold` (if no response)

- [ ] Stale Lead Reactivation workflow created and published

#### Workflows 7-8: ROAS Tracking

> **See:** [GHL_Ultimate_Tracking_Guide.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_Ultimate_Tracking_Guide.md) — Phase 5.1

- [ ] ROAS - Google workflow created
- [ ] ROAS - Meta workflow created

---

## 📅 Phase 5: Calendar & Booking

### 5.1 Create Discovery Call Calendar

**Path:** `Calendars > + Add Calendar`

**Settings:**

- Name: `Discovery Call`
- Duration: 30 minutes
- Buffer: 15 minutes
- Availability: Client business hours

- [ ] Discovery Call calendar created

### 5.2 Reminder Settings

**Path:** Calendar > Edit > Notifications

- [ ] Confirmation email enabled
- [ ] 24-hour reminder enabled
- [ ] 1-hour reminder enabled

### 5.3 Booking Widget

- [ ] Embed code added to funnel/site
- [ ] Booking link tested

---

## ✉️ Phase 6: Email & SMS Templates

### 6.1 Required Templates

**Path:** `Marketing > Templates`

| Template Name | Type | Purpose |
| :--- | :--- | :--- |
| Welcome Email | Email | After form submission |
| Appointment Confirmation | SMS | After booking |
| Appointment Reminder | SMS | 24hr/1hr before |
| Review Request | SMS | After Closed Won |
| Opt-Out Confirmation | SMS | TCPA compliance |

### 6.2 SMS Compliance

All SMS must include opt-out language:

```
Reply STOP to unsubscribe.
```

- [ ] All SMS templates include opt-out footer
- [ ] Opt-out workflow enabled

---

## ⭐ Phase 7: Reputation Management

### 7.1 Review Request Setup

**Path:** `Reputation > Settings`

- [ ] Google review link configured
- [ ] Review request workflow (Workflow 5) active

### 7.2 GMB Integration (Optional)

**Path:** `Settings > Integrations > Google My Business`

- [ ] GMB account connected
- [ ] Review monitoring enabled

---

## 📈 Phase 8: Reporting Dashboard

### 8.1 Standard Widgets

**Path:** `Dashboard > Widgets`

| Widget | Metric |
| :--- | :--- |
| Pipeline Value | Total opportunity value by stage |
| Leads This Month | New contacts count |
| Appointments Booked | Calendar bookings |
| Conversion Rate | Lead → Closed Won % |
| Revenue | Closed Won total value |

- [ ] Dashboard configured with standard widgets

### 8.2 Google/Meta Reporting

**Path:** `Reporting > Google Ads / Facebook Ads`

- [ ] Ad accounts connected
- [ ] ROAS visible in reports

---

## 🎨 Phase 9: White-Label Settings

### 9.1 Custom Domain (Agency Level)

**Path:** `Agency Settings > Domains`

- [ ] Custom domain configured
- [ ] SSL certificate active

### 9.2 Sub-Account Branding

**Path:** `Settings > Business Profile`

- [ ] Business name set
- [ ] Logo uploaded
- [ ] Brand colors applied
- [ ] Timezone set

### 9.3 Client Portal Access

**Path:** `Settings > Team Management`

- [ ] Client user created (if applicable)
- [ ] Permissions set appropriately

---

## 📋 Appendix: Sub-Account Audit Checklist

Use this for **existing clients** to verify all standards are met.

### Pipelines

| Component | Location | Status |
|-----------|----------|:------:|
| Sales Pipeline exists | Opportunities > Pipelines | [ ] |
| 8 standard stages | Pipeline settings | [ ] |
| Onboarding Pipeline (if needed) | Opportunities > Pipelines | [ ] |

### Custom Fields

| Component | Location | Status |
|-----------|----------|:------:|
| 7 UTM fields | Settings > Custom Fields | [ ] |
| Lead Value field | Settings > Custom Fields | [ ] |
| Industry field | Settings > Custom Fields | [ ] |

### Tags

| Component | Location | Status |
|-----------|----------|:------:|
| Source tags created | Settings > Tags | [ ] |
| Status tags created | Settings > Tags | [ ] |
| Naming convention followed | Settings > Tags | [ ] |

### Workflows

| Component | Location | Status |
|-----------|----------|:------:|
| Lead Response | Automation > Workflows | [ ] |
| Lead Nurture | Automation > Workflows | [ ] |
| Appointment Reminder | Automation > Workflows | [ ] |
| No-Show Follow-Up | Automation > Workflows | [ ] |
| Review Request | Automation > Workflows | [ ] |
| Stale Lead Reactivation | Automation > Workflows | [ ] |
| ROAS - Google | Automation > Workflows | [ ] |
| ROAS - Meta | Automation > Workflows | [ ] |

### Calendar

| Component | Location | Status |
|-----------|----------|:------:|
| Discovery Call calendar | Calendars | [ ] |
| Reminders configured | Calendar > Notifications | [ ] |

### Reputation

| Component | Location | Status |
|-----------|----------|:------:|
| Review link configured | Reputation > Settings | [ ] |
| Review workflow active | Automation > Workflows | [ ] |

### Reporting

| Component | Location | Status |
|-----------|----------|:------:|
| Dashboard widgets configured | Dashboard | [ ] |
| Ad accounts connected | Reporting | [ ] |

### Branding

| Component | Location | Status |
|-----------|----------|:------:|
| Business name set | Settings > Business Profile | [ ] |
| Logo uploaded | Settings > Business Profile | [ ] |
| Timezone correct | Settings > Business Profile | [ ] |

---

## Related Documents

- [GHL_Ultimate_Tracking_Guide.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_Ultimate_Tracking_Guide.md) — Tracking & attribution setup
- [GHL_Workflow_Setup_Steps.md](file:///d:/Operations/Meta%20&%20Google%20ADS/GHL_Workflow_Setup_Steps.md) — Detailed ROAS workflow steps
