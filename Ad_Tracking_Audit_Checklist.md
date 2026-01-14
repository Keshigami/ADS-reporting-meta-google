# Ad Tracking & Attribution Audit Checklist

**Objective:** Ensure every dollar spent is tracked, attributed, and reported in GoHighLevel (GHL).

---

## 🟥 1. Google Ads (Search, Display, PMax)

*Why it matters: If this is wrong, GHL sees clicks but doesn't know they are from ads.*

- [ ] **1.1 Check Tracking Template (Account Level)**
  - **Go to:** Google Ads > Settings > Account Settings > Tracking.
  - **Required Value:** `{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={adgroupid}&utm_term={keyword}`
  - **Status:** [ ] Verified / [ ] Missing
- [ ] **1.2 Verify Auto-Tagging**
  - **Go to:** Google Ads > Settings > Account Settings > Auto-tagging.
  - **Required Status:** Checked (ON).
  - **Status:** [ ] On / [ ] Off
- [ ] **1.3 Check Conversion Actions**
  - **Go to:** Google Ads > Goals > Conversions.
  - **Verify:** Are there "Imported" conversions from GHL (e.g., "GHL Lead")?
  - **Status:** [ ] Connected / [ ] Missing

---

## 🟦 2. Google Local Services Ads (LSA)

*Why it matters: LSA doesn't use URLs, so it needs special handling for Calls and Bookings.*

- [ ] **2.1 Audit Phone Tracking (The "Call Trap")**
  - **Go to:** LSA Dashboard > Profile & Budget > Phone Number.
  - **Verify:** Is the "Forwarding Number" set to a **GHL Tracking Number**? (Not the client's cell).
  - **Status:** [ ] GHL Number / [ ] Client Cell (Untracked)
- [ ] **2.2 Audit "Reserve with Google" (The "Booking Trap")**
  - **Go to:** GHL > Settings > Integrations.
  - **Verify:** Is "Reserve with Google" Connected?
  - **Status:** [ ] Connected / [ ] Disconnected

---

## 🟩 3. GoHighLevel (GHL) Settings

*Why it matters: This determines how GHL credits the sale.*

- [ ] **3.1 Attribution Settings**
  - **Go to:** GHL > Settings > Attribution.
  - **Recommended:** "First Click" (for Lead Gen) or "All" (for comprehensive view).
  - **Status:** [ ] Verified
- [ ] **3.2 Google Analytics Connection**
  - **Go to:** GHL > Settings > Integrations.
  - **Verify:** Is the GA4 Account connected for this sub-account?
  - **Status:** [ ] Connected / [ ] Disconnected

---

## 🟨 4. Meta Ads (Future Readiness)

*Even if paused, ensure the infrastructure is ready.*

- [ ] **4.1 Meta Pixel & CAPI**
  - **Go to:** GHL > Sites > Settings > Head Tracking Code.
  - **Verify:** is the Base Pixel Code installed?
  - **Status:** [ ] Installed / [ ] Missing
- [ ] **4.2 Facebook URL Parameters**
  - **Action:** Ensure all future ads use the UTM string: `utm_source=fb_ads&utm_medium=cpc&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`
