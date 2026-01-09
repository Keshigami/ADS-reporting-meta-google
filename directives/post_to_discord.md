# Directive: Post to Discord

## Goal

Send formatted report to Discord channel via webhook.

## Inputs

- `webhook_url`: Discord webhook URL (from .env)
- `message`: Formatted report text

## Tools

- `execution/post_to_discord.py`

## Outputs

- Discord message posted
- Console confirmation with message ID

## Message Format

```
**WEEKLY ROAS REPORT** (Jan 1 - Jan 7)

**OVERALL**
Total Ad Spend: $1,247.50
Total Leads: 23
Revenue: $52,019
ROAS: 41.7x
CPL: $54.24

**BY CHANNEL**
| Channel  | Spend   | Leads | Calls | CPL    |
|----------|---------|-------|-------|--------|
| Meta     | $400.00 | 8     | 15    | $50.00 |
| Google   | $450.00 | 10    | 18    | $45.00 |
| LSA      | $397.50 | 5     | 12    | $79.50 |
```

## Usage

```bash
python execution/post_to_discord.py --report ".tmp/roas_report_2026-01-08.json"
```
