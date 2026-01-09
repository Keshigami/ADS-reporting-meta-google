"""
GHL Contact Puller - Pull contacts with attribution data
Per directive: directives/pull_ghl_contacts.md
"""

import os
import json
import argparse
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv

load_dotenv()

# Config from .env
GHL_LOCATION_ID = os.getenv("GHL_LOCATION_ID", "FrSOvqFDYNjesCMYVuAc")
GHL_API_KEY = os.getenv("GHL_API_KEY", "pit-da630dfd-7851-468f-b86e-0cbc9b8e4399")
GHL_API_BASE = "https://services.leadconnectorhq.com"

def pull_contacts(days_back: int = 7) -> dict:
    """Pull contacts from GHL API"""
    
    headers = {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Version": "2021-07-28",
        "Content-Type": "application/json"
    }
    
    # Calculate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)
    
    url = f"{GHL_API_BASE}/contacts/"
    params = {
        "locationId": GHL_LOCATION_ID,
        "limit": 20
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        if response.status_code != 200:
            print(f"❌ API Error {response.status_code}: {response.text}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error pulling contacts: {e}")
        return {"contacts": [], "error": str(e)}

def analyze_attribution(contacts: list) -> dict:
    """Analyze attribution data on contacts"""
    
    total = len(contacts)
    with_gclid = 0
    with_fbclid = 0
    with_utm = 0
    no_attribution = 0
    
    for contact in contacts:
        has_gclid = bool(contact.get("gclid") or contact.get("googleClickId"))
        has_fbclid = bool(contact.get("fbclid") or contact.get("facebookClickId"))
        has_utm = bool(contact.get("source") or contact.get("utmSource"))
        
        if has_gclid:
            with_gclid += 1
        if has_fbclid:
            with_fbclid += 1
        if has_utm:
            with_utm += 1
        if not (has_gclid or has_fbclid or has_utm):
            no_attribution += 1
    
    return {
        "total": total,
        "with_gclid": with_gclid,
        "with_fbclid": with_fbclid,
        "with_utm": with_utm,
        "no_attribution": no_attribution,
        "attribution_rate": round((total - no_attribution) / total * 100, 1) if total > 0 else 0
    }

def save_to_file(data: dict, filename: str):
    """Save data to .tmp directory"""
    os.makedirs(".tmp", exist_ok=True)
    filepath = os.path.join(".tmp", filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"💾 Saved to {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Pull GHL contacts with attribution")
    parser.add_argument("--days", type=int, default=7, help="Days to look back")
    args = parser.parse_args()
    
    print(f"\n🔄 Pulling contacts from last {args.days} days...")
    print(f"   Location ID: {GHL_LOCATION_ID}")
    
    # Pull contacts
    result = pull_contacts(args.days)
    contacts = result.get("contacts", [])
    
    if result.get("error"):
        print(f"⚠️  API Error: {result['error']}")
        return
    
    # Analyze attribution
    analysis = analyze_attribution(contacts)
    
    # Print summary
    print(f"\n📊 CONTACT ATTRIBUTION SUMMARY")
    print(f"   Total Contacts: {analysis['total']}")
    print(f"   With GCLID (Google): {analysis['with_gclid']}")
    print(f"   With FBCLID (Meta): {analysis['with_fbclid']}")
    print(f"   With UTM Source: {analysis['with_utm']}")
    print(f"   No Attribution: {analysis['no_attribution']}")
    print(f"   Attribution Rate: {analysis['attribution_rate']}%")
    
    # Save to file
    output = {
        "pulled_at": datetime.now().isoformat(),
        "days_back": args.days,
        "analysis": analysis,
        "contacts": contacts
    }
    save_to_file(output, f"contacts_{datetime.now().strftime('%Y-%m-%d')}.json")

if __name__ == "__main__":
    main()
