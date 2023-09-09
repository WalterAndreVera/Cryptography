# Import necessary modules from the cryptography library
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import hashlib
import sys
import binascii

# Define the plaintext message and password
original_message = 'hello'
password = 'hello123'

# Set the plaintext variable to the original message
plaintext = original_message

# Function to encrypt data
def encrypt_data(data, encryption_key, encryption_mode):
    # Create an AES encryption method with the provided key
    encryption_method = algorithms.AES(encryption_key)
    
    # Create a cipher with the chosen encryption method and mode
    cipher = Cipher(encryption_method, encryption_mode, default_backend())
    
    # Create an encryptor
    encryptor = cipher.encryptor()
    
    # Encrypt the data
    ciphertext = encryptor.update(data) + encryptor.finalize()
    
    return ciphertext

# Function to decrypt data
def decrypt_data(ciphertext, decryption_key, encryption_mode):
    # Create an AES encryption method with the provided key
    encryption_method = algorithms.AES(decryption_key)
    
    # Create a cipher with the chosen encryption method and mode
    cipher = Cipher(encryption_method, encryption_mode, default_backend())
    
    # Create a decryptor
    decryptor = cipher.decryptor()
    
    # Decrypt the ciphertext
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    return decrypted_data

# Function to pad data
def pad_data(data, block_size=128):
    # Create a padder with PKCS7 padding
    padder = padding.PKCS7(block_size).padder()
    
    # Pad the data
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    
    return padded_data

# Function to unpad data
def unpad_data(data, block_size=128):
    # Create an unpadder with PKCS7 padding
    unpadder = padding.PKCS7(block_size).unpadder()
    
    # Unpad the data
    unpadded_data = unpadder.update(data)
    unpadded_data += unpadder.finalize()
    
    return unpadded_data

# Hash the password using SHA-256 to generate an encryption key
encryption_key = hashlib.sha256(password.encode()).digest()

# Print the original plaintext before padding
print("Original Message: ", original_message)

# Pad the plaintext using PKCS7 padding and print it in hexadecimal format
padded_plaintext = pad_data(plaintext.encode())
print("Padded Message (PKCS7): ", binascii.hexlify(bytearray(padded_plaintext)))

# Encrypt the padded plaintext using AES in ECB mode and print the resulting ciphertext in hexadecimal format
ciphertext = encrypt_data(padded_plaintext, encryption_key, modes.ECB())
print("Ciphertext (ECB): ", binascii.hexlify(bytearray(ciphertext)))

# Decrypt the ciphertext using the same key and mode
decrypted_plaintext = decrypt_data(ciphertext, encryption_key, modes.ECB())

# Remove the padding from the decrypted plaintext
decrypted_plaintext = unpad_data(decrypted_plaintext)
print("Decrypted Message: ", decrypted_plaintext.decode())
