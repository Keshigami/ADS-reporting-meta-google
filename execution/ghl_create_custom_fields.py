"""
GHL Custom Fields Creator
Create missing attribution fields
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

GHL_LOCATION_ID = os.getenv("GHL_LOCATION_ID")
GHL_API_KEY = os.getenv("GHL_API_KEY")
GHL_API_BASE = "https://services.leadconnectorhq.com"

def create_custom_field(name):
    headers = {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Version": "2021-07-28",
        "Content-Type": "application/json"
    }
    
    url = f"{GHL_API_BASE}/locations/{GHL_LOCATION_ID}/customFields"
    
    payload = {
        "name": name,
        "dataType": "TEXT",
        "placeholder": name,
        "model": "contact"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code in [200, 201]:
            print(f"✅ Created: {name}")
            return True
        else:
            print(f"❌ Failed to create {name}: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error creating {name}: {e}")
        return False

def main():
    fields_to_create = [
        "gclid", 
        "fbclid", 
        "utm_source", 
        "utm_medium", 
        "utm_campaign", 
        "utm_content", 
        "utm_term"
    ]
    
    print("\n🛠️ CREATING MISSING FIELDS")
    print("-" * 40)
    
    count = 0
    for field in fields_to_create:
        if create_custom_field(field):
            count += 1
            
    print("-" * 40)
    print(f"🎉 Created {count} fields.")

if __name__ == "__main__":
    main()
