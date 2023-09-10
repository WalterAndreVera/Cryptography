# Import necessary modules from the cryptography library
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

import hashlib
import binascii

# Input the hexadecimal ciphertext and encryption key
ciphertext_hex = input("Enter the hexadecimal ciphertext: ")
encryption_key = input("Enter the encryption key: ")

# Convert the hexadecimal ciphertext to bytes
ciphertext = binascii.unhexlify(ciphertext_hex)

# Generate the AES key by hashing the provided encryption_key
key = hashlib.sha256(encryption_key.encode()).digest()

# Initialize AES cipher with ECB mode
aes_cipher = Cipher(algorithms.AES(key), modes.ECB(), default_backend())

# Initialize AES decryptor
decryptor = aes_cipher.decryptor()

# Decrypt ciphertext
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

# Unpad the plaintext using PKCS7 padding
unpadder = padding.PKCS7(128).unpadder()
unpadded_plaintext = unpadder.update(plaintext) + unpadder.finalize()

# Print the decrypted plaintext
print("Decrypted Plaintext:", unpadded_plaintext.decode())
