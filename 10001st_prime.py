# Sieve's algorithm
num_occurence = 10001
max_numbers = num_occurence * 100
prime_array = [True] * max_numbers
prime_array[0] = False
for i in range(2, (max_numbers + 1)):
	for j in xrange((2 * i), (max_numbers + 1), i):
		prime_array[j - 1] = False

count = 0
for pos in range(len(prime_array)):
	if prime_array[pos] == True:
		count += 1
		if count == num_occurence:
			print (pos + 1)
			break