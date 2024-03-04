text = "Hello World"

encrypted_text = ''
for letter in text:
    encrypted_text += chr(ord(letter) ^ 200)
print(encrypted_text)

decrypted_text = ''
for letter in encrypted_text:
    decrypted_text += chr(ord(letter) ^ 200)
print(decrypted_text)

# 1010
# 1100 ^
# 0110
# 1100 ^
# 1010
