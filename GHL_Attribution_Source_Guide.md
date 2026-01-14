# Understanding Attribution Source

This guide explains how HighLevel categorizes traffic sources and provides the exact UTM templates needed for accurate reporting.

> **Source Article:** [Understanding Attribution Traffic Sources](https://help.gohighlevel.com/support/solutions/articles/48001219997-understanding-attribution-source)

---

## 1. What is Attribution?

Attribution tracks *where* a contact came from. This data is critical for knowing which ads or channels are driving revenue.

### First vs. Latest Attribution

Every contact has **two** attribution records:

* **First Attribution:** The *very first* time they interacted with you (e.g., visited website 6 months ago). **This never changes.**
* **Latest Attribution:** The *most recent* interaction (e.g., clicked a Facebook Ad yesterday). **This updates with every new interaction.**

> **Where to find it:** Open any Contact Record > Scroll to the bottom right > look for the **Attribution** card.

---

## 2. Types of Attribution Sources

HighLevel uses a set of rules to categorize traffic. Here are the definitions:

### 🟢 Paid Search (Google Ads)

Traffic from paid search engines like Google Ads.

* **Requirement:** Must match the Google UTM template.
* **Use for:** Google Ad Reporting.

**Google Ads UTM Template:**

```
{lpurl}?utm_source=adwords&utm_medium={adname}&utm_campaign={campaignname}&utm_content={adgroupname}&utm_keyword={keyword}&utm_matchtype={matchtype}&campaign_id={campaignid}&ad_group_id={adgroupid}&ad_id={creative}
```

### 🔵 Paid Social (Facebook/Instagram Ads)

Traffic from paid social campaigns.

* **Requirement:** Must match the Facebook UTM template.
* **Use for:** Facebook Ad Reporting.

**Facebook Ads UTM Template:**

```
{YourLandingPageUrl.com}?utm_source=fb_ad&utm_medium={{adset.name}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&campaign_id={{campaign.id}}
```

### 🟡 Organic Search

Traffic from non-paid search results (Google, Bing, Yahoo).

* **Trigger:** User clicks a search result link (not an ad).
* **Note:** Keywords are often "Unknown" because Google encrypts search terms for privacy.

### 🟣 Social Media (Organic)

Traffic from social platforms (Facebook, LinkedIn, Twitter) that is **not** a paid ad.

* **Trigger:** User clicks a link in a post, bio, or message.

### ⚫ Direct Traffic

Traffic with **no** source information.

* **Trigger:** User typed `yourwebsite.com` directly into the browser or used a bookmark.

### ⚪ Referrals

Traffic from other websites linking to you (e.g., a blog post on another site).

* **Trigger:** User clicks a link on an external domain.

### 🟠 CRM UI & Third-Party

* **CRM UI:** Lead was manually created inside HighLevel.
* **Third-Party:** Lead was created via API or Zapier.

---

## 3. How Attribution is Captured

**Critical Rule:** Attribution is ONLY captured when a contact submits a HighLevel entry point:

1. **Forms**
2. **Surveys**
3. **Calendars**
4. **Chat Widgets**
5. **Order Forms**

> **Warning:** If a user clicks an ad but *calls you* instead of filling a form, attribution will NOT be captured unless you use a **Number Pool** (Call Tracking).

---

## 4. Troubleshooting

**"Attribution is missing or wrong!"**

1. **Check the URL:** Does the landing page URL actually have the `?utm_...` parameters?
    * *Fix:* Check for redirects that strip parameters.
2. **Check the Form:** Is it a HighLevel form?
    * *Fix:* 3rd party forms need hidden fields to capture `gclid` or `utm` data manually.
3. **Check the Source:** Did you use the exact UTM templates above?
    * *Fix:* `utm_source=google` is NOT the same as `utm_source=adwords`. Use the templates exactly.
