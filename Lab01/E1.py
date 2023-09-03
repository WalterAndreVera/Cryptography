import random

samples = [ random.randint(1, 2) for i in range(500) ]
heads = samples.count(1)
tails = samples.count(2)
#Simulates 500 coin tossings
#Return the number of heads and tails
print ("Heads count=%d, Tails count=%d" % (heads, tails))
