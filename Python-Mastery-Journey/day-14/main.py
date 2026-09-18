print(" 🚀 Day 14 Practice: Raising Custom Errors ('raise' keyword)")
def validate_user_input(user_value):
    print(f"\nChecking input: '{user_value}'")
    
    # 1. Normal Exit Case
    if user_value.lower() == "quit":
        print("✅ User typed 'quit'. Exiting safely without errors.")
        return
    
    # 2. Raising a Custom Error for bad text
    if not user_value.isdigit():
        raise TypeError("❌ FATAL ERROR: Input MUST be a number or 'quit'!")
        
    # 3. Raising a Custom Error for out-of-range numbers
    num = int(user_value)
    if num < 5 or num > 9:
        raise ValueError(f"❌ VALUE ERROR: {num} is not allowed. Must be between 5 and 9.")
        
    # 4. Success Case
    print(f"✅ Success! {num} is a perfectly valid number.")

# Simulating user inputs one by one
test_cases = ["7", "quit", "15", "hello"]

for case in test_cases:
    try:
        validate_user_input(case)
    except Exception as e:
        # Catching the errors we just RAISED so the script doesn't completely die
        print(f"{e} (Program stopped for this input)")

print(" 🎉 Execution finished. Custom errors were successfully raised!")
