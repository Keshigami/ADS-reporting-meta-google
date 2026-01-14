# Google Ads Reporting Guide

This comprehensive guide covers the setup, terminology, GA4 integration, and troubleshooting for Google Ads Reporting in GoHighLevel.

---

## Part 1: Google Ads Reporting Setup

*Source: [How to set up Google Ad Reporting](https://help.gohighlevel.com/support/solutions/articles/48001219312-how-to-set-up-google-ad-reporting)*

To see live analysis of your ad campaigns directly in the dashboard, follow these steps.

### Step 1: Connect Google Ad Account

1. Go to **Settings > Integrations**.
2. Connect your Google Account.
3. **Requirements**: The connected Gmail address must have **Admin** or **Standard** access to the Google Ads account. It cannot be a Manager (MCC) account login only; it must be a user in the ad account itself.

### Step 2: Configure Reporting Settings

1. Go to **Reporting > Google Ads**.
2. If applicable, select the correct **MCC Account ID** (Manager Account).
3. Select the **Client Account ID** (The specific ad account you want to report on).

### Step 3: Add UTM Tracking Template (CRITICAL)

For GHL to track leads and attribute them back to specific ads, you must add the Tracking Template in Google Ads.

**The Template:**

```
{lpurl}?utm_source=adwords&utm_medium={adname}&utm_campaign={campaignname}&utm_content={adgroupname}&utm_keyword={keyword}&utm_matchtype={matchtype}&campaign_id={campaignid}&ad_group_id={adgroupid}&ad_id={creative}
```

**Where to Add It:**

1. In Google Ads, go to **Account Settings** (Recommended).
2. Find **Tracking**.
3. Paste the template into the "Tracking template" field.
4. Click **Test** to verify your landing pages are found.
5. Click **Save**.

---

## Part 2: Google Analytics 4 (GA4) Tracking

*Source: [Google Analytics 4 Tracking](https://help.gohighlevel.com/support/solutions/articles/48001234199-google-analytics-4-tracking)*

You can also send conversion events from GHL workflows directly to GA4.

### Step 1: Get Your GA4 Credentials

1. Go to Google Analytics Admin.
2. **Data Streams**: Copy your **Measurement ID** (e.g., `G-XXXXXXXX`).
3. **API Secrets**: Go to **Measurement Protocol API secrets**. Create a new secret and copy the **Secret Value** (e.g., `SPhmkV...`).

### Step 2: Create the Workflow Action

1. In GHL, create a workflow (e.g., Trigger: Opportunity Status Changed to Won).
2. Add Action: **Add to Google Analytics**.
3. Action Type: Select **Google Analytics 4**.
4. **Measurement ID**: Paste your ID.
5. **API Secret**: Paste your Secret Value.
6. **Event Name**: Enter a name (e.g., `purchase`, `generate_lead`). *Follow [Google's event naming rules](https://support.google.com/analytics/answer/13316687?hl=en).*

---

## Part 3: Understanding Google Ad Reporting Terminology

*Source: [Understanding Google Ad Reporting Terminology](https://help.gohighlevel.com/support/solutions/articles/48001219241-understanding-google-ad-reporting-terminology)*

| Term | Definition |
| :--- | :--- |
| **Impressions** | Number of times your ad was shown on the Google Network. |
| **Clicks** | Number of times someone clicked your ad (headline, phone number, etc). |
| **Conversions** | A valuable action completed by a user (e.g., form submit, purchase, call). Defined in Google Ads. |
| **Client Spend** | Cost of running the ad + management fees (Visible to Agency Admins). |
| **Average CPC** | **Cost Per Click**. The average amount paid for each click. (Total Cost / Clicks). |
| **CPA** | **Cost Per Acquisition** (or Cost Per Conversion). Average cost to acquire one customer. (Total Cost / Conversions). |
| **Conversion Rate** | Percentage of clicks that resulted in a conversion. (Conversions / Clicks). |
| **Revenue** | Sum total of the **Monetary Value** of all opportunities marked as "Won" attributed to the Google Ad campaign. |
| **ROI** | **Return On Investment**. (Revenue - Cost) / Cost. |
| **Leads** | Number of opportunities created (Open status) from the ads. |
| **CPL** | **Cost Per Lead**. Cost of the campaign divided by the number of Leads (Open opportunities). |

---

## Part 4: Troubleshooting Guide

*Source: [Troubleshoot Guide For Google Ad Reporting](https://help.gohighlevel.com/support/solutions/articles/48001219996-troubleshoot-guide-for-google-ad-reporting)*

### Issue 1: Integration not working

* **Check**: Does the connected Gmail address have **Admin** access in Google Ads?
* **Check**: Is the user role in Google Ads a normal User, not just a Manager (MCC) login?

### Issue 2: Attribution failing or Duplicates

* **Check**: Is the UTM Tracking Template added in multiple places?
  * *Correct*: Add it ONLY at the **Account Level**.
  * *Incorrect*: Adding it at Campaign + Ad Group + Ad level causes conflicts.
* **Check**: Are you using unique names?
  * **Rule**: Campaign, Ad Set, and Ad names must be **unique**.
  * *Bad Example*: Two campaigns both named "Winter Sale".
  * *Result*: Data will merge or show as duplicates in reports.

### Issue 3: Changing Names

* **Warning**: If you rename a campaign/ad in Google Ads, the old UTM parameters don't disappear.
* **Best Practice**: Create a **new** campaign/ad instead of renaming an old one to ensure clean data attribution.

### Issue 4: Case Sensitivity

* **Rule**: UTM parameters are case-sensitive. `utm_source=google` is different from `utm_source=Google`.
* **GHL Requirement**: Use the exact tracking template provided above (lowercase).

---
