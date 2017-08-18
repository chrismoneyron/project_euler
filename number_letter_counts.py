small_num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 
			7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 
			12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
			16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

med_num_dict = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 
				70: 'seventy', 80: 'eighty', 90: 'ninety'}

num_letters = 0
lower_number = 1
upper_number = 1000
for num in range(lower_number, (upper_number + 1)):
	if num in small_num_dict:
		num_string = small_num_dict[num]
		num_letters += len(num_string)
	elif num in med_num_dict:
		num_string = med_num_dict[num]
		num_string = ''.join(num_string.split())
		num_letters += len(num_string)
	elif num % 100 == 0 and num < 1000:
		num_string = small_num_dict[num / 100] + ' hundred'
		num_string = ''.join(num_string.split())
		num_letters += len(num_string)
	elif num > 100 and num < 1000:
		num_string = small_num_dict[(num - (num % 100)) / 100] + ' hundred and '
		if (num % 100) in small_num_dict:
			num_string += small_num_dict[num % 100]
			num_string = ''.join(num_string.split())
			num_letters += len(num_string)
		elif (num % 100) in med_num_dict:
			num_string += med_num_dict[num % 100]
			num_string = ''.join(num_string.split())
			num_letters += len(num_string)
		else:
			num_string += med_num_dict[(num % 100) - (num % 10)]
			num_string += ' ' + small_num_dict[num % 10]
			num_string = ''.join(num_string.split())
			num_letters += len(num_string)
	elif num == 1000:
		num_string = 'one thousand'
		num_string = ''.join(num_string.split())
		num_letters += len(num_string)
	else:
		num_string = med_num_dict[num - (num % 10)]
		num_string += ' ' + small_num_dict[num % 10]
		num_string = ''.join(num_string.split())
		num_letters += len(num_string)

print 'Total number of letters: %d' % num_letters