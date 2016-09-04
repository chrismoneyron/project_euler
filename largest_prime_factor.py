# NEED TO IMPROVE SPEED!
number = 13195
factor = 1
while factor <= number:
	if number % factor == 0:
		factor_2 = number / factor
		is_prime = True
		j = 2
		while j <= factor_2:
			if factor_2 % j == 0:
				is_prime = False
			j += 1
		if is_prime:
			print('Largest prime factor: %d' % factor_2)
			break
	factor += 1