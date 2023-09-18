# Import the necessary functions and modules from the Passlib library for password hashing.
import passlib.hash;

# Define a Python function named 'hash_lm_nt' that takes a single argument 'string'.
def hash_lm_nt(string):
    # Print the input string followed by a colon to provide context for the following hash values.
    print(string+":")
    
    # Generate and print the LM hash for the input string using Passlib's 'lmhash.hash()' function.
    print("LM Hash:" + passlib.hash.lmhash.hash(string))
    
    # Generate and print the NTLM hash for the input string using Passlib's 'nthash.hash()' function.
    print("NTLM Hash:" + passlib.hash.nthash.hash(string))

# Call the 'hash_lm_nt' function with the input string "Napier" to compute and display LM and NTLM hashes.
hash_lm_nt("Napier")

# Call the 'hash_lm_nt' function with the input string "Foxtrot" to compute and display LM and NTLM hashes.
hash_lm_nt("Foxtrot")
