"""
ROAS Calculator - Combine ad spend with GHL revenue
Per directive: directives/calculate_roas.md
"""

import os
import json
import argparse
import csv
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def parse_currency(value: str) -> float:
    """Parse currency string to float"""
    if not value:
        return 0.0
    # Remove $, commas, and % signs
    cleaned = str(value).replace("$", "").replace(",", "").replace("%", "").strip()
    try:
        return float(cleaned)
    except ValueError:
        return 0.0

def load_csv(filepath: str) -> list:
    """Load CSV file and return list of dicts"""
    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filepath}")
        return []
    
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_opportunities(filepath: str = None) -> dict:
    """Load opportunities from .tmp or use default"""
    if filepath and os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    
    # Try to find latest opportunities file
    tmp_dir = ".tmp"
    if os.path.exists(tmp_dir):
        files = [f for f in os.listdir(tmp_dir) if f.startswith("opportunities_")]
        if files:
            latest = sorted(files)[-1]
            with open(os.path.join(tmp_dir, latest), "r") as f:
                return json.load(f)
    
    return {"analysis": {"total_revenue": 0}}

def calculate_channel_metrics(campaigns: list, channel_name: str) -> dict:
    """Calculate metrics for a channel from campaign data"""
    
    total_spend = 0
    total_leads = 0
    total_clicks = 0
    total_impressions = 0
    
    for campaign in campaigns:
        total_spend += parse_currency(campaign.get("Cost", 0))
        total_leads += int(parse_currency(campaign.get("Leads", 0)))
        total_clicks += int(parse_currency(campaign.get("Clicks", 0)))
        impressions = campaign.get("Impressions", "0")
        total_impressions += int(parse_currency(str(impressions).replace(",", "")))
    
    cpl = round(total_spend / total_leads, 2) if total_leads > 0 else 0
    
    return {
        "channel": channel_name,
        "spend": round(total_spend, 2),
        "leads": total_leads,
        "clicks": total_clicks,
        "impressions": total_impressions,
        "cpl": cpl
    }

def calculate_roas(total_spend: float, total_revenue: float) -> float:
    """Calculate ROAS"""
    if total_spend == 0:
        print("⚠️  Warning: Total spend is $0, cannot calculate ROAS")
        return 0.0
    return round(total_revenue / total_spend, 2)

def main():
    parser = argparse.ArgumentParser(description="Calculate ROAS from CSV exports")
    parser.add_argument("--google", type=str, default="Google Ads Campaigns.csv")
    parser.add_argument("--meta", type=str, default="Facebook Campaigns (1).csv")
    parser.add_argument("--opportunities", type=str, default=None)
    args = parser.parse_args()
    
    print("\n📊 ROAS CALCULATION")
    print("=" * 50)
    
    # Load data
    google_campaigns = load_csv(args.google)
    meta_campaigns = load_csv(args.meta)
    opportunities_data = load_opportunities(args.opportunities)
    
    # Calculate channel metrics
    google_metrics = calculate_channel_metrics(google_campaigns, "Google Ads")
    meta_metrics = calculate_channel_metrics(meta_campaigns, "Meta Ads")
    
    # Get revenue from opportunities
    total_revenue = opportunities_data.get("analysis", {}).get("total_revenue", 0)
    
    # Calculate totals
    total_spend = google_metrics["spend"] + meta_metrics["spend"]
    total_leads = google_metrics["leads"] + meta_metrics["leads"]
    roas = calculate_roas(total_spend, total_revenue)
    overall_cpl = round(total_spend / total_leads, 2) if total_leads > 0 else 0
    
    # Print report
    print(f"\n📈 OVERALL METRICS")
    print(f"   Total Ad Spend: ${total_spend:,.2f}")
    print(f"   Total Leads: {total_leads}")
    print(f"   Total Revenue: ${total_revenue:,.2f}")
    print(f"   ROAS: {roas}x")
    print(f"   Overall CPL: ${overall_cpl:,.2f}")
    
    print(f"\n📊 BY CHANNEL")
    print(f"   {'Channel':<15} {'Spend':<12} {'Leads':<8} {'CPL':<10}")
    print(f"   {'-'*45}")
    print(f"   {'Meta Ads':<15} ${meta_metrics['spend']:<11,.2f} {meta_metrics['leads']:<8} ${meta_metrics['cpl']:,.2f}")
    print(f"   {'Google Ads':<15} ${google_metrics['spend']:<11,.2f} {google_metrics['leads']:<8} ${google_metrics['cpl']:,.2f}")
    
    # Save report
    report = {
        "generated_at": datetime.now().isoformat(),
        "overall": {
            "total_spend": total_spend,
            "total_leads": total_leads,
            "total_revenue": total_revenue,
            "roas": roas,
            "cpl": overall_cpl
        },
        "channels": {
            "meta": meta_metrics,
            "google": google_metrics
        }
    }
    
    os.makedirs(".tmp", exist_ok=True)
    filepath = f".tmp/roas_report_{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(filepath, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\n💾 Report saved to {filepath}")

if __name__ == "__main__":
    main()
