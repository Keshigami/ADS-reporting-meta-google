# Directive: Pull GHL Opportunities with Revenue

## Goal

Pull opportunities from GoHighLevel, filter by pipeline stage, and calculate total revenue.

## Inputs

- `location_id`: GHL Location ID (from .env)
- `api_key`: GHL API Key (from .env)
- `stage_name`: Pipeline stage to filter (default: "Closed")

## Tools

- `execution/ghl_pull_opportunities.py`

## Outputs

- JSON file in `.tmp/opportunities_{date}.json`
- Console summary showing:
  - Total opportunities
  - Opportunities in target stage
  - Total monetary value
  - Average deal size

## Edge Cases

- No monetary value set: Log warning, count as $0
- API pagination: Handle via cursor

## Usage

```bash
python execution/ghl_pull_opportunities.py --stage "Closed"
```
