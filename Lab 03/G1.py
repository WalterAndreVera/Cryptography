# Import the necessary functions and modules from the Passlib library for password hashing.
import passlib.hash;

# Define a Python function named 'hash_PBKDF2' that takes two arguments: 'string' and 'salt'.
def hash_PBKDF2(string, salt):
    # Print the input string followed by a colon to provide context for the following hash values.
    print(string+":")
    
    # Generate and print the PBKDF2 (SHA-1) hash for the input string using Passlib's 'pbkdf2_sha1.hash()' function.
    # The 'salt' parameter is specified as bytes using 'salt.encode()'.
    print("PBKDF2 (SHA1):", passlib.hash.pbkdf2_sha1.hash(string, salt=salt.encode()))

# Call the 'hash_PBKDF2' function with the input string "changeme" and the salt "ZDzPE45C"
# to compute and display the PBKDF2 (SHA-1) hash for this input.
hash_PBKDF2("changeme", "ZDzPE45C")

# Call the 'hash_PBKDF2' function with the input string "123456" and the same salt "ZDzPE45C"
# to compute and display the PBKDF2 (SHA-1) hash for this input.
hash_PBKDF2("123456", "ZDzPE45C")

# Call the 'hash_PBKDF2' function with the input string "password" and the same salt "ZDzPE45C"
# to compute and display the PBKDF2 (SHA-1) hash for this input.
hash_PBKDF2("password", "ZDzPE45C")
