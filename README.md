# Numeric Key One-Time Pad Cipher (Encode & Decode)

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple Python implementation of a **One-Time Pad (OTP)** style cipher using numeric key sequences. This project demonstrates the fundamentals of modular arithmetic in cryptography, making it ideal for cybersecurity labs and academic study.

## 📌 Overview
This script allows users to encrypt and decrypt alphabetic messages using a series of numbers as the key. Unlike a Caesar cipher which uses a single shift value, this OTP-style cipher uses a unique shift for every single letter.

## ✨ Features
* **Bidirectional:** Encode (encrypt) and decode (decrypt) messages.
* **Numeric Key Input:** Supports comma-separated integer keys.
* **Security Validation:** Enforces the "Key Length = Text Length" rule.
* **CLI Interface:** Simple, interactive command-line experience.
* **Educational:** Clear implementation of $Mod 26$ logic.

---

## ⚙️ Cipher Logic

The program maps letters to numbers: **A = 0, B = 1, ..., Z = 25**.

### Formulas
* **Encoding:** $Ciphertext = (Plaintext + Key) \pmod{26}$
* **Decoding:** $Plaintext = (Ciphertext - Key) \pmod{26}$



### Example
**Input Text:** `GDCHV`  
**Numeric Key:** `5, 21, 15, 1, 7`  
**Output:** `BICGU`

---

## 📂 Project Structure
```text
otp_cipher/
│
├── otp_cipher.py      # Main implementation script
└── README.md          # Project documentation
```

## How to Run
Prerequisites

Python 3.x installed

Command Prompt or Terminal access

Execution

Navigate to the project directory and run:
```
python otp_cipher.py
```
Sample Execution Output
```=== Numeric Key Cipher (OTP Style) ===
1. Encode
2. Decode

Choose option (1 or 2): 2
Enter text: GDCHV
Enter key (comma-separated numbers): 5,21,15,1,7

Decrypted Text: BICGU
```
## Security Notes

This cipher follows One-Time Pad principles
For theoretical perfect secrecy:
The key must be truly random
The key must be used only once
The key length must equal the message length
Reusing a key compromises security
This implementation is for educational purposes only.

## Limitations
Supports only uppercase English alphabets (A–Z)
Does not support digits or special characters
Manual key input required
Not suitable for real-world cryptographic use

## Educational Use Cases
Cryptography and cybersecurity laboratories
Understanding modular arithmetic
OTP cipher demonstrations
Exam preparation and viva explanations
Academic mini-project submissions

## Future Enhancements
Automatic random key generation
ASCII and binary One-Time Pad support
File encryption and decryption
Key reuse detection
Implementations in Java, C, or JavaScript

## License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it for educational purposes.
