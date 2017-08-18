max_pandigital = 0
for number in range(1, 1000):
	pandigital = ''
	n = 1
	while len(pandigital) < 9:
		product = number * n
		product_string = str(product)
		pandigital += str(product)
		if (int(pandigital) > max_pandigital) and len(pandigital) == 9 and n > 1:
			max_pandigital = int(pandigital)
			max_n = n
			max_number = number
		n += 1

print('Max Pandigital: %d' % max_pandigital)
print('Number: %d' % max_number)
print('n: %d' % max_n)