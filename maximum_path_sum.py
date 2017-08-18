file = open('maximum_path_sum_2.txt', 'r')
triangle = []

for line in file:
	triangle.append(line.strip().split())

file.close()

for i in range(len(triangle)):
	for j in range(len(triangle[i])):
		triangle[i][j] = int(triangle[i][j])

sum_triangle = [[triangle[0][0]]]
for i in range(len(triangle) - 1):
	sum_triangle.append([])
	prev_right_val = 0
	for j in range(i + 1):
		left_val = sum_triangle[i][j] + triangle[i + 1][j]
		right_val = sum_triangle[i][j] + triangle[i + 1][j + 1]
		if j == 0:
			sum_triangle[i + 1].append(left_val)
		else:
			if left_val > prev_right_val:
				sum_triangle[i + 1].append(left_val)
			else:
				sum_triangle[i + 1].append(prev_right_val)
				
		if j == i:
			sum_triangle[i + 1].append(right_val)
		
		prev_right_val = right_val

max_sum = max(sum_triangle[-1])

print 'The maximum total of the triangle is: %d' % max_sum