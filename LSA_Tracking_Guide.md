# How to Track Local Services Ads (LSA) in GoHighLevel

**The Problem:**
LSA (Google Guaranteed) does **not** use URLs, so "UTM Tracking" does not work. You cannot just "link" it like a Search Ad.

**The Solution:**
You must "trap" the lead at the source (Phone, Booking, or Message) and force it into GHL.

---

## Method 1: The "Direct Booking" Trap (Easiest)

*Best for: Clients who want appointments.*

1. **Enable "Reserve with Google":**
    * In GHL > Settings > Integrations > **Reserve with Google**.
    * Connect your GHL Calendar.
2. **The Result:**
    * When a lead clicks "Book" on the Google LSA profile, it goes *directly* into the GHL Calendar.
    * **Source:** Automatically marked as "Reserve with Google" (easy to filter).

---

## Method 2: The "Call Forwarding" Trap (Most Common)

*Best for: Emergency services (Electricians, Plumbers) who get phone calls.*

**Challenge:** Google *assigns* you a tracking number on the LSA profile. You usually cannot change this to your GHL number directly.

**The Workaround:**

1. **Get the LSA Number:** Log into the [LSA Dashboard](https://ads.google.com/localservices).
2. **Set Forwarding:** Tell Google to forward calls to your **GHL Number** (not your personal cell).
    * *LSA Dashboard > Profile & Budget > Phone Number > Edit.*
    * Enter your GHL Twilio Number here.
3. **The Result:**
    * Customer calls Google Number -> Forwards to GHL Number -> GHL "hears" the call -> Forwards to Client.
    * **Tracking:** GHL records the call and creates a contact.
    * **Attribution:** You must manually tag these or use a specific "LSA Dedicated" GHL number to know the source.

---

## Method 3: The "Email Parsing" Trap (Backup)

*Best for: "Message" leads or if Call Forwarding fails.*

1. **LSA Notifications:** Google sends an email for every lead ("New tracking number..." or "New message...").
2. **The Setup:**
    * Set the "Notification Email" in LSA to a specific GHL "Mailgun" address (or use Zapier).
    * **Zapier Flow:** `Gmail (New Email matching "Local Services")` -> `GHL (Create/Update Contact)`.
3. **The Result:**
    * Zapier reads the email body ("Customer Name: John Doe"), scrapes it, and pushes it to GHL.

---

## Summary Strategy for MEC

1. **Do Method 2 (Call Forwarding):** Change the "Destination Number" in LSA to a new GHL Number called "LSA Tracking Line."
2. **Do Method 1 (Reserve):** If they take bookings.
3. **Agency Report:** You will see "Source: Call" and "Called Line: LSA Tracking Line."
