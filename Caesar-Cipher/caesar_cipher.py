# Caesar Cipher Encryptor/Decryptor
# Cybersecurity Project #2
message = input("Enter a message: ")
shift = int(input("Enter shift value: "))

choice = input("Encrypt or Decrypt? ").lower()

print("Choice:", choice)
print("Message:", message)
print("Shift:", shift)

result = ""

for char in message:
    if char.isalpha():
        print("Letter found:", char)
    else:
        result += char
