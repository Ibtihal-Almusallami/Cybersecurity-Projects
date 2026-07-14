print("Welcome to Password Strength Checker!")

password = input("Enter your password: ")

print("Your password is:", password)

# Password score starts at 0
score = 0

# Check password length
if len(password) >= 8:
    score += 1
    print("✅ Good! Your password has at least 8 characters.")
else:
    print("❌ Your password must be at least 8 characters long.")

# Check for uppercase letter
has_upper = False

for letter in password:
    if letter.isupper():
        has_upper = True
        break

if has_upper:
    score += 1
    print("✅ Password contains an uppercase letter.")
else:
    print("❌ Password needs an uppercase letter.")

# Check for lowercase letter
has_lower = False

for letter in password:
    if letter.islower():
        has_lower = True
        break

if has_lower:
    score += 1
    print("✅ Password contains a lowercase letter.")
else:
    print("❌ Password needs a lowercase letter.")

# Check for a number
has_number = False

for letter in password:
    if letter.isdigit():
        has_number = True
        break

if has_number:
    score += 1
    print("✅ Password contains a number.")
else:
    print("❌ Password needs a number.")

# Check for a special character
special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

has_special = False

for letter in password:
    if letter in special_characters:
        has_special = True
        break

if has_special:
    score += 1
    print("✅ Password contains a special character.")
else:
    print("❌ Password needs a special character.")

# Display the final score
print("\nPassword Score:", score, "/5")

# Determine password strength
if score <= 2:
    print("🔴 Weak Password")
elif score <= 4:
    print("🟡 Medium Password")
else:
    print("🟢 Strong Password")
