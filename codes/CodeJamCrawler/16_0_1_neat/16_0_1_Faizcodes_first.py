
def sleep(n):
	if n == 0:
		return "INSOMNIA"
	else:
		array = set(list(str(n)))
		t = n
		i = 1 
		while len(array) != 10:
			t = i*n
			array = array.union(list(str(t)))
			# print array, len(array)
			i+=1
		return t
			
file = open("A-large.in")
data = file.readlines()
trials = int(data[0].strip('\n'))

for i in range(1, trials+1):
	number = int(data[i].strip('\n'))
	print "CASE #"+str(i)+": "+str(sleep(number))