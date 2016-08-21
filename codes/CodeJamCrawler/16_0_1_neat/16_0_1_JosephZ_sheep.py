filename="A-large.in"
f1=open(filename)
numbers=list()
result=list()
info=f1.readline()
n=int(info)
correct=set([1,2,3,4,5,6,7,8,9,0])

def split(t):
	result=[]
	for i in range(len(t)):
		result.append(int(t[i]))
	return set(result)

for i in range(n):
	t=str(f1.readline()).strip()
	initial=int(t)
	checked=split(t)
	if initial==0:
		result.append('INSOMNIA')
		continue
	index=1
	while True:
		temp=index*initial
		if checked==correct:
			result.append(temp)
			break
		checked=checked|split(str(temp+initial))
		index+=1

f2=open("output.txt",'w+')
for i in range(len(result)):
        line="Case #"+str(i+1)+": "+str(result[i])+'\n'
        f2.write(line)
f2.close()


