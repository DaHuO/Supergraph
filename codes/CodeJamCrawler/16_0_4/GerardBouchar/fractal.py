
# for small there can't be more than K L in a row if there is Gold elsewhere

for N in range(int(input())) :
	(k,c,s)=map(lambda x: int(x), input().split(" "))
	print("Case #"+str(N+1)+": "+str(list(range(1,k+1)))[1:-1].replace(',',''))