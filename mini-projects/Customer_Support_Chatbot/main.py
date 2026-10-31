print("Bot: Welcome to one8 support!")
print("Please choose one of the options:")
print("1. Product Information")
print("2. Order Status")
print("3. Refund Policy")
print("4. Technical Support")
print("5. Contact Us")

user = int(input("Enter your choice in 1/2/3/4/5 :"))
if user == 1:
    print("Bot: Please choose a product category:")
    print("a. Laptops")
    print("b. Mobiles")
    print("c. Accessories")
    user = input("Enter your choice in a/b/c:")
    if user == 'a':
        print("Bot: Our laptops include Model A, Model B, and Model C. All come with 1‑year warranty.")
    elif user == 'b':
        print("Bot: Our mobiles include Apple and Androids. Both support 5G.")
    elif user == 'c':
        print("Bot: Accessories include chargers, headphones, and covers.")
    else:
        print("Bot: Invalid choice. Please try again.")

elif user == 2:
    order_id = input("Bot: Please enter your order ID: ")
    print(f"Bot: Your order #{order_id} is shipped and will be delivered in 3 days.")

elif user == 3:
    print("Bot: Please choose one of the refund queries:")
    print("a. Refund eligibility")
    print("b. Refund timeline")
    print("c. Refund method")
    user = input("Enter your choice in a/b/c:")
    if user == 'a':
        print("Bot: Refunds are eligible if requested within 30 days of purchase.")
    elif user == 'b':
        print("Bot: Refunds are processed within 7 business days after approval.")
    elif user == 'c':
        print("Bot: Refunds are credited back to your original payment method.")
    else:
        print("Bot: Invalid choice. Please try again.")

elif user == 4:
    print("Bot: Please describe your technical issue:")
    issue = input("Enter your issue: ")
    print(f"Bot: Thank you for reporting: '{issue}'. Our technical team will assist you shortly.")

elif user == 5:
    print("Bot: You can reach us at support@one8.com or call +91-1234567890.")

else:
    print("Bot: Please enter a valid input!")
