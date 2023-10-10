# Import necessary modules
import hashlib 
import sys 
import binascii 
import Padding 
import random

# Import AES encryption related modules
from Crypto.Cipher import AES 
from Crypto import Random

# Define the message to be encrypted
msg = "test"

# Function to encrypt a word using AES encryption
def encrypt(word, key, mode): 
    # Pad the plaintext to ensure its length is a multiple of 16 bytes (AES block size)
    plaintext = pad(word)
    # Create an AES encryption object with the provided key and mode
    encobj = AES.new(key, mode) 
    # Encrypt the padded plaintext
    return encobj.encrypt(plaintext)

# Function to decrypt ciphertext using AES decryption
def decrypt(ciphertext, key, mode): 
    # Create an AES decryption object with the provided key and mode
    encobj = AES.new(key, mode)
    # Decrypt the ciphertext
    rtn = encobj.decrypt(ciphertext) 
    return rtn

# Function to pad a string to a multiple of 16 bytes
def pad(s):
    extra = len(s) % 16 
    if extra > 0:
        s = s + (' ' * (16 - extra)) 
    return s

# Generate random numbers to create long-term keys for Alice and Bob
rnd = random.randint(1, 2**256)
keyA = hashlib.sha256(str(rnd).encode()).digest() 
rnd = random.randint(1, 2**256)
keyB = hashlib.sha256(str(rnd).encode()).digest()

# Print the long-term keys for Alice and Bob
print('Long-term Key Alice=', binascii.hexlify(keyA)) 
print('Long-term Key Bob=', binascii.hexlify(keyB))

# Generate a random number to create a session key
rnd = random.randint(1, 2**256)
keySession = hashlib.sha256(str(rnd).encode()).hexdigest()

# Encrypt the session key for Alice using her long-term key
ya = encrypt(keySession.encode(), keyA, AES.MODE_ECB) 
# Encrypt the session key for Bob using his long-term key
yb = encrypt(keySession.encode(), keyB, AES.MODE_ECB)

# Print the encrypted session keys sent to Alice and Bob
print("Encrypted key sent to Alice:", binascii.hexlify(ya)) 
print("Encrypted key sent to Bob:", binascii.hexlify(yb))

# Decrypt the session keys using the respective long-term keys
decipherA = decrypt(ya, keyA, AES.MODE_ECB) 
decipherB = decrypt(yb, keyB, AES.MODE_ECB)

# Print the decrypted session keys
print("Session key:", decipherA) 
print("Session key:", decipherB)
