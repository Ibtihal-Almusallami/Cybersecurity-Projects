print("Welcome to Password Strength Checker!")

password = input("Enter your password: ")

print("Your password is:", password)

if len(password) >= 8:
    print("✅ Good! Your password has at least 8 characters.")
else:
    print("❌ Your password must be at least 8 characters long.")
