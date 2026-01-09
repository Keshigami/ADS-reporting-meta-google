"""
GHL Opportunities Puller - Pull opportunities with revenue data
Per directive: directives/pull_ghl_opportunities.md
"""

import os
import json
import argparse
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

# Config from .env
GHL_LOCATION_ID = os.getenv("GHL_LOCATION_ID", "FrSOvqFDYNjesCMYVuAc")
GHL_API_KEY = os.getenv("GHL_API_KEY", "pit-da630dfd-7851-468f-b86e-0cbc9b8e4399")
GHL_API_BASE = "https://services.leadconnectorhq.com"

def pull_opportunities(stage_name: str = None) -> dict:
    """Pull opportunities from GHL API"""
    
    headers = {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Version": "2021-07-28",
        "Content-Type": "application/json"
    }
    
    url = f"{GHL_API_BASE}/opportunities/"
    params = {
        "locationId": GHL_LOCATION_ID,
        "limit": 100
    }
    
    if stage_name:
        params["status"] = stage_name
    
    all_opportunities = []
    cursor = None
    
    while True:
        if cursor:
            params["startAfter"] = cursor
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            opportunities = data.get("opportunities", [])
            all_opportunities.extend(opportunities)
            
            # Check for pagination
            meta = data.get("meta", {})
            if meta.get("nextPageToken"):
                cursor = meta["nextPageToken"]
            else:
                break
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error pulling opportunities: {e}")
            return {"opportunities": all_opportunities, "error": str(e)}
    
    return {"opportunities": all_opportunities}

def analyze_opportunities(opportunities: list, target_stage: str = "Closed") -> dict:
    """Analyze opportunities and calculate revenue"""
    
    total = len(opportunities)
    in_stage = 0
    total_revenue = 0
    with_value = 0
    without_value = 0
    
    for opp in opportunities:
        stage = opp.get("pipelineStageId", "") or opp.get("stage", "")
        value = opp.get("monetaryValue", 0) or 0
        
        # Check if in target stage (flexible matching)
        if target_stage.lower() in stage.lower() or opp.get("status", "").lower() == "won":
            in_stage += 1
            if value > 0:
                total_revenue += value
                with_value += 1
            else:
                without_value += 1
    
    avg_deal = round(total_revenue / with_value, 2) if with_value > 0 else 0
    
    return {
        "total": total,
        "in_target_stage": in_stage,
        "with_value": with_value,
        "without_value": without_value,
        "total_revenue": total_revenue,
        "average_deal_size": avg_deal
    }

def save_to_file(data: dict, filename: str):
    """Save data to .tmp directory"""
    os.makedirs(".tmp", exist_ok=True)
    filepath = os.path.join(".tmp", filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"💾 Saved to {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Pull GHL opportunities with revenue")
    parser.add_argument("--stage", type=str, default="Closed", help="Stage to filter")
    args = parser.parse_args()
    
    print(f"\n🔄 Pulling opportunities...")
    print(f"   Location ID: {GHL_LOCATION_ID}")
    print(f"   Target Stage: {args.stage}")
    
    # Pull opportunities
    result = pull_opportunities()
    opportunities = result.get("opportunities", [])
    
    if result.get("error"):
        print(f"⚠️  API Error: {result['error']}")
    
    # Analyze
    analysis = analyze_opportunities(opportunities, args.stage)
    
    # Print summary
    print(f"\n💰 OPPORTUNITY REVENUE SUMMARY")
    print(f"   Total Opportunities: {analysis['total']}")
    print(f"   In '{args.stage}' Stage: {analysis['in_target_stage']}")
    print(f"   With Monetary Value: {analysis['with_value']}")
    print(f"   Without Value: {analysis['without_value']}")
    print(f"   Total Revenue: ${analysis['total_revenue']:,.2f}")
    print(f"   Average Deal Size: ${analysis['average_deal_size']:,.2f}")
    
    if analysis['without_value'] > 0:
        print(f"\n   ⚠️  WARNING: {analysis['without_value']} closed deals have no monetary value!")
    
    # Save to file
    output = {
        "pulled_at": datetime.now().isoformat(),
        "target_stage": args.stage,
        "analysis": analysis,
        "opportunities": opportunities
    }
    save_to_file(output, f"opportunities_{datetime.now().strftime('%Y-%m-%d')}.json")

if __name__ == "__main__":
    main()
