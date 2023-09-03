from math import floor
#The following functions returns the prime numbers up to n
def criba(n):
	#We use a modified version of Erasthotenes prime sieve
	#Notice that using the equation 6*k+-1 is equivalent
	#to performing to rounds of the Erasthotenes prime sieve
	primes = [2,3] #We know 2,3 are prime (and are not considered by the 6*k+-1 equation)
	isPrime = [0 for i in range(n)] #isPrime stores booleans answering whether a number is prime or not
	#We initialize isPrime with 0 for every number
	isPrime[2] = isPrime[3] =1 #We mark 2,3 as prime
	limit=floor((n-1)/6)+1 #We establish a limit for k when using the equation 6*k+-1
	for i in range(1,limit):
		isPrime[6*i-1]=1 #We mark the numbers ofthe form 6*k+-1 as possible primes
		isPrime[6*i+1]=1
	if 6*limit-1<=n:
		isPrime[6*limit-1]=1
	for i in range(5,n): #Now we consider the numbers from 5 to n and perform the Erasthotenes prime sieve
		if isPrime[i]:
			primes.append(i)
			h = i
			while i*h < n:
				isPrime[i*h] = 0
				h += 1
	return primes #Return a list of primes up to n

print(criba(100))
print(criba(1000)[-1])