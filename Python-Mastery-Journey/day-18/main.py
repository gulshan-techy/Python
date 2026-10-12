from datetime import datetime, date, timedelta

# 1 Current Date & Time
print("\n 1. CURRENT DATE & TIME:")
now = datetime.now()
print(f" Raw Timestamp: {now}")
print(f" Extracted Year: {now.year}")
print(f" Extracted Month: {now.month}")
print(f" Extracted Day: {now.day}")

# 2 Custom Formatting (strftime)
print("\n 2 CUSTOM FORMATTING (strftime):")
friendly_format = now.strftime("%A, %B %d, %Y")
time_format = now.strftime("%I:%M %p")
print(f" Friendly Date: {friendly_format}")
print(f" 12-Hour Time: {time_format}")

# 3 Parsing Strings to Dates (strptime)
print("\n 3. PARSING STRINGS TO DATES (strptime):")
date_string = "25-12-2026 14:30:00"
parsed_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
print(f" Input String: '{date_string}'")
print(f" Converted Object: {parsed_date} (Type: {type(parsed_date).__name__})")

# 4 Time Travel with timedelta
print("\n 4. TIME CALCULATIONS (timedelta):")
future_deadline = now + timedelta(days=10, hours=5)
past_date = now - timedelta(days=7)
print(f" 10 Days & 5 Hours From Now: {future_deadline.strftime('%d-%m-%Y %H:%M')}")
print(f" Exactly 7 Days Ago Was: {past_date.strftime('%d-%m-%Y')}")

print(" 🎉 Datetime Module Operations Completed Successfully!")
