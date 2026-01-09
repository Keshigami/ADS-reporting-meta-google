# Call Tracking Strategy

## For Multi-Channel Ad Campaigns

---

## Overview

This document outlines how to track phone calls from all advertising channels (Google Ads, Facebook Ads, Local Service Ads) and attribute them correctly in reports.

---

## The Problem

| Channel | Native Call Tracking? |
|---------|----------------------|
| Google Call Ads | ✅ Yes (Google forwarding numbers) |
| Facebook Ads | ❌ No |
| Local Service Ads | ⚠️ Separate system |
| Website | ❌ No |
| Organic/Referral | ❌ No |

**Challenge:** Each platform tracks differently (or not at all), making unified reporting difficult.

---

## Solution: GHL Phone Numbers

Use GHL phone numbers as a unified tracking layer:

```
All Ad Channels ──→ GHL Phone Number ──→ Business Phone
                          │
                          ▼
                    All Calls Logged
                          │
                          ▼
                   n8n Weekly Reports
```

---

## Tracking Granularity Options

### Level 1: One Number for All ($2/month)

```
Google Ads  ──┐
Facebook   ───┼──→  One GHL Number  ──→  Total: 47 calls
Website    ───┘
```

**Know:** Total call volume  
**Don't Know:** Which channel drove each call

---

### Level 2: One Number Per Channel ($6-8/month)

```
Meta Ads    ──→  Number 1  ──→  15 calls from Meta
Google Ads  ──→  Number 2  ──→  28 calls from Google
LSA         ──→  Number 3  ──→  12 calls from LSA
Website     ──→  Number 4  ──→  4 calls from Website
```

**Know:** Calls per channel  
**Don't Know:** Which specific campaign within each channel

---

### Level 3: One Number Per Campaign ($12+/month)

```
Google Brand    ──→  Number 1  ──→  10 calls
Google Service  ──→  Number 2  ──→  18 calls
Facebook Lead   ──→  Number 3  ──→  12 calls
Facebook Retarget ──→  Number 4  ──→  3 calls
Website        ──→  Number 5  ──→  4 calls
```

**Know:** Exact campaign attribution  
**Cost:** More numbers = more monthly cost

---

## Recommended Approach by Client Size

| Client Type | Recommendation | Cost |
|-------------|---------------|------|
| Small (1-2 campaigns) | One number per channel (3 numbers) | $6/mo |
| Medium (has LSA) | One number per channel + LSA (4 numbers) | $8/mo |
| Large/High-spend | CallRail for dynamic insertion | $45/mo |

---

## Implementation Checklist

### Phase 1: Immediate Tracking (Day 1)

- [ ] Buy GHL phone number(s) with local area code
- [ ] Configure forwarding to business phone
- [ ] Enable call recording (if desired)
- [ ] Update Google Ads with GHL number
- [ ] Update Facebook Ads with GHL number
- [ ] Update landing pages with GHL number

### Phase 2: Number Porting (Week 2)

- [ ] Gather carrier info from client
- [ ] Submit port request in GHL
- [ ] Client signs LOA
- [ ] Wait for port completion (7-14 days)
- [ ] Replace tracking numbers with ported number
- [ ] Full tracking live with original business number

---

## Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│                       CALL DATA FLOW                        │
└─────────────────────────────────────────────────────────────┘

Caller Dials GHL Number
         │
         ▼
┌─────────────────┐
│  GHL Receives   │
│     Call        │
├─────────────────┤
│ • Logs call     │
│ • Creates/updates contact
│ • Records call (optional)
│ • Triggers webhook
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  n8n Webhook    │
│  (Optional)     │
├─────────────────┤
│ • Add tags      │
│ • Update fields │
│ • Send notifications
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Weekly Report  │
├─────────────────┤
│ Google: 28 calls│
│ Facebook: 15    │
│ Website: 4      │
│ Total: 47       │
└─────────────────┘
```

---

## Metrics Available from GHL

| Metric | Available? |
|--------|-----------|
| Total calls | ✅ Yes |
| Call duration | ✅ Yes |
| Caller phone number | ✅ Yes |
| Call timestamp | ✅ Yes |
| Call recording | ✅ Yes (if enabled) |
| Call outcome | ✅ Yes (answered/missed/voicemail) |
| Which GHL number called | ✅ Yes (for channel attribution) |

---

## Integration with Weekly Reports

The n8n workflow pulls call data via GHL API:

```javascript
// GHL API call
GET /conversations/search?type=call&startDate=2024-12-16&endDate=2024-12-22

// Returns:
{
  "conversations": [
    {
      "id": "abc123",
      "contactId": "contact_xyz",
      "phone": "+15551234567",
      "dateAdded": "2024-12-18T14:30:00Z",
      "type": "call",
      "duration": 180
    }
  ]
}
```

---

*Last Updated: December 22, 2024*
