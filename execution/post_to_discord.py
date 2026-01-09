"""
Discord Poster - Send reports to Discord webhook
Per directive: directives/post_to_discord.md
"""

import os
import json
import argparse
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")

def load_report(filepath: str) -> dict:
    """Load report from JSON file"""
    if not os.path.exists(filepath):
        print(f"❌ Report file not found: {filepath}")
        return None
    
    with open(filepath, "r") as f:
        return json.load(f)

def format_report(report: dict) -> str:
    """Format report for Discord"""
    
    overall = report.get("overall", {})
    channels = report.get("channels", {})
    
    # Build message
    lines = [
        "**📊 WEEKLY ROAS REPORT**",
        f"Generated: {datetime.now().strftime('%B %d, %Y')}",
        "",
        "**OVERALL PERFORMANCE**",
        f"• Total Ad Spend: ${overall.get('total_spend', 0):,.2f}",
        f"• Total Leads: {overall.get('total_leads', 0)}",
        f"• Total Revenue: ${overall.get('total_revenue', 0):,.2f}",
        f"• **ROAS: {overall.get('roas', 0)}x**",
        f"• CPL: ${overall.get('cpl', 0):,.2f}",
        "",
        "**BY CHANNEL**",
        "```",
        f"{'Channel':<12} {'Spend':<10} {'Leads':<6} {'CPL':<8}",
        f"{'-'*40}",
    ]
    
    meta = channels.get("meta", {})
    google = channels.get("google", {})
    
    lines.append(f"{'Meta':<12} ${meta.get('spend', 0):<9,.0f} {meta.get('leads', 0):<6} ${meta.get('cpl', 0):,.2f}")
    lines.append(f"{'Google':<12} ${google.get('spend', 0):<9,.0f} {google.get('leads', 0):<6} ${google.get('cpl', 0):,.2f}")
    lines.append("```")
    
    return "\n".join(lines)

def post_to_discord(message: str) -> bool:
    """Post message to Discord webhook"""
    
    if not DISCORD_WEBHOOK_URL:
        print("❌ DISCORD_WEBHOOK_URL not set in .env")
        return False
    
    payload = {
        "content": message,
        "username": "ROAS Bot"
    }
    
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=10)
        response.raise_for_status()
        print("✅ Posted to Discord successfully!")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to post to Discord: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Post ROAS report to Discord")
    parser.add_argument("--report", type=str, required=True, help="Path to report JSON")
    parser.add_argument("--dry-run", action="store_true", help="Print message without sending")
    args = parser.parse_args()
    
    print("\n📤 DISCORD POSTER")
    print("=" * 40)
    
    # Load report
    report = load_report(args.report)
    if not report:
        return
    
    # Format message
    message = format_report(report)
    
    if args.dry_run:
        print("\n📋 DRY RUN - Message preview:")
        print("-" * 40)
        print(message)
        print("-" * 40)
    else:
        post_to_discord(message)

if __name__ == "__main__":
    main()
