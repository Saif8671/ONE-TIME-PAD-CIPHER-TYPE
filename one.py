import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def encode(plaintext, key):
    result = ""
    plaintext = plaintext.upper()

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            p = ord(plaintext[i]) - 65
            c = (p + key[i]) % 26
            result += chr(c + 65)
        else:
            result += plaintext[i]

    return result


def decode(ciphertext, key):
    result = ""
    ciphertext = ciphertext.upper()

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            c = ord(ciphertext[i]) - 65
            p = (c - key[i]) % 26
            result += chr(p + 65)
        else:
            result += ciphertext[i]

    return result


# -------- MAIN PROGRAM --------
print("=== Numeric Key Cipher (OTP Style) ===")
print("1. Encode")
print("2. Decode")

choice = input("Choose option (1 or 2): ")

text = input("Enter text: ").strip().upper()
key_input = input("Enter key (comma-separated numbers): ")

key = list(map(int, key_input.split(",")))

if len(text) != len(key):
    print("ERROR: Key length must match text length.")
else:
    if choice == "1":
        print("Encrypted Text:", encode(text, key))
    elif choice == "2":
        print("Decrypted Text:", decode(text, key))
    else:
        print("Invalid choice")

