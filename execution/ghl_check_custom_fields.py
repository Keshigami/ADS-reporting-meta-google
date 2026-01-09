"""
GHL Custom Fields Checker
Check if attribution fields exist
"""

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

GHL_LOCATION_ID = os.getenv("GHL_LOCATION_ID")
GHL_API_KEY = os.getenv("GHL_API_KEY")
GHL_API_BASE = "https://services.leadconnectorhq.com"

def check_custom_fields():
    headers = {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Version": "2021-07-28",
        "Content-Type": "application/json"
    }
    
    url = f"{GHL_API_BASE}/locations/{GHL_LOCATION_ID}/customFields"
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        fields = data.get("customFields", [])
        
        required_fields = ["gclid", "fbclid", "utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"]
        found = {field: False for field in required_fields}
        
        print(f"\n📋 CUSTOM FIELD CHECK (Total: {len(fields)})")
        print("-" * 40)
        
        for field in fields:
            name = field.get("name", "").lower()
            key = field.get("fieldKey", "")
            if name in found:
                found[name] = True
                print(f"✅ Found: {name} (Key: {key})")
        
        print("-" * 40)
        missing = [f for f, exists in found.items() if not exists]
        
        if missing:
            print(f"❌ MISSING FIELDS: {', '.join(missing)}")
            print("   Action required: Create these fields in Settings -> Custom Fields")
        else:
            print("✅ All attribution fields exist!")
            
    except Exception as e:
        print(f"❌ Error checking fields: {e}")

if __name__ == "__main__":
    check_custom_fields()
