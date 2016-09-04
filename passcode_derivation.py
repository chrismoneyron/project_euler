# Find starting numbers, determine if one starting number comes before or after other starting number in login attempts
# Answer: 73162890
file = open('keylog.txt', 'r')
logins = []
for i in range(50):
	logins.append(file.readline().strip())

def find_next_number(curr_number, passcode, starting_numbers):
	for login in logins:
		if curr_number == -1:
			if login[0] not in starting_numbers:
				starting_numbers.append(login[0])

	for login in logins:
		if curr_number != -1:
			index = login.find(str(curr_number))
			#print 'Index: %d' % index
			if index == 0:
				if login[index + 2] in starting_numbers:
					#print 'Login: %s' % login
					starting_numbers.remove(login[index + 2])
					#print 'Starting Numbers: %s' % starting_numbers
		else:
			if login[1] in starting_numbers:
				starting_numbers.remove(login[1])

	second_numbers = []
	for number in starting_numbers:
		print 'Number: %s' % number
		for login in logins:
			index = login.find(str(number))
			if index != -1 and index != 2:
				if login[index + 1] not in second_numbers:
					second_numbers.append(login[index + 1])
					if login[index + 1] in starting_numbers:
						starting_numbers.remove(login[index + 1])


	if len(starting_numbers) == 1:
		print 'Starting Numbers: %s' % starting_numbers
		print 'Second Numbers: %s' % second_numbers

		passcode += str(starting_numbers[0])
		print 'Passcode: %s' % passcode
		curr_number = starting_numbers[0]
		starting_numbers = second_numbers[:]
		find_next_number(curr_number, passcode, starting_numbers)

passcode = ''
starting_nums = []
find_next_number(-1, passcode, starting_nums)