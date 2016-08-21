
lst=[0,1,2,3,4,5,6,7,8,9]
f=open("input.in","r")
T=f.readline()
T=int(T)

fo=open("output.txt","w")
# print T
cnt=1


while T>=cnt:
	# print T,cnt

	
	num_lst=[]
	# N=int(raw_input(''))
	N=int(f.readline())
	if N!=0:
		tmp_N=N
		j=1
		print num_lst,lst,num_lst==lst
		while num_lst!=lst:
			t_lst= map(int, str(N))
			# print t_lst
			for i in range(len(t_lst)):
				num_lst.append(int(t_lst[i]))
			# print "num_lst  ",num_lst
			num_lst=list(set(num_lst))

			# print num_lst
			N=(j+1)*tmp_N
			j=j+1

		print (j-1)*tmp_N
		fo.write("Case #"+str(cnt)+": "+str((j-1)*tmp_N)+"\n")
	else:
		print "INSOMNIA"
		fo.write("Case #"+str(cnt)+": "+"INSOMNIA"+"\n")


	cnt+=1
f.close
fo.close()