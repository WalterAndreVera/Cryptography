def sieve_for_primes_to(n):
  size = n//2
  sieve = [1]*size
  limit = int(n**0.5)
  for i in range(1,limit):
    if sieve[i]:
      val = 2*i+1
      tmp = ((size-1) - i)//val
      sieve[i+val::val] = [0]*tmp
  return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]


print (sieve_for_primes_to(100)[-1])
print (sieve_for_primes_to(1000)[-1])
print (sieve_for_primes_to(5000)[-1])
print (sieve_for_primes_to(10000)[-1])