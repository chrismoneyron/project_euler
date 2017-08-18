longest_chain = 0
longest_chain_starting_num = 0
for starting_num in range(999999, 12, -2):
	curr_chain = 1
	n = starting_num
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = (3 * n) + 1
		curr_chain += 1
	if curr_chain > longest_chain:
		longest_chain = curr_chain
		longest_chain_starting_num = starting_num

print 'Longest Chain: %d' % longest_chain
print 'Longest Chain Starting Number: %d' % longest_chain_starting_num