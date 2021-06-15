import random
start = input('random number starts: ')
end = input('random number ends: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1		#count = count + 1
	num = input('guess number: ')
	num = int(num)
	if num == r:
		print('You are right')
		print('You are guessing the', count, 'time')
		break
	elif num > r:
		print('number is bigger than the answer')
	elif num < r:
		print('number is smaller than the answer')
	print('You are guessing the', count, 'time')
