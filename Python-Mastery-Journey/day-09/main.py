# 1. Break Example
# Printing a multiplication table of 5, but stopping at 5 * 10

for i in range(1, 15):
    if i == 11:
        print("Loop is broken! Exiting...")
        break  # The loop stops here
    
    print("5 X", i, "=", 5 * i)

print ("-------------------------------------")

# 2. Continue Example
# Printing a multiplication table of 5, but skipping 5 * 10

for i in range(1, 15):
    if i == 10:
        print("Skipping the 10th iteration...")
        continue  # Skips only this step and moves to i = 11
    
    print("5 X", i, "=", 5 * i)
