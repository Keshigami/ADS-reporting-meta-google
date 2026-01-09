# Directive: Calculate ROAS Report

## Goal

Combine ad spend data with GHL revenue to calculate ROAS and generate a weekly report.

## Inputs

- Google Ads CSV export (from GHL Ad Manager)
- Meta Ads CSV export (from GHL Ad Manager)
- GHL opportunities data (from pull_ghl_opportunities.py)

## Tools

- `execution/calculate_roas.py`

## Outputs

- `.tmp/roas_report_{date}.json` - Raw data
- Console formatted report with:
  - Total Spend (Google + Meta + LSA)
  - Total Revenue (from closed opportunities)
  - ROAS = Revenue / Spend
  - CPL = Spend / Leads
  - Breakdown by channel

## Formula

```
ROAS = Total Revenue / Total Ad Spend
CPL = Total Spend / Total Leads
```

## Edge Cases

- Division by zero: Return 0.00 with warning
- Missing data: Use defaults, log warning

## Usage

```bash
python execution/calculate_roas.py --google "Google Ads Campaigns.csv" --meta "Facebook Campaigns (1).csv"
```
