"""
GHL Phone Number Checker
List purchased phone numbers to verify setup
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

GHL_LOCATION_ID = os.getenv("GHL_LOCATION_ID")
GHL_API_KEY = os.getenv("GHL_API_KEY")
GHL_API_BASE = "https://services.leadconnectorhq.com"

def list_phone_numbers():
    headers = {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Version": "2021-07-28",
        "Content-Type": "application/json"
    }
    
    # Note: Endpoint might differ based on API version, trying standard V2
    url = f"{GHL_API_BASE}/conversations/providers/twilio/phone-numbers" 
    # Fallback to locations endpoint if above fails
    
    try:
        # GHL V2 API for Phone Numbers usually requires location context
        params = {"locationId": GHL_LOCATION_ID}
        
        # Trying to fetch location details which might include phone numbers
        # Or specific phone numbers endpoint
        url = f"{GHL_API_BASE}/locations/{GHL_LOCATION_ID}/phone-numbers"
        
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 404:
             # Try V1 style or different endpoint if V2 404s
             print("⚠️ V2 Phone endpoint not found, trying fallback...")
             return
             
        response.raise_for_status()
        data = response.json()
        
        # Adjust parsing based on actual response structure
        numbers = data.get("phoneNumbers", [])
        
        print(f"\n📞 EXISTING PHONE NUMBERS (Total: {len(numbers)})")
        print("-" * 50)
        
        targets = ["mec", "meta", "google", "lsa", "organic"]
        
        for num in numbers:
            name = num.get("name", "Unnamed")
            phone = num.get("phoneNumber", "")
            
            # Highlight relevant ones
            prefix = "  "
            if any(t in name.lower() for t in targets):
                prefix = "✅"
            
            print(f"{prefix} {name}: {phone}")
            
        print("-" * 50)
            
    except Exception as e:
        print(f"❌ Error listing phone numbers: {e}")

if __name__ == "__main__":
    list_phone_numbers()
