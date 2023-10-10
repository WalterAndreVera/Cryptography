# Define a function for the Diffie-Hellman Key Exchange (DHKE) cracker
def DHKEcracker(g, p, A, B):
    # Initialize variables to store Alice's and Bob's secret keys
    a = None
    b = None

    # Iterate through possible private key values from 2 to p-2
    for i in range(2, p - 1):
        # Check if (g^i) mod p is equal to A (Alice's public key)
        if (g**i) % p == A:
            a = i
        # Check if (g^i) mod p is equal to B (Bob's public key)
        if (g**i) % p == B:
            b = i

    # Print Alice's secret key
    print("Alice's secret key is: " + str(a))
    # Print Bob's secret key
    print("Bob's secret key is: " + str(b))

    # Calculate and print the shared key using Alice's secret key and Bob's public key
    shared_key = (A**b) % p
    print("The shared key is: " + str(shared_key))

# Call the DHKEcracker function with specific parameters
DHKEcracker(5, 97, 32, 41)
