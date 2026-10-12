# 🐍 Day 18: Working with Date and Time in Python (`datetime` module)

## 📌 Overview
In almost every application we build—whether it's logging user activity, tracking timestamps, or scheduling tasks—we need to work with dates and times. 

Instead of writing complex custom logic for calendar math and time formats, Python provides a powerful built-in module called **`datetime`**. Today, I learned how to handle dates, times, format them for humans, and calculate time differences!

---

## 🛠️ Concepts Learned

### 1. Working with Current Date and Time
To get the current date and time right now, we use the `datetime` class inside the `datetime` module.

```
from datetime import datetime

# Get current local date and time
now = datetime.now()
print("Current Date and Time:", now)

# Extracting individual components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
```

### 2. Creating Specific Dates
You can create a custom date object by passing year, month, and day to the date class.
```
from datetime import date

# Creating a specific date (YYYY, MM, DD)
my_birthday = date(2005, 2, 22)
print("My Birthday:", my_birthday)
print("Day of the week (0=Mon, 6=Sun):", my_birthday.weekday())
```

### 3. Formatting Dates (strftime)
By default, Python datetime objects print in a standard format (YYYY-MM-DD HH:MM:SS). But what if we want to display it neatly as DD-MM-YYYY or write out the full month name? We use strftime() (String Format Time).

```
from datetime import datetime

now = datetime.now()

# Formatting to Day-Month-Year Hour:Minute:Second
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
print("Custom Formatted Date:", formatted_date)

# Formatting with full day and month name
friendly_format = now.strftime("%A, %B %d, %Y")
print("Friendly Format:", friendly_format)
```
(Common format codes: %Y = Year, %m = Month, %d = Day, %H = Hour, %M = Minute, %A = Day name, %B = Month name)

### 4. Parsing Strings into Dates (strptime)
Sometimes you receive a date as a plain string from user input or a file, and you need to convert it back into an actual Python datetime object to perform calculations. We use strptime() (String Parse Time).

```
from datetime import datetime

date_string = "25-12-2026 14:30:00"

# Converting string to datetime object using format directives
parsed_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")

print("Parsed Object:", parsed_date)
print("Data type:", type(parsed_date))
```
###5. Time Travel with timedelta
What if you want to know what date it will be 10 days from now, or what the date was 7 days ago? We use timedelta, which represents a duration or difference between two points in time.

```
from datetime import datetime, timedelta

current_time = datetime.now()

# Add 10 days and 5 hours
future_deadline = current_time + timedelta(days=10, hours=5)
print("Deadline after 10 days and 5 hours:", future_deadline)

# Subtract 7 days (1 week ago)
past_date = current_time - timedelta(days=7)
print("One week ago was:", past_date)

# Calculating difference between two dates
date1 = datetime(2026, 1, 1)
date2 = datetime(2026, 12, 31)
difference = date2 - date1
print(f"Days in between: {difference.days} days")
```

### 💡 Summary
```
Use datetime.now() to get the current system timestamp.

Use strftime() to convert a date object into a readable string format.

Use strptime() to convert a string into a date object for data processing.

Use timedelta to easily add, subtract, or measure time durations!
