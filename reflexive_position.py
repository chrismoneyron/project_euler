# NEED TO IMPROVE SPEED!
import math

sum = 0
s = ''
number = 1
k_min = 1
k_max = 13
array = range(k_min, (k_max + 1))
array = [int(math.pow(3, k)) for k in array]
for n in array:
	num_digits = len(str(n))
	count = 0
	while count < n:
		count = 0
		s += str(number)
		i = 0
		while i <= (len(s) - num_digits):
			if int(s[i:(num_digits + i)]) == n:
				count += 1
				if count >= n:
					s = s[0:(i + 1)]
					break
			i += 1
		number += 1
		position = len(s)
	sum += position
	print '%d: %d' % (n, sum)
print sum
