term_1 = 1
term_2 = 2
sum = 0
while term_2 < 4000000:
	if term_1 % 2 == 0:
		sum += term_1
	if term_2 % 2 == 0:
		sum += term_2
	new_term_1 = term_1 + term_2
	new_term_2 = term_2 + new_term_1
	term_1 = new_term_1
	term_2 = new_term_2

print('Sum: %d' % sum)