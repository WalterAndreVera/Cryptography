#B.1 Write a Python program to determine the GCD for the following:
#The following function returns the gcd of a and b
def gcd(a,b):
  #We use the Euclidean Algorithm
  if a>b: #We use the Division algorithm on a,b
    r0=a
    r1=b
    r2=a%b
    while r2!=0: #We use the Division algorithm on the remainders until we get a zero remainder
      r0=r1
      r1=r2
      r2=r0%r1
    return r1 #Return the last non-zero remainder
  else: #We use the Division algorithm on b,a
    r0=b
    r1=a
    r2=b%a
    while r2!=0: #We use the Division algorithm on the remainders until we get a zero remainder
      r0=r1
      r1=r2
      r2=r0%r1
    return r1 #Return the last non-zero remainder
print(gcd(4105,10))
print(gcd(4539,6))
print(gcd(5435,634))
print(gcd(5432,634))
