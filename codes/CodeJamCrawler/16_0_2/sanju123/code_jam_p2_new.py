
import operator
f=open("B-large.in","r")
T=f.readline()
T=int(T)

fo=open("output.txt","w")

cnt=1
	

def flip_subarray(lst):
	#flip 1--->-1 and -1--->1	
	for i in range(len(lst)):
		if lst[i]==0:
			lst[i]=1
		else:
			lst[i]=0
	return lst

while T>=cnt:
	N=f.readline().replace('\n','')
	num_lst=[]
	print N,type(N),list(N)
	t_lst= list(N)
	out_lst=[]
	for i in range(len(t_lst)):
		if t_lst[i]=='-':
			num_lst.append(0)#consider 0('-') as 1
		else:
			num_lst.append(1)#consider 1('+') as -1
		out_lst.append(1)
	# print num_lst
	
	flip_cnt=0
	tmp=num_lst[0]
	flip_flag=False
	while num_lst!=out_lst:
		for i in range(len(num_lst)):
			if num_lst[i]!=tmp:
				flip_flag=True
				print "value at index ",i,"  ",num_lst[i]
				tmp=num_lst[i]
				print "subarray ",num_lst[:i]
				flipped_subarray=flip_subarray(num_lst[:i])
				flipped_subarray=flipped_subarray[::-1]
				print "flipped_subarray  ",flipped_subarray

				
				for mm in range(len(flipped_subarray)):
					num_lst[mm]=flipped_subarray[mm]
				print "modified stack ",num_lst
				flip_cnt+=1
				break
			flip_flag=False

		if flip_flag==False:
			flip_cnt+=1
			break
	print flip_cnt
	fo.write("Case #"+str(cnt)+": "+str(flip_cnt)+"\n")
				


	cnt+=1
f.close
fo.close()