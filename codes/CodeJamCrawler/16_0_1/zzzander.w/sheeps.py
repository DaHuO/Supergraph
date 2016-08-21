input = open('A-large.in', 'r')
T = int(input.readline().strip())
cap = 1000000
for X in range(1,T+1):
	N = int(input.readline().strip())
	numbers = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0 ,'9':0}
	final = 0
	if N == 0:
		print "Case #%d:" % X,'INSOMNIA'
	else:
		for factor in range(1,cap):
			num = N * factor
			count = 0
			for y in str(num):
				numbers[y] = 1
			for z in numbers:
				if numbers[z] == 1:
					count += 1
			if count == 10:
				final = num
				break
		print "Case #%d:" % X,final