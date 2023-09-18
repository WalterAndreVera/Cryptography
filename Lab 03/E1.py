# Import the necessary functions and modules from the Passlib library for password hashing.
import passlib.hash;

# Define a Python function named 'hash_APR1' that takes two arguments: 'string' and 'salt'.
def hash_APR1(string, salt):
    # Print the input string followed by a colon to provide context for the following hash value.
    print(string+":")
    
    # Generate and print the APR1 MD5-based crypt hash for the input string using Passlib's 'apr_md5_crypt.hash()' function.
    # The 'salt' parameter is specified to use the provided salt value.
    print("APR1:" + passlib.hash.apr_md5_crypt.hash(string, salt=salt))

# Call the 'hash_APR1' function with the input string "changeme" and the salt "PkWj6gM4"
# to compute and display the APR1 MD5-based crypt hash for this input.
hash_APR1("changeme", "PkWj6gM4")

# Call the 'hash_APR1' function with the input string "123456" and the same salt "PkWj6gM4"
# to compute and display the APR1 MD5-based crypt hash for this input.
hash_APR1("123456", "PkWj6gM4")

# Call the 'hash_APR1' function with the input string "password" and the same salt "PkWj6gM4"
# to compute and display the APR1 MD5-based crypt hash for this input.
hash_APR1("password", "PkWj6gM4")
