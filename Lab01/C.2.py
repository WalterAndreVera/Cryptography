from math import isqrt
#The following function checks if a number is prime or not and returns a boolean
def is_prime(n):
    if n <= 3: #2, 3 are prime numbers
        return n > 1 #but 1 is not a prime number
    if n % 2 == 0 or n % 3 == 0: #If 2,3 divide a number, then that number if not prime
        return False
    limit = isqrt(n) #check if the rest of possible primes until sqrt(n) can divide n
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

#The following function returns M^e mod p
#and print a message answering whether p is prime or not
def modulo(M,e,p):
  if is_prime(p):
    # if p is a prime, print p is a prime
    print(str(p)+" is prime")
  else:
    #else, print p is not a prime
    print(str(p)+" is not prime")
    #return M^e mod p
  return (M ** e) % p #return M^e mod p
print(modulo(8,13,271))
print(modulo(12,23,973))
print(modulo(8,5,269))
print(modulo(5,5,53))
print(modulo(4,11,79))
print(modulo(101,7,293))