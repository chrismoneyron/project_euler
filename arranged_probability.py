# Need to learn how to solve quadratic diophantine equation
import math

d = 1000000000000
denominator = d * (d - 1)
while True:
	numerator1 = (1.0 / 2.0) + (math.sqrt(1 + (2 * denominator)) / 2)
	numerator2 = (1.0 / 2.0) - (math.sqrt(1 + (2 * denominator)) / 2)

	if numerator1.is_integer() == True or numerator2.is_integer() == True:
		if numerator1 > 0:
			print 'Blue discs: %d' % int(numerator1)
			print 'Total Discs: %d' % int(d)
			print 'Probability: %f' % ((numerator1 * (numerator1 - 1)) / denominator)
		else:
			print 'Blue discs: %d' % int(numerator2)
			print 'Total Discs: %d' % int(d)
			print 'Probability: %f' % ((numerator2 * (numerator2 - 1)) / denominator)
		break
	else:
		d += 1
		denominator = d * (d - 1)