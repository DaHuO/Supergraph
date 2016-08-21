fin=open('a_small.in','r')
fout=open('a_small.out','w')

T=int(fin.readline())

let=[[25,4,17,14],[14,13,4],[19,22,14],[19,7,17,4,4],[5,14,20,17],[5,8,21,4],[18,8,23],[18,4,21,4,13],[4,8,6,7,19],[13,8,13,4]]

def solve(nums,min_v):
	ans=""
	for i in range(min_v,10):
		if max(nums)==0:
			break
		n=2**19
		for ind in set(let[i]):
				n=min(n,int(nums[ind]//let[i].count(ind)))
		t_nums=nums[:]
		ans0=""
		for k in range(n):
			for j in let[i]:
				t_nums[j]-=1
			if max(t_nums)>0:
				ans0=solve(t_nums[:],i+1)
			if ans0!="":
				n=k+1
				break
		if ans0=="" and max(t_nums)>0:
			continue
		return(str(i)*n+ans0)
	return ans

for t in range(T):
	s=fin.readline()
	nums=[0 for i in range(26)]
	for i in range(len(s)):
		l=ord(s[i])-65
		if l>0:
			nums[ord(s[i])-65]+=1
	ans=solve(nums[:],0)
	fout.write("Case #%d: %s\n" % (t+1,ans))

fin.close()
fout.close()