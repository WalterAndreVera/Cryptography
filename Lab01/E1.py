import random

samples = [ random.randint(1, 2) for i in range(100) ]
heads = samples.count(1)
tails = samples.count(2)
#Simulates 100 coin tossings
#Return the number of heads and tails
print ("Heads count=%d, Tails count=%d" % (heads, tails))
