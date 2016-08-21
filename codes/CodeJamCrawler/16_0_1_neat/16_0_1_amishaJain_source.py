T = int(input())


for i in range(T):
 
	
	n = input()
	
	s = set(n)
	
	n = number = int(n)
 
	
	if number==0:
		
		r = "INSOMNIA"

 
	else:

		while len(s) < 10:

			number += n
			
			s.update(set(str(number)))

		r = str(number)

 
	print("Case #",i+1,": ",r,sep="")