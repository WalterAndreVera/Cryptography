# Import the necessary functions and modules from the Passlib library for password hashing.
import passlib.hash;

# Define a Python function named 'hash_SHA' that takes two arguments: 'string' and 'salt'.
def hash_SHA(string, salt):
    # Print the input string followed by a colon to provide context for the following hash values.
    print(string+":")
    
    # Generate and print the SHA-1 hash for the input string using Passlib's 'sha1_crypt.hash()' function.
    # The 'salt' parameter is specified to use the provided salt value.
    print("SHA1:" + passlib.hash.sha1_crypt.hash(string, salt=salt))
    
    # Generate and print the SHA-256 hash for the input string using Passlib's 'sha256_crypt.hash()' function.
    # The 'salt' parameter is specified to use the provided salt value.
    print("SHA256:" + passlib.hash.sha256_crypt.hash(string, salt=salt))
    
    # Generate and print the SHA-512 hash for the input string using Passlib's 'sha512_crypt.hash()' function.
    # The 'salt' parameter is specified to use the provided salt value.
    print("SHA512:" + passlib.hash.sha512_crypt.hash(string, salt=salt))

# Call the 'hash_SHA' function with the input string "changeme" and the salt "8sFt66rZ"
# to compute and display SHA-1, SHA-256, and SHA-512 hashes for this input.
hash_SHA("changeme", "8sFt66rZ")

# Call the 'hash_SHA' function with the input string "123456" and the same salt "8sFt66rZ"
# to compute and display SHA-1, SHA-256,
