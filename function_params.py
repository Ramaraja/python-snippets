# Function params example

def print_max(a, b):
	if a > b:
		print a, 'is maximum'
	elif a == b:
		print a, 'is equal to', b
	else:
		print b, 'is maximum'

# directly pass values
print_max(3, 4)