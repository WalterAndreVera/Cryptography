from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import hashlib
import sys
import binascii

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python d_01.py <plaintext> <key>")
    sys.exit(1)

# Extract plaintext and key from command-line arguments
plaintext = sys.argv[1]
password = sys.argv[2]

def encrypt(plaintext, key, mode):
    method = algorithms.AES(key)
    cipher = Cipher(method, mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return ct

def pad(data, size=128):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return padded_data

def key_from_password(password):
    return hashlib.sha256(password.encode()).digest()

key = key_from_password(password)

plaintext_bytes = plaintext.encode()

plaintext_padded = pad(plaintext_bytes)

ciphertext = encrypt(plaintext_padded, key, modes.ECB())

# Print the ciphertext in hexadecimal format
print("Cipher Text (ECB):", binascii.hexlify(bytearray(ciphertext)).decode())
