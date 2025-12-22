# 📞 Call Tracking Options for Ads Reporting

**To:** Jake  
**From:** Wally / Team  
**Re:** How to track calls from Google Ads, Facebook, and LSA

---

## The Problem

For clients like Acton running **Call Ads**, we can't currently track phone calls because:
- Google Call Ads use Google's forwarding numbers (tracked in Google, not GHL)
- Facebook has NO call tracking
- Business has their own phone number (no tracking)

---

## Options to Fix This

### Option A: Use ONE GHL Number Everywhere ⭐ RECOMMENDED

| What | Details |
|------|---------|
| **How it works** | Get one GHL number → Use in ALL ads → All calls logged in GHL |
| **Cost** | ~$2/month |
| **Setup time** | 10 minutes |
| **What you get** | Track calls from Google, Facebook, Website, LSA - all in one place |

**Pros:** Cheapest, simplest, unified tracking  
**Cons:** Different number than business's current number

---

### Option B: Port Business Number to GHL

| What | Details |
|------|---------|
| **How it works** | Move business's existing number INTO GHL |
| **Cost** | Free (just takes time) |
| **Setup time** | 7-14 days for port to complete |
| **What you get** | Same number, now with full tracking |

**Pros:** Keep same number customers know  
**Cons:** Takes 1-2 weeks, requires carrier account info

---

### Option C: Google Forwarding Only (Partial)

| What | Details |
|------|---------|
| **How it works** | Enable Google forwarding numbers for Call Ads only |
| **Cost** | Free |
| **Setup time** | 5 minutes |
| **What you get** | Google Ads calls tracked, Facebook/LSA NOT tracked |

**Pros:** Free, fast  
**Cons:** Only tracks Google Ads, not Facebook calls

---

### Option D: CallRail (Paid Service)

| What | Details |
|------|---------|
| **How it works** | Third-party call tracking service |
| **Cost** | $45/month |
| **Setup time** | 1 hour |
| **What you get** | Full attribution, call recording, AI transcription |

**Pros:** Best features, enterprise-grade  
**Cons:** Monthly cost adds up across clients

---

## Trade-offs Deep Dive

### Option A: GHL Number - Trade-offs

| ✅ Pros | ❌ Cons |
|---------|---------|
| Cheapest ($2/mo) | Different number than customers know |
| Set up in 10 minutes | Client may resist changing their number |
| All channels tracked in one place | If client leaves, they lose the number |
| Auto-creates GHL contacts from callers | Caller ID shows GHL number, not business |
| Full call recordings available | |

**Best for:** New clients, clients okay with new number

---

### Option B: Port to GHL - Trade-offs

| ✅ Pros | ❌ Cons |
|---------|---------|
| Keep the number customers already know | Takes 7-14 days to complete |
| No cost to port | Requires carrier account info (hassle) |
| All channels tracked | Risk of downtime during port (rare) |
| Client keeps number if they leave GHL | Need business owner to sign LOA |
| Full call recordings available | Can't undo easily if issues arise |

**Best for:** Established businesses, clients who value their existing number

---

### Option C: Google Forwarding Only - Trade-offs

| ✅ Pros | ❌ Cons |
|---------|---------|
| Completely free | ONLY tracks Google Ads calls |
| Takes 5 minutes to enable | Facebook, LSA, website calls NOT tracked |
| No changes to business phone | No call recordings |
| Works with existing number | Can't see who called (just count) |
| | Doesn't create GHL contacts |

**Best for:** Clients ONLY running Google Call Ads, not Facebook

---

### Option D: CallRail - Trade-offs

| ✅ Pros | ❌ Cons |
|---------|---------|
| Best-in-class call tracking | $45/month PER CLIENT |
| AI transcription & scoring | Another tool to manage |
| Multiple tracking numbers included | Cost adds up (10 clients = $450/mo) |
| Works with any ad platform | Overkill for small campaigns |
| Easy GHL integration | |

**Best for:** High-volume clients, agencies with budget for tools

---

## Risk Assessment

| Option | What Could Go Wrong | Mitigation |
|--------|--------------------|--------------------|
| A: GHL Number | Client confused by new number | Clear communication, update all listings |
| B: Port to GHL | Port fails/delays | Keep old service active until complete |
| C: Google Only | Miss FB/LSA calls | Only use if Google is primary channel |
| D: CallRail | Budget overrun | Start with 1-2 clients, prove ROI first |

---

## Comparison

| Option | Cost | Setup Time | Google | Facebook | LSA | Keep Same # |
|--------|------|------------|--------|----------|-----|-------------|
| **A: GHL Number** | $2/mo | 10 min | ✅ | ✅ | ✅ | ❌ |
| **B: Port to GHL** | Free | 2 weeks | ✅ | ✅ | ✅ | ✅ |
| **C: Google Only** | Free | 5 min | ✅ | ❌ | ❌ | ✅ |
| **D: CallRail** | $45/mo | 1 hour | ✅ | ✅ | ✅ | ✅ |

---

## Implementation Workflows

### Option A: GHL Number - Step by Step

```
Day 1 (10 minutes)
━━━━━━━━━━━━━━━━━━
1. GHL → Settings → Phone Numbers → Buy Number
2. Choose local area code (match client's area)
3. Set forwarding → Client's real business number
4. Enable Call Recording (optional)
5. Done! Number is live

Day 1-2 (30 minutes)
━━━━━━━━━━━━━━━━━━━━
6. Update Google Ads → Replace number with GHL number
7. Update Facebook Ads → Replace number with GHL number  
8. Update landing pages → Replace number with GHL number

Ongoing
━━━━━━━
• All calls now logged in GHL automatically
• n8n pulls call data for weekly reports
```

---

### Option B: Port to GHL - Step by Step

```
Day 1 (20 minutes)
━━━━━━━━━━━━━━━━━━
1. Get from client:
   - Current carrier name
   - Account number (from phone bill)
   - Account PIN/passcode
   - Service address on file

2. GHL → Settings → Phone Numbers → Port Number
3. Fill out form with client info
4. Download and send LOA to client for signature

Day 2 (5 minutes)
━━━━━━━━━━━━━━━━━
5. Upload signed LOA to GHL
6. Submit port request

Day 7-14 (Wait)
━━━━━━━━━━━━━━━
7. GHL processes port with carriers
8. Client keeps using phone normally during this time
9. Port completes → Number now in GHL
10. Enable call recording, set up forwarding if needed

Ongoing
━━━━━━━
• All calls now logged in GHL automatically
• n8n pulls call data for weekly reports
```

---

### Option C: Google Forwarding - Step by Step

```
Day 1 (5 minutes)
━━━━━━━━━━━━━━━━━
1. Google Ads → Campaign with Call Extension
2. Click Edit on Call Extension
3. Check "Use a Google forwarding number"
4. Save

5. Google Ads → Tools → Conversions
6. Create new conversion: "Phone Calls"
7. Select "Calls from ads"
8. Save

Ongoing
━━━━━━━
• Call count shows in Google Ads dashboard
• n8n pulls phone_calls metric from Google API
• Facebook/LSA calls NOT tracked (limitation)
```

---

### Option D: CallRail - Step by Step

```
Day 1 (1 hour)
━━━━━━━━━━━━━━
1. Sign up at callrail.com ($45/mo plan)
2. Add company/client account
3. Buy tracking number (included in plan)
4. Set destination → Client's business number

5. Create "Tracking Number Pool" for website
   - OR use single tracking number for ads

6. Integrations:
   - Connect Google Ads account
   - Connect Facebook Ads (manual attribution)
   - Connect GHL via Zapier/webhook

Day 1-2
━━━━━━━
7. Update Google Ads with CallRail number
8. Update Facebook Ads with CallRail number
9. Update website with dynamic number script

Ongoing
━━━━━━━
• All calls logged in CallRail with source
• Syncs to GHL via integration
• AI transcription available
• n8n can pull from CallRail API for reports
```

---

## My Recommendation

**Start with Option A (GHL Number)** for immediate tracking, then **port the business number (Option B)** if they want to keep their existing number long-term.

This gets us:
- Tracking TODAY with new GHL number
- Full migration to their number in 2 weeks
- $0-2/month total cost

---

## Decision Needed

1. **Which option do you want to go with?**
2. **Should we do this for Acton first as a pilot?**

---

*Let me know and I'll set it up.*
