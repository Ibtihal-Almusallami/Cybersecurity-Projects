# Caesar Cipher Encryptor/Decryptor with Brute Force Attack
# Cybersecurity Project #2

print("=== Caesar Cipher Encryptor/Decryptor ===")
print("1. Encrypt")
print("2. Decrypt")
print("3. Brute Force Attack")

choice = input("Choose an option (1, 2, or 3): ")

message = input("Enter a message: ")

# Only ask for a shift if encrypting or decrypting
if choice == "1" or choice == "2":
    shift = int(input("Enter shift value: "))

# -----------------------------
# Brute Force Attack
# -----------------------------
if choice == "3":
    print("\n=== Brute Force Results ===")

    for shift in range(26):
        result = ""

        for char in message:
            if char.isalpha():

                # Determine if character is uppercase or lowercase
                if char.isupper():
                    start = ord('A')
                else:
                    start = ord('a')

                # Convert character into a position (0-25)
                position = ord(char) - start

                # Try every possible shift (decrypt)
                new_position = (position - shift) % 26

                # Convert back to a letter
                result += chr(start + new_position)

            else:
                # Keep spaces and symbols unchanged
                result += char

        print(f"Shift {shift}: {result}")

# -----------------------------
# Encrypt / Decrypt
# -----------------------------
elif choice == "1" or choice == "2":

    result = ""

    for char in message:
        if char.isalpha():

            # Determine if character is uppercase or lowercase
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            # Convert character into a position (0-25)
            position = ord(char) - start

            # Encrypt or decrypt
            if choice == "1":
                new_position = (position + shift) % 26
            else:
                new_position = (position - shift) % 26

            # Convert position back into a character
            result += chr(start + new_position)

        else:
            # Keep spaces and symbols unchanged
            result += char

    print("\nOriginal Message:", message)
    print("Shift Value:", shift)
    print("Result:", result)

# -----------------------------
# Invalid Option
# -----------------------------
else:
    print("Invalid option! Please choose 1, 2, or 3.")
