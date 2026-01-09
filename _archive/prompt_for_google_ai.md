# Prompt for Google Gemini / Advanced AI

**Instructions:** Copy and paste the text below into the AI chat interface.

---

**Role:** You are an expert in n8n automation and JavaScript.

**Task:** Create a consolidated, linear n8n workflow JSON that generates a "Weekly ROAS Report" by pulling data from Google Ads, Meta Ads, and GoHighLevel, processing it, and sending a summary to Discord.

**Workflow Architecture:**

1. **Trigger:** Schedule Trigger (Weekly, Monday 9am) AND Manual Webhook Trigger.
2. **Date Config:** Set `start_date` (7 days ago) and `end_date` (yesterday) using Luxon/n8n expressions.
3. **Data Fetching (Parallel):**
    * **Google Ads (HTTP Request):**
        * URL: `https://googleads.googleapis.com/v14/customers/3300525230/googleAds:searchStream`
        * Method: POST
        * Auth: Predefined `googleAdsOAuth2Api`
        * Query: `SELECT campaign.id, campaign.name, metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions, metrics.conversions_value FROM campaign WHERE segments.date BETWEEN '${start_date}' AND '${end_date}'`
    * **Meta Ads (HTTP Request):**
        * URL: `https://graph.facebook.com/v19.0/act_54337533/insights`
        * Method: GET
        * Auth: Predefined `facebookGraphApi` (ID: `z8gP5ZZAbWdJ6ONT`)
        * Query Params: `level=campaign`, `fields=spend,clicks,actions,action_values`, `time_range={'since':'${start_date}','until':'${end_date}'}`
    * **GoHighLevel (HTTP Request):**
        * URL: `https://services.leadconnectorhq.com/opportunities/search`
        * Auth: Header Auth (Name: `GHL API Key`, Value: `pit-da630dfd-7851-468f-b86e-0cbc9b8e4399`)
        * Query Params: `locationId=FrSOvqFDYNjesCMYVuAc`, `status=won`
4. **Merge:** Merge all three branches into one execution stream (Multiplex/Combine).
5. **Data Processing (Code Node):**
    * Iterate through Google results (convert `cost_micros` / 1,000,000 to get spend).
    * Iterate through Meta results (sum spend, filter actions for `type='lead'` to get leads, filter action_values for `type='purchase'` to get revenue).
    * Iterate through GHL opportunities (sum `monetaryValue` for total revenue).
    * **Calculate:**
        * `Total Spend` = Google Spend + Meta Spend
        * `Total Leads` = Google Conversions + Meta Leads
        * `Real Revenue` = GHL Won Opportunity Value
        * `ROAS` = Real Revenue / Total Spend
        * `CPL` = Total Spend / Total Leads
        * `Google CPL` = Google Spend / Google Conversions
        * `Meta CPL` = Meta Spend / Meta Leads
    * **Output JSON:** A simplified object with `overall`, `google`, and `meta` stats.
6. **Notification (Discord):**
    * Webhook/Bot Credential: `Discord Webhook`
    * Channel ID: `1423013870456274944`
    * Message Content: A markdown table/summary showing Spend, Leads, Revenue, ROAS, and CPL for Overall, Google, and Meta.
    * Example Output:

        ```
        **WEEKLY ROAS REPORT**
        Total Spend: $1,247.50
        Revenue: $52,019
        ROAS: 41.7x
        ```

**Output Requirement:** Provide ONLY the valid JSON code for the n8n workflow. Do not wrap it in markdown code blocks if possible, or verify that the JSON is copy-paste ready for n8n.
