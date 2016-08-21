import pickle

allperms = pickle.load(open('perms.pkl', 'rb'))

for cases in range(1, int(input()) + 1):
	ans = 0
	n = int(input())
	temp = list(map(int, input().split()))
	a = [x-1 for x in temp]
	
	for i in range(2,n+1)[::-1]:
	    perms = allperms[n][i]
	    for p in perms:
	        flag = True
	        for j in range(i):
	            dude = p[j]
	            if(p[(j-1)%i] != a[dude] and p[(j+1)%i] != a[dude]):
	                flag = False
	                break
	        if(flag):
	            ans = i
	            break
	    if(ans > 0):
	        break        
	print('Case #%d:' % (cases,), ans)
