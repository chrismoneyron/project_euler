import math

i = 1
while True:
	triangle_num = sum(range(i))
	num_divisors = 0
	triangle_num_sqrt = math.sqrt(triangle_num)
	
	for j in range(1, int(math.ceil(triangle_num_sqrt))):
		if triangle_num % j == 0:
			num_divisors += 1

	num_divisors *= 2

	if (math.ceil(triangle_num_sqrt) - triangle_num < 1e-6):
		num_divisors += 1

	if num_divisors >= 500:
		print triangle_num
		break

	i += 1