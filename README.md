# GHL Ad Manager & ROAS Attribution System

System for tracking, attributing, and reporting Real ROAS (Return on Ad Spend) for MEC and agency clients using GoHighLevel.

## 🎯 Objective

Enable "Fortune 500" level reporting by linking GHL "Closed Won" revenue back to Google/Meta Ads via Offline Conversions.

## 📂 Project Structure

### 📄 Core Documentation

- **`GHL_Ad_Manager_ROAS_Setup.md`** - The Master Guide for setting up attribution.
- **`Agency_Scaling_Strategy.md`** - Roadmap to "Top 10" status via AI & Reporting.
- **`Attribution_Video_Analysis.md`** - Technical decision log (Native vs. GTM).
- **`MEC_Workflow_Instructions.md`** - Step-by-step for current MEC implementation.

### 🤖 Automation (3-Layer Architecture)

The system uses a "Directives" and "Execution" model:

- **`/directives`** - Standard Operating Procedures (SOPs) in Markdown.
  - `pull_ghl_contacts.md`
  - `calculate_roas.md`
  - `post_to_discord.md`

- **`/execution`** - Python scripts that do the work.
  - `ghl_pull_contacts.py` - Fetches data & checks attribution.
  - `ghl_create_custom_fields.py` - Automates field creation.
  - `calculate_roas.py` - Merges Ad Spend + GHL Revenue.

### 🗄️ Archive

- **`/_archive`** - Contains old research, n8n JSONs, and superseded guides.

## 🚀 Quick Start

1. **Check Task List:** See `task.md` for current progress.
2. **Environment:** Ensure `.env` is configured with MEC credentials.
3. **Run Reports:**

    ```bash
    python execution/calculate_roas.py
    ```

## 🛠️ Current Status (MEC Pilot)

- Integrations: ✅ Verified
- Custom Fields: ✅ Created
- Workflows: 🚧 In Progress (Manual Creation)
- Phone Numbers: 🚧 Pending Purchase
