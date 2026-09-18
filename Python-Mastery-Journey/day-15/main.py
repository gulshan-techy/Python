print(" 🚀 Day 15 Practice: Local Scope, Global Scope & Constants")

print(" 1. CONSTANTS (Convention: ALL_CAPS):")
PI = 3.14159
MAX_CONNECTIONS = 100
print(f"Value of PI is strictly set to: {PI}")
print(f"Max allowed connections: {MAX_CONNECTIONS}\n")

print("----------------------------------------------------------------\n")

print(" 2. LOCAL VARIABLES (Private to the function):")
def secure_room():
    secret_key = "XYZ-999"  # Local Variable
    print(f"Inside function: The secret key is '{secret_key}'")

secure_room()
print("Outside function: Python doesn't know what 'secret_key' is!\n")

print("---------------------------------------------------------------\n")
print(" 3. GLOBAL VARIABLES (Publicly readable):")
player_name = "Gulshan"  # Global Variable

def greet_player():
    print(f"Reading global variable inside function: Hello, {player_name}!\n")

greet_player()

print("--------------------------------------------------------------\n")

print(" 4. MODIFYING GLOBAL VARIABLES (Using 'global' keyword):")
score = 0  # Global Variable
print(f"Score before function call: {score}")

def increase_score():
    global score  # Telling Python to use the global variable, not create a new local one
    score += 50
    print("(Inside function) Score increased by 50!")

increase_score()
print(f"Score after function call: {score}\n")
