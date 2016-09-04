import math

sum = 0
sum_squares = 0
for num in range(1, 101):
	sum += num
	sum_squares += math.pow(num, 2)

square_sum = math.pow(sum, 2)
difference = square_sum - sum_squares
print 'Difference: %d' % difference