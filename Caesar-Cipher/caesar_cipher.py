# Caesar Cipher Encryptor/Decryptor
# Cybersecurity Project #2

message = input("Enter a message: ")
shift = int(input("Enter shift value: "))
choice = input("Encrypt or Decrypt? ").lower()

result = ""

for char in message:
    if char.isalpha():

        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')

        position = ord(char) - start

        if choice == "encrypt":
            new_position = (position + shift) % 26
        elif choice == "decrypt":
            new_position = (position - shift) % 26
        else:
            print("Invalid choice!")
            exit()

        result += chr(start + new_position)

    else:
        result += char

print("Result:", result)
