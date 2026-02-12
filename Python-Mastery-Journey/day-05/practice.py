import sys
import timeit

# A. PYTHON DICTIONARIES (Key-Value Pairs)

print("\n--- A. DICTIONARY OPERATIONS ---")

# 1. Creating Dictionaries
server_config = {
    "host": "192.168.1.5",
    "port": 8080,
    "os": "Linux Ubuntu",
    "active": True
}
print(f"Original Config: {server_config}")

# 2. Accessing Items
print(f"Host: {server_config['host']}")

# .get() -> Safer way (Returns None if key missing, doesn't crash)
print(f"Admin User: {server_config.get('admin')}") 

# 3. Modifying Dictionaries (Mutable)
# Direct Assignment
server_config["region"] = "us-east-1"

# .update() -> Merge another dictionary into existing one (Bulk Update)
new_settings = {"active": False, "backup_enabled": True}
server_config.update(new_settings)
print(f"After .update(): {server_config}")

# .setdefault() -> Returns value if key exists, else inserts key with default value
# 'protocol' doesn't exist, so it adds 'https'
proto = server_config.setdefault("protocol", "https") 
print(f"SetDefault Protocol: {proto}")
print(f"Config after SetDefault: {server_config}")

# 4. Removing Elements
# pop() -> Removes key and returns value
removed_os = server_config.pop("os") 
print(f"Popped OS: {removed_os}")

# popitem() -> Removes the last inserted item (LIFO)
last_item = server_config.popitem()
print(f"Popped Last Item: {last_item}")

# del -> Deletes key strictly
if "port" in server_config:
    del server_config["port"]

# clear() -> Wipes out the dictionary (Emptying it)
temp_dict = {"temp": 100}
temp_dict.clear()
print(f"Cleared Dict: {temp_dict}") # Output: {}

# 5. Looping Keys & Values
print("\n--- Looping Config ---")
for key, value in server_config.items():
    print(f"{key} : {value}")

# B. PYTHON SETS (Unique Collections)

print("\n--- B. SET OPERATIONS ---")

# 1. Creating Sets (Unordered & Unique)
id_list = [101, 102, 101, 103, 102]
unique_ids = set(id_list)
print(f"Unique Set: {unique_ids}")

# 2. Adding Elements
my_set = {"DevOps", "AI", "Cloud"}

# .add() -> Add single item
my_set.add("Security")

# .update() -> Add multiple items (from list or another set)
my_set.update(["Blockchain", "Data Science"])
print(f"After Update: {my_set}")

# 3. Removing Elements
# .remove() -> Error if item missing
my_set.remove("AI")

# .discard() -> No Error if item missing (Safer)
my_set.discard("RandomString") 

# .pop() -> Removes a RANDOM item (Because sets are unordered)
removed_item = my_set.pop()
print(f"Popped Random Item: {removed_item}")

# 4. Copy vs Clear
# .copy() -> Creates a backup (Independent copy)
backup_set = my_set.copy()
my_set.clear()

print(f"Original (Cleared): {my_set}")
print(f"Backup Copy: {backup_set}")

# 5. Set Logic (Subset & Superset) - Very useful for Permissions/Roles
admins = {"Alice", "Bob", "Charlie"}
users = {"Alice", "Bob"}

# .issubset() -> Are all 'users' inside 'admins'?
print(f"Is Users subset of Admins? {users.issubset(admins)}") # True

# .issuperset() -> Does 'admins' contain all 'users'?
print(f"Is Admins superset of Users? {admins.issuperset(users)}") # True

# Mathematical Operations
print(f"Union (|): {admins | users}")
print(f"Intersection (&): {admins & users}")
print(f"Difference (-): {admins - users}")

# C. THE ENGINEERING INSIGHT (Why use Sets?)

print("\n--- C. PERFORMANCE ENGINEERING (Search Speed) ---")

# Experiment: Searching for a number in a Huge List vs Huge Set
huge_list = list(range(1000000)) 
huge_set = set(range(1000000))

search_item = 999999

# Speed Test
list_time = timeit.timeit(stmt=f"{search_item} in huge_list", globals=globals(), number=1000)
set_time = timeit.timeit(stmt=f"{search_item} in huge_set", globals=globals(), number=1000)

print(f"List Search Time: {list_time:.5f} sec")
print(f"Set Search Time:  {set_time:.5f} sec")

speed_up = list_time / set_time
print(f"\n✅ Conclusion: Searching in a Set is {speed_up:.0f}x FASTER than a List!")
