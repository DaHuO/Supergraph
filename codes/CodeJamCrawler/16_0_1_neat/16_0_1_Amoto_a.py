from sys import stdin
def func(n):
	i=1
	ban=False
	num=[0,1,2,3,4,5,6,7,8,9]
	seen=set()
	alls=set()
	sleep=False
	while(not(ban)):
	    m=n*i
	    if m in alls:
	    	ban=True
	    	break
	    alls.add(m)
	    l=str(m)
	    for j in range(len(l)):
	            seen.add(int(l[j]))
	    c=0
	    i+=1
	    for cant in num:
	            if cant in seen:
	                    c+=1
	    if c==len(num):
	    	ban=True
	    	sleep=True
	if sleep:
		return str(n*(i-1))
	else:
		return "INSOMNIA"
def main():
	tab=[None for i in range (1000005)]
	t=int(stdin.readline().strip())
	for i in range(1,t+1):
		n=int(stdin.readline().strip())
		if tab[n]==None:
			tab[n]=func(n)
		print('Case #'+str(i)+': '+tab[n])
main()