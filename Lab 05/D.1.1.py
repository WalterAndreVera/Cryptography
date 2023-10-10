# Import necessary modules from the cryptography library for cryptographic operations
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec 
from cryptography.hazmat.primitives.kdf.hkdf import HKDF 
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.backends import default_backend

# Import binascii for hexadecimal encoding and sys for system-related functions
import binascii 
import sys

# Define the size of the derived key (256 bits)
size = 32

# Generate a private key for Bob using the SECP192R1 elliptic curve
Bob_private_key = ec.generate_private_key(ec.SECP192R1(), default_backend()) 

# Generate a private key for Alice using the SECP192R1 elliptic curve
Alice_private_key = ec.generate_private_key(ec.SECP192R1(), default_backend())

# Perform the ECDH key exchange, Bob calculates his shared key
# using his private key and Alice's public key
Bob_shared_key = Bob_private_key.exchange(ec.ECDH(), Alice_private_key.public_key())

# Derive a symmetric encryption key for Bob using HKDF and the SHA-256 hash algorithm
Bob_derived_key = HKDF(algorithm=hashes.SHA256(), length=size, salt=None, info=b'', backend=default_backend()).derive(Bob_shared_key)

# Perform the ECDH key exchange, Alice calculates her shared key
# using her private key and Bob's public key
Alice_shared_key = Alice_private_key.exchange(ec.ECDH(), Bob_private_key.public_key())

# Derive a symmetric encryption key for Alice using HKDF and the SHA-256 hash algorithm
Alice_derived_key = HKDF(algorithm=hashes.SHA256(), length=size, salt=None, info=b'', backend=default_backend()).derive(Alice_shared_key)

# Print the name of the elliptic curve used for the public keys
print("Name of curve: ", Bob_private_key.public_key().curve.name)

# Print the size of the generated key (in bytes and bits)
print(f"Generated key size: {size} bytes ({size * 8} bits)")

# Extract and print Bob's private key value
vals = Bob_private_key.private_numbers()
print(f"\nBob private key value: {vals.private_value}")

# Extract and print Bob's public key in hexadecimal format
vals = Bob_private_key.public_key()
enc_point = binascii.b2a_hex(vals.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
print("Bob's public key: ", enc_point)

# Extract and print Alice's private key value
vals = Alice_private_key.private_numbers()
print(f"\nAlice private key value: {vals.private_value}")

# Extract and print Alice's public key in hexadecimal format
vals = Alice_private_key.public_key() 
enc_point = binascii.b2a_hex(vals.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
print("Alice's public key: ", enc_point)

# Print the derived encryption keys for both Bob and Alice in hexadecimal format
print("\nBob's derived key: ", binascii.b2a_hex(Bob_derived_key).decode()) 
print("Alice's derived key: ", binascii.b2a_hex(Alice_derived_key).decode())
