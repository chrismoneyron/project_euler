import math

number = 600851475143
largest_prime_factor = 0
sqrt_number = int(math.ceil(math.sqrt(number)))
for i in range(2, sqrt_number):
	is_prime = True
	if number % i == 0:
		if i == 2 and i > largest_prime_factor:
			largest_prime_factor = i
		else:
			for j in range(2, i):
				if i % j == 0:
					is_prime = False
					break
		if is_prime and i > largest_prime_factor:
			largest_prime_factor = i

print largest_prime_factor