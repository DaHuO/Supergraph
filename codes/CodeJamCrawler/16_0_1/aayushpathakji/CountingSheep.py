for test_cases in range(int(input())):
	n=int(input())
	i=1
	s=set()
	string =""
	test=10
	if n==0:
		answer="INSOMNIA"
	else:	
		while(len(s) != 10):
			mul=n*i
			string+=str(mul)
			s=set(string)
			answer=mul
			#print (string,s,end=" ")
			i+=1
	print ("Case #{}: {}".format(test_cases+1,answer))	