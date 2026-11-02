import string

print("Welcome to Password Strength Checker!")

password = input("Enter your password: ")

uppercase = 0
lowercase = 0
digits = 0
special_chars = 0

for char in password:

    if char in string.ascii_uppercase:
        uppercase += 1

    elif char in string.ascii_lowercase:
        lowercase += 1

    elif char in string.digits:
        digits += 1

    elif char in string.punctuation:
        special_chars += 1

score = 0

if len(password) >= 8:
    score += 1

if uppercase > 0:
    score += 1

if lowercase > 0:
    score += 1

if digits > 0:
    score += 1

if special_chars > 0:
    score += 1

print("\nPassword Analysis:")
print("Password Length:", len(password))
print("Uppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Digits:", digits)
print("Special Characters:", special_chars)

print("\nPassword Strength:")

if score <= 2:
    print("Weak Password")

elif score <= 4:
    print("Medium Password")

else:
    print("Strong Password")
