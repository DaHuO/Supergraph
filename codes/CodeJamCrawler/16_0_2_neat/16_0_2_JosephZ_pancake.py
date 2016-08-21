filename="B-large.in"
f1=open(filename)
numbers=list()
result=list()
info=f1.readline()
n=int(info)

import re
def prep(t):
	t=re.sub("-+","-",t)
	t=re.sub("\++","+",t)
	return t
def work(t):
	if t=="+":
		return 0
	if t=="-":
		return 1
	if t[-1]=="-":
		return work(t[:-1])+2
	if t[-1]=="+":
		return work(t[:-1])

f2=open("output_2.txt",'w+')
for i in range(n):
        info=f1.readline()
        result=work(prep(info.strip()))
        line="Case #"+str(i+1)+": "+str(result)+"\n"
        f2.write(line)
f2.close()
print('done')


