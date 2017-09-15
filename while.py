number = 23
running = True

while running:
	guess = int(raw_input('Enter an integer : '))
	if guess == number:
		print 'Congratulations, you guessed it.'
		break
	elif guess < number:
		print 'No, it is a little higher than that'
	else:
		print 'No, it is a little lower than that'

print 'Done'
