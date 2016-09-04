import math

# Prime factorization
def find_first_factor_set(number):
	for i in range(2, number):
		if number % i == 0:
			return [i, (number / i)]
	return [1, number]

def prime_factorization(factors, primes):
	for i in factors:
		is_prime = True
		for j in range(2, i):
			if i % j == 0:
				is_prime = False
		if is_prime:
			added = False
			for k in primes:
				if i in k:
					k.append(i)
					added = True
			if not added:
				primes.append([i])
			
		else:
			factors = find_first_factor_set(i)
			prime_factorization(factors, primes)
	return primes

max_number = 20
prime_numbers = []
numbers_to_multiply = []
for m in range(1, (max_number + 1)):
	first_factors = find_first_factor_set(m)
	prime_numbers = prime_factorization(first_factors, [])
	for n in prime_numbers:
		index = None
		for p in numbers_to_multiply:
			if n[0] == p[0]:
				index = numbers_to_multiply.index(p)
				break
			else:
				index = None
		if index is None:
			numbers_to_multiply.append(n)
		elif len(n) > len(numbers_to_multiply[index]):
			numbers_to_multiply[index] = n

product = 1
for array in numbers_to_multiply:
	for number in array:
		product *= number

print product