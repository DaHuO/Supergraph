def storedata(nums, numcase):
	for ch in str(numcase):	     
		nums[ch]=''  	

limit = 10000000
fichero = open('input','r')
numcases = int(fichero.readline());
for i in range(numcases):
	numcase = int(fichero.readline());	
	nums={}	
	N=1
	while len(nums) < 10 and N <= limit:
		out = N*numcase
		storedata(nums, out)
		N+=1
		
	if N > limit:
		print 'Case #'+str(i+1)+': INSOMNIA'
	else:	
		print 'Case #'+str(i+1)+': '+str(out)
