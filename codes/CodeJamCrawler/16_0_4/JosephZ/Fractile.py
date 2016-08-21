filename="D-small-attempt0.in"
f1=open(filename)
info=f1.readline()
n=int(info)

def work(k,c,s):
	if k>s:
		return ["IMPOSSIBLE"]
	result=[]
	for j in range(0,k**c,k**(c-1)):
		result.append(str(j+1))
	return result

f2=open("output.txt",'w+')
for i in range(n):
	info=f1.readline()
	info=info.strip().split(" ")
	k,c,s=int(info[0]),int(info[1]),int(info[2])

	result=" ".join(work(k,c,s))
	line="Case #"+str(i+1)+": "+str(result)+'\n'
	f2.write(line)

f2.close()

print("liu xing wei zhen shuai")
# f2=open("output.txt",'w+')
# for i in range(len(result)):
#         line="Case #"+str(i+1)+": "+str(result[i])+'\n'
#         f2.write(line)
# f2.close()


