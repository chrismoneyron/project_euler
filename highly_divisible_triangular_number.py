# NEED TO MAKE FASTER!
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
				if i in k and i != 1:
					k.append(i)
					added = True
			if not added and i != 1:
				primes.append([i])
			
		else:
			factors = find_first_factor_set(i)
			prime_factorization(factors, primes)
	return primes

iteration = 0
triangle_number = 0
max_divisors = 500
while True:
	iteration += 1
	triangle_number += iteration
	first_factors = find_first_factor_set(triangle_number)
	prime_numbers = prime_factorization(first_factors, [])
	num_factors = 1
	for prime in prime_numbers:
		num_factors *= (len(prime) + 1)
	if num_factors > 100:
		print 'Iteration: %d' % iteration
		print num_factors
	if num_factors > max_divisors:
		print triangle_number
		break