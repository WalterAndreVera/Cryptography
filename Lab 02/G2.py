from Crypto.Cipher import ARC4  # Import the ARC4 (RC4) cipher module from the Crypto library
import hashlib  # Import the hashlib module for key derivation

# Define a function to perform RC4 decryption
def rc4_decrypt(key, ciphertext_hex):
    cipher = ARC4.new(key)  # Create an ARC4 cipher object with the provided key
    ciphertext_bytes = bytes.fromhex(ciphertext_hex)  # Convert the hexadecimal ciphertext to bytes
    decrypted_bytes = cipher.decrypt(ciphertext_bytes)  # Decrypt the ciphertext
    return decrypted_bytes.decode('utf-8')  # Decode the decrypted bytes as a UTF-8 string

def main():
    keyname = "napier"  # Define the keyname, which could be any string (e.g., a password)
    ciphertext_hex = "8907deba"  # Define the hexadecimal ciphertext to be decrypted

    # Derive the actual encryption key by hashing the keyname using SHA-256
    key = hashlib.sha256(keyname.encode()).digest()

    # Decrypt the ciphertext using RC4 and the provided key
    decrypted_text = rc4_decrypt(key, ciphertext_hex)

    # Print the ciphertext (in hexadecimal) and the decrypted plaintext
    print("Ciphertext (Hexadecimal):", ciphertext_hex)
    print("Decrypted plaintext:", decrypted_text)

if __name__ == "__main__":
    main()
