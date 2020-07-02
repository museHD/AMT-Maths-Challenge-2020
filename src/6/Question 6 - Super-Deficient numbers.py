import numpy as np
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def isPrime(num):
	for i in range(2, num): 
		if (num % i) == 0: 
			return False

oddnos = np.arange(1,10000,2).tolist()
oddcomp = []

for i in oddnos:
	if (isPrime(i) == False):
		oddcomp.append(i)


for j in oddcomp:
	total = sum(factors(j)) * 2
	# print(total)
	if total < j:
		print(j)

# INCOMPLETE