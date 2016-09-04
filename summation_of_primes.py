# Sieve's algorithm
max_numbers = 2000000
prime_array = [True] * max_numbers
prime_array[0] = False
for i in range(2, (max_numbers + 1)):
	for j in xrange((2 * i), (max_numbers + 1), i):
		prime_array[j - 1] = False

sum = 0
for pos in range(len(prime_array)):
	if prime_array[pos] == True:
		sum += pos + 1

print sum