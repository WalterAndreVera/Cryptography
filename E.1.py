#The following function returns a list of a number of "size" numbers
#pseudo-randomly generated using Linear Congruential Random Numbers
def seqpseudorand(a,seed,c,m,size):
#We use the equation x{i+1}=a*x{i}+c mod m
  seq=[seed]*size
  seq[0]=(a*seed+c)%m #Although x{0}=seed, we do not include it in the list
  for i in range(size-1):
    # We use the equation x{i+1}=a*x{i}+c mod m
    seq[i+1]=(a*seq[i]+c)%m
  return seq #Return the list
print(seqpseudorand(21,35,31,100,5))
print(seqpseudorand(22,35,31,100,4))
print(seqpseudorand(954365343,436241,55119927,1000000, 4))
print(seqpseudorand(2175143,3553,10653,1000000, 4))