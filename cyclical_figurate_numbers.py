# Fix so that any order of numbers works

import math

def find_next_num(starting_num, order, ordered_set):
	if order == 3:
		num = str(int((starting_num * (starting_num + 1)) / 2))
		if len(num) == 4:
			ordered_set = [num]
			ordered_set = find_next_num(starting_num, 4, ordered_set)
		else:
			starting_num += 1
			ordered_set = find_next_num(starting_num, 3, ordered_set)
	for n in range(44, 142):
		if order == 4:
			num = str(int(math.pow(n, 2)))
		elif order == 5:
			num = str(int((n * ((3 * n) - 1)) / 2))
		elif order == 6:
			num = str(int(n * ((2 * n) - 1)))
		elif order == 7:
			num = str(int((n * ((5 * n) - 3)) / 2))
		else:
			num = str(int(n * ((3 * n) - 2)))
		if num[:2] == ordered_set[order - 4][2:] and len(num) == 4:
			ordered_set.append(num)
			print 'Ordered Set: %s' % ordered_set
			if order < 5:
				order += 1
				ordered_set = find_next_num(starting_num, order, ordered_set)
			else:
				return ordered_set
			
	ordered_set = []
	starting_num += 1
	order = 3
	ordered_set = find_next_num(starting_num, order, ordered_set)

ordered_set = []
starting_number = 44
starting_order = 3
print find_next_num(starting_number, starting_order, ordered_set)