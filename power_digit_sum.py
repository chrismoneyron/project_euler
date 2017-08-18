num = 2 ** 1000
sum_digits = 0

while num > 0:
	digit = num % 10
	num = (num - digit) / 10
	sum_digits += digit

print 'Sum of digits: %d' % sum_digits