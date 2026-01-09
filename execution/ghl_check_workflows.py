"""
GHL Workflow Checker
List existing workflows to avoid duplicates
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

GHL_LOCATION_ID = os.getenv("GHL_LOCATION_ID")
GHL_API_KEY = os.getenv("GHL_API_KEY")
GHL_API_BASE = "https://services.leadconnectorhq.com"

def list_workflows():
    headers = {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Version": "2021-07-28",
        "Content-Type": "application/json"
    }
    
    url = f"{GHL_API_BASE}/workflows/"
    params = {
        "locationId": GHL_LOCATION_ID
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        workflows = data.get("workflows", [])
        
        print(f"\n📋 EXISTING WORKFLOWS (Total: {len(workflows)})")
        print("-" * 50)
        
        targets = ["google", "meta", "facebook", "ads", "roas", "attribution"]
        
        for wf in workflows:
            name = wf.get("name", "")
            status = wf.get("status", "draft")
            wf_id = wf.get("id", "")
            
            # Highlight relevant ones
            prefix = "  "
            if any(t in name.lower() for t in targets):
                prefix = "🔍"
            
            print(f"{prefix} {name} ({status})")
            
        print("-" * 50)
            
    except Exception as e:
        print(f"❌ Error listing workflows: {e}")

if __name__ == "__main__":
    list_workflows()
