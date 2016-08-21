
def check(l):
	for i in range(10):
		if l[i] == False:
			return False
	return True

def create():
	l = []
	for i in range(10):
		l.append(False)
	return l

def add(l,n):
	while n > 0:
		l[n%10] = True
		n = n / 10
	return l

def get(n):
	if n == 0:
		return -1
	l = create()
	j = n
	add(l,j)
	while not check(l):
		j = j + n
		l = add(l,j)
	return j

fin = open('input', 'r')
fout = open('output', 'w')
tests = int(fin.readline())
for i in range(tests):
	n = int(fin.readline())
	answer = get(n)
	if answer == -1:
		fout.write("Case #"+str(i+1)+": INSOMNIA\n")
	else:
		fout.write("Case #"+str(i+1)+": "+str(answer)+"\n")

fin.close()
fout.close()