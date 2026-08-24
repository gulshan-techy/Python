# 1. if-else 

server_status = "offline"

if server_status == "running":
    print("Health Check Passed! ✅")
else:
    print("CRITICAL: Server is down. Triggering restart... 🔴")

# 2. if-else-else

cpu_load = 85

if cpu_load < 50:
    print("Normal Load: No action required.")
elif cpu_load <= 80:
    print("Warning: Load is getting high. Monitor closely.")
else:
    print("CRITICAL: Load > 80%. Provisioning new EC2 Instance...")

# 3. Nested Conditionals

is_active = True
user_role = "admin"

if is_active:
    if user_role == "admin":
        print("Access Granted: Initiating deployment.")
    else:
        print("Access Denied: Insufficient privileges.")

# Important

  # Incorrect
age = input("Enter age: ")
if age > 18: # ❌ TypeError: string cannot be compared to int

# Correct
age = int(input("Enter age: "))
if age > 18: # ✅
