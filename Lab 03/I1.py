# Import necessary modules from the cryptography library.
from cryptography.hazmat.primitives import hashes, hmac
import binascii

# Define a function named 'show_hash' that takes four arguments: 'name', 'type', 'data', and 'key'.
def show_hash(name, type, data, key):
    # Create an HMAC (Hash-based Message Authentication Code) object with the specified key and hash type.
    digest = hmac.HMAC(key, type)
    
    # Update the HMAC object with the input data.
    digest.update(data)
    
    # Finalize the HMAC computation and get the resulting hash value.
    res = digest.finalize()
    
    # Convert the hash value to hexadecimal format.
    hex = binascii.b2a_hex(res).decode()
    
    # Convert the hash value to Base64 format.
    b64 = binascii.b2a_base64(res).decode()
    
    # Print the HMAC name, hexadecimal hash value, and Base64 hash value.
    print(f"HMAC-{name}: {hex} {b64}")

# Define input data and key as strings.
st = "Hello"
k = "qwerty123"

# Convert the input data and key to bytes.
data = st.encode()
key = k.encode()

# Print the input data and key in both hexadecimal and string formats.
print("Data: ", st)
print(" Hex: ", binascii.b2a_hex(data).decode())
print("Key: ", k)
print(" Hex: ", binascii.b2a_hex(key).decode())
print()

# Call the 'show_hash' function with different HMAC names and hash types, input data, and key.
show_hash("MD5", hashes.MD5(), data, key)
show_hash("SHA1", hashes.SHA1(), data, key)
show_hash("SHA256", hashes.SHA256(), data, key)
show_hash("SHA512", hashes.SHA512(), data, key)
