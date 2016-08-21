n = eval(input())
ans = []

alpha= []
for i in range(ord('A'),ord('Z')+1):
        alpha.append(chr(i))
for i in range(n):
	part = eval(input())
	inp = input()
	inp = inp.split(" ")
	inp = [ int(j) for j in inp]
	ans2 = []
	while(max(inp)!=0):
		total = sum(inp)
		maximum = max(inp);
		m1i = inp.index(maximum)
		ans2.append(alpha[m1i])
		inp[m1i] = maximum-1
		#print("Mid = ",inp)
		maximum2 = max(inp)
		m2i = inp.index(maximum2)
		inp[m2i] = (maximum2)-1
		#print("Mid2 = ",inp)
		maximum3 = max(inp)
		if(sum(inp)>0 and (maximum3/sum(inp))>0.5):
				inp[m2i] = (maximum2);
		else:
				x = ans2.pop();
				ans2.append(x+alpha[m2i])
	ans.append(ans2)

 	
k =""
for i in range(n):
        k =""
        x = ans[i]
        for j in x:
                k += j+" "
        print("Case #",i+1,": ",k,sep="")
