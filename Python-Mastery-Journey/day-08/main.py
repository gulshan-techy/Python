# --- FOR LOOPS ---
print("\n FOR LOOP: Iterating over a String")
user_name = "Gulshan"
for char in user_name:
    print(f"-> {char}")

print("\n FOR LOOP: Using range() with Step")
print("Numbers from 1 to 10 (Jumping by 3):")
for i in range(1, 12, 3):
    print(f"Value: {i}")

# --- WHILE LOOPS ---
print("\n WHILE LOOP: Decrementing (Countdown)")
count = 3
while count > 0:
    print(f"T-minus: {count}...")
    count -= 1  # Decrementing so it doesn't run forever
print("Liftoff! 🚀")

print("\n WHILE LOOP with ELSE BLOCK")
attempts = 2
while attempts > 0:
    print(f"Running task... (Attempts left: {attempts})")
    attempts -= 1
else:
    print("✅ Loop ended naturally (Condition became False)")
