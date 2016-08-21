f=open("A-small-attempt0(1).in","r")
T=f.readline()
T=int(T)
print T
fo=open("output.txt","w")
cnt=1


while T>=cnt:
	word=str(f.readline()).replace('\n','')
	print word,type(word)
	m=len(word)
	last_list=[word[0]]
	
	for m in range(1,len(word)):
		final_list=[]
		for i in range(len(last_list)):
			final_list.append(last_list[i]+word[m])
			final_list.append(word[m]+last_list[i])
		last_list=final_list
	last_list.sort()
	print last_list[-1]
	fo.write("Case #"+str(cnt)+": "+last_list[-1]+"\n")
	cnt+=1
f.close()
fo.close()


