# Caesar Cipher Encryptor/Decryptor
# Cybersecurity Project #2

print("=== Caesar Cipher Encryptor/Decryptor ===")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose an option (1 or 2): ")

message = input("Enter a message: ")
shift = int(input("Enter shift value: "))

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

        elif choice == "2":
            new_position = (position - shift) % 26

        else:
            print("Invalid option! Please choose 1 or 2.")
            exit()

        # Convert position back into a character
        result += chr(start + new_position)

    else:
        # Keep spaces and symbols unchanged
        result += char

print("\nOriginal Message:", message)
print("Shift Value:", shift)
print("Result:", result)
