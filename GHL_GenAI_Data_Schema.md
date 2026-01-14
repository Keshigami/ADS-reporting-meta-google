# GHL Gen AI Data Schema & Prompt Protocol

**Purpose:** This document establishes the strict data structure required to "feed" any Generative AI agent (ChatGPT, Claude, Custom GHL Bot) so it can autonomously write the "Monday Morning Win" emails.

---

## 1. The Standard Data Payload (JSON)

Any AI agent you build must accept this exact JSON structure as input. This ensures the "Foundation" we built in the Tracking Guide translates perfectly to AI analysis.

```json
{
  "client_info": {
    "name": "Banner Mountain Media",
    "industry": "Real Estate Marketing",
    "cycle_stage": "Scaling"
  },
  "reporting_period": {
    "start_date": "2026-07-14",
    "end_date": "2026-07-21"
  },
  "metrics": {
    "total_spend": 450.00,
    "total_leads": 24,
    "cost_per_lead": 18.75,
    "revenue_pipeline": 12000.00,
    "sales_velocity": 850.00
  },
  "lead_interaction_insights": {
    "avg_response_time_minutes": 12,
    "response_time_grade": "A",
    "lead_sentiment_score": 8.5,
    "sentiment_summary": "Most leads are asking about pricing immediately, indicating high intent.",
    "top_objection": "Availability on weekends",
    "ai_recommendation": "Update auto-responder to mention 'Weekend Emergency Service Available' to boost conversion."
  },
  "channel_performance": {
    "google": {
      "spend": 300.00,
      "leads": 10,
      "cpl": 30.00,
      "top_keyword": "real estate video production"
    },
    "facebook": {
      "spend": 150.00,
      "leads": 14,
      "cpl": 10.71,
      "top_creative": "Video_Strategy_V2.mp4"
    }
  },
  "previous_period_comparison": {
    "leads_change_percent": 12.5,
    "cpl_change_percent": -5.0
  }
}
```

---

## 2. The "Strategy Note" Prompt

This is the exact prompt to send to your LLM along with the JSON above to generate the **"Strategy Note"** for the email.

**System Role:**
> You are a concise, high-level Marketing Strategist for Banner Mountain Media. Your tone is Professional, Enthusiastic, and Strategic.

**User Prompt:**
> Analyze the provided JSON data. Write a 2-sentence "Strategy Note" for the client.
>
> **Rules:**
>
> 1. Highlight the biggest "Win" (e.g., low CPL, high volume, or specific channel success).
> 2. State ONE specific action we are taking next week based on this data (e.g., shifting budget, launching new creative).
> 3. Do NOT simply recap the numbers; interpret them.
> 4. Max 40 words.

**Example Output:**
> "Facebook Video ads are driving leads at $10.71 (60% cheaper than Google). We are shifting $100 of the Google budget to Facebook next week to maximize this efficiency."

---

## 3. Automation Workflow Logic

To automate the entire "Monday Morning Win":

1. **Trigger:** Weekly Schedule (Monday 8:00 AM).
2. **Action 1 (Data Fetch):** Webhook/API pulls metrics from GHL Reporting -> formats into `JSON`.
3. **Action 2 (AI Analysis):** Send `JSON` + `Prompt` to OpenAI/Claude API.
4. **Action 3 (Email Gen):** GHL Email Builder populates:
    * `{{custom_values.leads}}`
    * `{{custom_values.spend}}`
    * `{{custom_values.ai_strategy_note}}` (Result from Action 2).
5. **Action 4 (Send):** Email sent to Client.

---

## 4. Why This Matters

By "establishing" this Schema now:

* **You replace yourself:** You don't write reports; you just approve them.
* **Zero Hallucinations:** The AI is constrained by strict JSON data.
* **Scalability:** This works for 1 client or 1,000 clients without changing the code.
