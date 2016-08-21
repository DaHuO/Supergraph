def calc(b):
	arr = set([i for i in str(b)])
	count = 1
	q = b
	while q!=q*(count+1):
		if arr == {'0','1','2','3','4','5','6','7','8','9'}:
			return q
		else:
			count += 1
			q = b*count
			arr|=set([i for i in str(q)])
	return 'INSOMNIA'
a = open('A-large.in','r').readlines()
attemps = int(a.pop(0))
attemps = 1 <=attemps<=100 and attemps or 0
output=''
for i in range(attemps):
	if 0<=int(a[i][:-1])<=10**6:
		output+='Case #' + str(i+1) + ': ' + str(calc(int(a[i][:-1]))) +'\n'
with open('tempo_google.txt','w') as q:
		q.write(output)
