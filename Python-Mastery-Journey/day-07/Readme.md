# ☁️ Day 7: Decision Making in Python (If-Elif-Else)

## 📌 Overview
Automation scripts cannot be rigid; they must react dynamically to changing infrastructure states. Today, I learned how to implement decision-making in Python using Conditional Statements (`if`, `elif`, `else`). 

Understanding how Python evaluates conditions and handles indentation is a core requirement for writing logic that can monitor servers, handle error codes, or trigger automated scaling events.

---

## 🛠️ Core Concepts Learned

### 1. The Conditional Operators
Python evaluates conditions to either `True` or `False` (Boolean). The core operators include:
*   `>` (Greater than)
*   `<` (Less than)
*   `>=` (Greater than or equal to)
*   `<=` (Less than or equal to)
*   `==` (Equal to)
*   `!=` (Not equal to)

### 2. If-Else (The Gatekeeper)
The simplest form of decision-making. If a condition is met, execute Block A. Otherwise, execute Block B.
```
# Cloud Example: Health Check
server_status = "offline"

if server_status == "running":
    print("Health Check Passed! ✅")
else:
    print("CRITICAL: Server is down. Triggering restart... 🔴")
```

### 3. Elif (Handling Multiple States)
When infrastructure has multiple thresholds (e.g., CPU load at 50%, 80%, or 95%), the elif (Else-If) ladder is used to check multiple conditions sequentially. Once a condition is met, the rest of the ladder is ignored.
```
# Cloud Example: Auto-Scaling Logic

cpu_load = 85

if cpu_load < 50:
    print("Normal Load: No action required.")
elif cpu_load <= 80:
    print("Warning: Load is getting high. Monitor closely.")
else:
    print("CRITICAL: Load > 80%. Provisioning new EC2 Instance...")
```

## *⚠️ Important*
Indentation is Mandatory: Unlike C or Java which use {} for code blocks, Python relies strictly on indentation (usually 4 spaces). Incorrect indentation will cause an IndentationError or completely alter the script's logic.

Typecasting from input(): Remember that user inputs are always read as Strings. You must convert them (int(), float()) before comparing them with numeric thresholds.

```
# Incorrect
age = input("Enter age: ")
if age > 18: # ❌ TypeError: string cannot be compared to int

# Correct
age = int(input("Enter age: "))
if age > 18: # ✅
```
