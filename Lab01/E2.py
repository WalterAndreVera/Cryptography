#The following function takes a ciphertext and a key,
#and applies the reverse process of the caesar cipher using the key
def decrypt(ciphertext,key):
    result = ""

    # traverse text
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char==" ":
          result +=" "
        # Encrypt uppercase characters

        elif (char.isupper()):
            result += chr((ord(char) - key-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return result

#The following function uses to decrypt function with all possible keys
# and returns the key and the result in each case
def breakcaesar(ciphertext):
  for i in range(26):
    print("key: "+str(i)+", plaintext: "+decrypt(ciphertext,i))
breakcaesar("WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ")
