import random

r = random.randint(1, 100)

while True:
	num = input('guess number: ')
	num = int(num)
	if num == r:
		print('You are right')
		break
	elif num > r:
		print('number is bigger than the answer')
	elif num < r:
		print('number is smaller than the answer')

