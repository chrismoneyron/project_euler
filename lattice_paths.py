import math

width = 20
height = 20

num_routes = (math.factorial(width + height) / math.factorial(height)) / math.factorial(width)

print num_routes