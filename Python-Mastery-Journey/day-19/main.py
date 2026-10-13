print("="*65)
print(" 🚀 Day 19 Practice: Match Case Statements in Python")
print("="*65)

def evaluate_number(x):
    print(f"\n   -> Testing value: x = {x}")
    
    # Modern Python Match-Case block
    match x:
        case 0:
            print("      🎯 Match Found! x is zero (0)")
        case 4:
            print("      🎯 Match Found! x is four (4)")
        case _ if x == 90:
            print("      🛡️ Guard Condition Match! x is specially 90")
        case _:
            print(f"      📌 Default Wildcard Case (_): x is {x} (No specific match)")

# Simulating different inputs to test various cases
test_inputs = [0, 4, 15, 90, 7]

for val in test_inputs:
    evaluate_number(val)

print("\n" + "="*65)
print(" 🎉 Match-Case Execution Completed Successfully!")
print("="*65)
