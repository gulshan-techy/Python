# Data Structures - Dictionaries & Sets

## Q. What are Dictionaries & Sets?
##  Ans. Up until now, we accessed data using numeric indexes (e.g., list[0]). But what if we want to access data using a Name (Key)? Or what if we need to store a list of items where Duplicates are NOT allowed?That's where Dictionaries (Hash Maps) and Sets come in. These are the most powerful data structures for real-world engineering.

## 1. Python ***Dictionaries*** (Key-Value Pairs)A Dictionary is an unordered collection of items stored as Key: Value pairs. It is Mutable, meaning you can change the values after creation. It is widely used for JSON data and Configuration management.
```
Syntax :- Curly Braces {key: value}
```
***Characteristics of Dictionary:***
- Key-Value Pair :- Data is accessed via Keys, not indexes.
- Mutable :- You can update values, add new keys, or delete them.
- Unique Keys :- Keys must be unique (Duplicate keys overwrite the old value).
- Unordered :- (Though Python 3.7+ maintains insertion order, logically they are treated as unordered maps).

***Common Dictionary Methods:***
- get(key) :- Returns value for the key (Safe: returns None if key is missing).
- keys() :- Returns a list of all keys.
- values() :- Returns a list of all values.
- items() :- Returns a list of (Key, Value) tuples.
- update(dict) :- Merges another dictionary or adds multiple key-values.
- pop(key) :- Removes the key and returns its value.

Creating a Dictionary (Server Config)
```
server_config = {
    "host": "192.168.1.5",
    "port": 8080,
    "os": "Linux"
}
print(server_config["host"])  # Output: 192.168.1.5
```

Modifying & Adding ItemsPython# 
Updating existing value
```
server_config["os"] = "Ubuntu 22.04"
```
## Adding a new key-value pair
```
server_config["region"] = "us-east-1"
Using Methods (Update & Get)Python# Safe Access
print(server_config.get("admin"))  # Output: None (No error crash)
```

## Bulk Update
```
server_config.update({"active": True, "env": "Production"})
Removing Items removed_val = server_config.pop("port") # Removes 'port'
print(server_config)
```
## 2. Python ***Sets*** (Unique Collections)A Set is an unordered collection of Unique items. It automatically removes duplicates. It is highly optimized for mathematical operations like Union and Intersection.
```
Syntax :- Curly Braces {item1, item2} or set()
```
***Characteristics of Set:***
- Unordered :- Items have no fixed position (Index access [0] is NOT allowed).
- Unique :- Duplicates are automatically removed.
- Mutable :- You can add or remove items.
- Faster Search :- Checking if item in set is much faster than a List.

***Common Set Methods:***

- add(item) :- Adds an element to the set.
- update(iterable) :- Adds multiple items (like extending a list).
- remove(item) :- Removes item (Throws error if missing).
- discard(item) :- Removes item (No error if missing).
- pop() :- Removes a random item.
- union(|) :- Combines items from two sets.
- intersection(&) :- Returns common items.

Creating a Set (Handling Duplicates)Python# List with duplicates
```
id_list = [101, 102, 101, 103, 102]
```
### Converting to Set removes duplicates
```
unique_ids = set(id_list)
print(unique_ids)  # Output: {101, 102, 103}
Adding & RemovingPythonmy_set = {"DevOps", "Cloud"}

my_set.add("AI")           # Add single
my_set.update(["SecOps", "Data"]) # Add multiple

my_set.discard("Cloud")    # Remove safely
Mathematical Operations (Venn Diagram Logic)Pythonteam_A = {"Alice", "Bob"}
team_B = {"Bob", "Charlie"}

print(team_A | team_B)  # Union: {'Alice', 'Bob', 'Charlie'}
print(team_A & team_B)  # Intersection: {'Bob'}
```
## 4. Real-World Use Cases (DevOps & Cloud)

## When to use a Dictionary?
## API Responses: Handling JSON data from AWS/Azure APIs (e.g., EC2 details).Configurations: Storing settings like { "ENV": "PROD", "DB_HOST": "localhost" }.Tagging Resources: Mapping Instance IDs to Owner names.

## When to use a Set?
## Filtering Logs: Extracting unique IP addresses from a massive server log file.Access Control: Storing user permissions (e.g., {"read", "write"}) to ensure no duplicates.Comparison: Finding missing resources between two environments (using Difference -).

## 5. Performance Proof (Engineering Insight)Let's prove that Searching in a Set is instant compared to a List. We use the timeit module.Scenario: Searching for a number in a dataset of 1 Million items.Pythonimport timeit

### Creating Data
```
huge_list = list(range(1000000))
huge_set = set(range(1000000))
search_item = 999999
```
### Speed Test
```
list_time = timeit.timeit(stmt=f"{search_item} in huge_list", globals=globals(), number=1000)
set_time = timeit.timeit(stmt=f"{search_item} in huge_set", globals=globals(), number=1000)

print(f"List Search Time: {list_time:.5f} sec")
print(f"Set Search Time:  {set_time:.5f} sec")
Conclusion:Lists search one by one (Linear Search).Sets/Dicts use Hash Tables (Instant Lookup).Result: Sets are 1000x+ FASTER for searching!
```
