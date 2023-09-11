from Crypto.Cipher import ChaCha20  # Import the ChaCha20 cipher module from the Crypto library
import hashlib  # Import the hashlib module for key derivation

# Function to decrypt ciphertext using ChaCha20
def chacha20_decrypt(key, nonce, ciphertext):
    cipher = ChaCha20.new(key=key, nonce=nonce)  # Create a ChaCha20 cipher object with the provided key and nonce
    plaintext = cipher.decrypt(ciphertext)  # Decrypt the ciphertext using the cipher
    return plaintext.decode()  # Convert the decrypted bytes to a string (assuming it's text)

def main():
    keyname = "qwerty"  # Define the keyname, which could be any string (e.g., a password)
    ciphertext_hex = "e96924f16d6e"  # Define the hexadecimal ciphertext to be decrypted

    # Derive the actual encryption key by hashing the keyname with SHA-256
    key = hashlib.sha256(keyname.encode()).digest()

    nonce = b'\x00' * 8  # Define the nonce as 8 bytes filled with zeros (nonce should be unique for each message)

    # Convert the ciphertext from hexadecimal to bytes
    ciphertext = bytes.fromhex(ciphertext_hex)

    # Decrypt the ciphertext using ChaCha20 and the provided key and nonce
    decrypted_text = chacha20_decrypt(key, nonce, ciphertext)

    # Print the ciphertext and the decrypted plaintext
    print("Ciphertext:", ciphertext_hex)
    print("Decrypted plaintext:", decrypted_text)

if __name__ == "__main__":
    main()
