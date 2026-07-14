print("Welcome to Password Strength Checker!")

password = input("Enter your password: ")

print("Your password is:", password)

if len(password) >= 8:
    print("✅ Good! Your password has at least 8 characters.")
else:
    print("❌ Your password must be at least 8 characters long.")

has_upper = False

for letter in password:
    if letter.isupper():
        has_upper = True
        break

if has_upper:
    print("✅ Password contains an uppercase letter.")
else:
    print("❌ Password needs an uppercase letter.")

has_lower = False

for letter in password:
    if letter.islower():
        has_lower = True
        break

if has_lower:
    print("✅ Password contains a lowercase letter.")
else:
    print("❌ Password needs a lowercase letter.")
