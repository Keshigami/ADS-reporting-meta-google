# GHL Sub-Account Call Tracking Setup

## Standard 4-Number Attribution System

---

## Overview

Each client sub-account gets **up to 4 GHL phone numbers** for clear call attribution:

| Number | Purpose | Used In |
|--------|---------|---------|
| #1 | Meta Ads | Facebook ads, Instagram ads, Meta landing pages |
| #2 | Google Ads | Google Search Ads, Display, Google landing pages |
| #3 | Local Service Ads (LSA) | Google LSA (if applicable) |
| #4 | Organic/Other | Website, GMB, Yelp, print, referrals |

**Cost:** $6-8/month per client (3-4 numbers × $2/each)

---

## Setup Checklist (Per Client)

### Phase 1: Buy Numbers

- [ ] Go to client's GHL sub-account
- [ ] Settings → Phone Numbers → Buy Number
- [ ] Buy 3 numbers with same area code as business
- [ ] Name them clearly:
  - `Google Ads Tracking`
  - `Facebook Ads Tracking`
  - `Organic/Website Tracking`

### Phase 2: Configure Forwarding

- [ ] Each number forwards to client's main business line
- [ ] Settings → Phone Numbers → Click number → Forwarding
- [ ] Enter business phone number
- [ ] Enable call recording (optional)

### Phase 3: Update Ads

- [ ] **Google Ads:**
  - Call extensions → Use Google Ads number
  - Landing pages → Use Google Ads number
  - Ad copy phone mentions → Google Ads number

- [ ] **Facebook Ads:**
  - Ad copy → Use Facebook number
  - Landing pages → Use Facebook number
  - Messenger auto-replies → Facebook number

- [ ] **Website:**
  - Header → Use Organic number
  - Contact page → Use Organic number
  - Footer → Use Organic number

### Phase 4: Update External Listings

- [ ] Google Business Profile → Use Organic number
- [ ] Yelp → Use Organic number
- [ ] Other directories → Use Organic number

### Phase 5: Verify in n8n

- [ ] Add client to Notion Clients database
- [ ] Add all 3 GHL numbers to client record
- [ ] Test workflow pulls call data

---

## Number Naming Convention

Use consistent naming in GHL:

```
[ClientCode]-[Channel]

Examples:
ACTON-GOOGLE
ACTON-FACEBOOK
ACTON-ORGANIC
```

---

## Client Tracking Sheet

| Client | Meta # | Google # | LSA # | Organic # | Status |
|--------|--------|----------|-------|-----------|--------|
| MEC Builds | TBD | TBD | TBD | TBD | In Setup |
| Acton | 530-557-3502 | TBD | N/A | TBD | Partial |
| [Client B] | | | | | Not Started |

---

## Notion Database Updates

Add these fields to **Clients** database:

| Field | Type | Purpose |
|-------|------|---------|
| GHL Google Number | Text | Google Ads tracking number |
| GHL Facebook Number | Text | Facebook tracking number |
| GHL Organic Number | Text | Website/organic tracking number |
| Call Tracking Status | Select | Not Started, Partial, Complete |

---

## Verification Steps

After setup, verify:

1. **Test call to each number:**
   - Call Google number → Appears in GHL with "Google Ads Tracking" label
   - Call Facebook number → Appears with "Facebook Tracking" label
   - Call Organic number → Appears with "Organic Tracking" label

2. **Check forwarding:**
   - All calls forward to business phone
   - Business can answer normally

3. **Check recording (if enabled):**
   - Recordings appear in GHL

---

## Weekly Report Output

Once implemented, reports show:

```
📞 CALL ATTRIBUTION - ACTON

                     Calls    Spend    Cost/Call
─────────────────────────────────────────────────
Google Ads           28       $385     $13.75
Facebook Ads         15       $220     $14.67
Organic/Other        12       $0       FREE
─────────────────────────────────────────────────
TOTAL                55

💡 Insight: Google Ads generating 2x calls vs Facebook
```

---

## Cost Summary

| Clients | Monthly Cost |
|---------|--------------|
| 1 client | $6/mo |
| 5 clients | $30/mo |
| 10 clients | $60/mo |

---

## Implementation Priority

1. **Acton** - Pilot client (already has 1 number)
2. Other active ad clients
3. New clients during onboarding

---

*Last Updated: December 22, 2024*
