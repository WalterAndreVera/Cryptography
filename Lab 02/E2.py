# Import necessary modules from the cryptography library
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

import hashlib
import binascii

# Define the hexadecimal ciphertext and the encryption key (password)
ciphertext_hex = '6ee95415aca2b33c'
password = 'ankle'

# Convert the hexadecimal ciphertext to bytes
ciphertext = binascii.unhexlify(ciphertext_hex)

# Generate a 128-bit key by hashing the password using SHA-256 and taking the first 16 bytes
key = hashlib.sha256(password.encode()).digest()[:16]

# Function to decrypt ciphertext using TripleDES and a specified mode (ECB)
def decrypt(ciphertext, key, mode):
    # Initialize TripleDES cipher with the provided key
    method = algorithms.TripleDES(key)
    cipher = Cipher(method, mode, default_backend())
    
    # Initialize TripleDES decryptor
    decryptor = cipher.decryptor()
    
    # Decrypt ciphertext
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    return plaintext

# Function to unpad data using PKCS7 padding
def unpad(data):
    unpadder = padding.PKCS7(64).unpadder()
    unpadded_data = unpadder.update(data)
    unpadded_data += unpadder.finalize()
    return unpadded_data

# Decrypt the ciphertext using TripleDES in ECB mode
plaintext = decrypt(ciphertext, key, modes.ECB())

# Remove padding from the decrypted plaintext
plaintext = unpad(plaintext)

# Print the decrypted text
print("Decrypted text:", plaintext.decode())
