test=input()


ind=0
while test>0:
	K,C,S=map(int, raw_input().split())
	test=test-1
	ind=ind+1
	print "Case #"+str(ind)+":",

	print "1",
	ans=1
	for i in range(K-1):
		ans=ans+K**(C-1)
		print ""+str(ans),
	print " "
