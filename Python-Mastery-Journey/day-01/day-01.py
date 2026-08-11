# --- 1. Memory Management Proof (Integer Interning) ---
a = 10
b = 10

print(id(a))    # memory address of object 10
print(id(b))    # same as id(a)

# Insight: Python points both variables to the SAME object to save memory! 
# This is called 'Interning'.


# --- 2. This is How define different data types variables ---
server_name = "xyz"      # String
server_count = 5       # Integer
is_active = True       # Boolean
cpu_load = 45.5        # Float   - Precision value

print(f"Server {server_name} is active: {is_active} load is {cpu_load}")
