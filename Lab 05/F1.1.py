g=5 #generator
p=97 #prime number
A=32 #Alice public key
B=41 #Bob public key
for i in range(2,p-1):
  if (g**i)%p==A:
    a=i
  if (g**i)%p==B:
    b=i
print("Alice's secret key is: "+str(a))
print("Bob's secret key is: "+str(b))
print("The shared key is: "+str((A**b)%p))
