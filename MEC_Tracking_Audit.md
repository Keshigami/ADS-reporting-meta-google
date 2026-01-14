# MEC Tracking Audit Checklist

**Client:** MEC (Mountain Entertainment Company / MEC Builds)  
**Date:** January 2026  
**Purpose:** Verify Phase 5 tracking is complete

---

## 🔌 1. Platform Connections

**Path:** `Settings > Integrations`

| Platform | Status | Notes |
|----------|:------:|-------|
| Google Ads Connected | [ ] | Green checkmark visible |
| Google Ads Account Selected | [ ] | Correct account in Reporting |
| Meta (Facebook) Connected | [ ] | Green checkmark visible |
| Meta Ad Account Selected | [ ] | Correct account in Reporting |

---

## 📊 2. UTM Custom Fields

**Path:** `Settings > Custom Fields > Contact`

| Field | Created | Hidden on Forms |
|-------|:-------:|:---------------:|
| utm_source | [ ] | [ ] |
| utm_medium | [ ] | [ ] |
| utm_campaign | [ ] | [ ] |
| utm_content | [ ] | [ ] |
| utm_term | [ ] | [ ] |
| gclid | [ ] | [ ] |
| fbclid | [ ] | [ ] |

---

## 📝 3. Google Ads Configuration

**3.1 Tracking Template**
**Path:** Google Ads > Account Settings > Tracking

- [ ] Tracking template installed:

```
{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignname}&utm_content={adgroupname}&utm_term={keyword}&campaign_id={campaignid}&ad_group_id={adgroupid}&ad_id={creative}
```

**3.2 Auto-Tagging**
**Path:** Google Ads > Settings > Account Settings

- [ ] Auto-tagging enabled (appends GCLID automatically)

---

## 📘 4. Meta Ads Configuration

**4.1 UTM Parameters**
**Path:** Ads Manager > Ad Level > URL Parameters

- [ ] UTM parameters added to all active ads:

```
utm_source=facebook&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}
```

**4.2 Pixel/CAPI**

- [ ] Meta Pixel ID stored in custom values
- [ ] Access Token stored in custom values
- [ ] Pixel installed on funnels (head tracking)

---

## 📞 5. Call Tracking Numbers

**Path:** `Settings > Phone Numbers`

| Number Name | Purchased | Forwarding Set | Used In |
|-------------|:---------:|:--------------:|---------|
| MEC-GOOGLE | [ ] | [ ] | Google Ad Extensions |
| MEC-META | [ ] | [ ] | Meta Ad Creatives |
| MEC-LSA | [ ] | [ ] | Local Service Ads |
| MEC-ORGANIC | [ ] | [ ] | Website, GMB |

**Number Pool (Optional):**

| Component | Status |
|-----------|:------:|
| Number Pool created (4+ numbers) | [ ] |
| Swap script in Footer Tracking | [ ] |
| Dynamic swapping verified | [ ] |

---

## ⚙️ 6. ROAS Workflows

**Path:** `Automation > Workflows`

| Workflow Name | Exists | Published | Tested |
|---------------|:------:|:---------:|:------:|
| Google Ads - Track Lead | [ ] | [ ] | [ ] |
| Google Ads - Track Closed Won | [ ] | [ ] | [ ] |
| Meta Ads - Track Lead | [ ] | [ ] | [ ] |
| Meta Ads - Track Purchase | [ ] | [ ] | [ ] |

---

## 🧪 7. Live Test

### 7.1 Form Submission Test

1. [ ] Open funnel with test UTMs:

   ```
   ?utm_source=test&utm_medium=audit&utm_campaign=mec_tracking_test&gclid=TEST123&fbclid=TESTFB456
   ```

2. [ ] Submit form
3. [ ] Check contact record:
   - [ ] utm_source = test
   - [ ] utm_campaign = mec_tracking_test
   - [ ] gclid = TEST123
   - [ ] fbclid = TESTFB456

### 7.2 Call Tracking Test

- [ ] Call MEC-GOOGLE number → Appears in Call Report
- [ ] Call MEC-META number → Appears in Call Report
- [ ] Calls forwarded to business phone correctly

### 7.3 ROAS Workflow Test

1. [ ] Create test opportunity ($100 value)
2. [ ] Move to Closed Won
3. [ ] Check Automation > Logs → Workflows executed
4. [ ] Delete test contact after verification

---

## 🚨 Issues Found

| Issue | Severity | Fix Required |
|-------|----------|--------------|
| | | |
| | | |
| | | |

---

## ✅ Sign-Off

| Auditor | Date | Status |
|---------|------|--------|
| | | [ ] Complete [ ] Needs Work |

---

## Next Steps

- [ ] Fix any issues found above
- [ ] Re-test after fixes
- [ ] Update `GHL_Subaccount_Call_Tracking_Setup.md` with MEC numbers
