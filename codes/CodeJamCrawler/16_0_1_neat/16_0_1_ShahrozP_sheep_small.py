t = int(input()) 
for i in range(1, t + 1):
  n = int(input())  
  if n ==0:
  	print "Case #{}: {}".format(i, "INSOMNIA")
  else:
  	digits = ['0','1','2','3','4','5','6','7','8','9']
  	k = 1
  	j=0
  	while(j==0):
	  	num = str(n*k)
	  	k = k + 1
	  	for letter in num:
	  		if letter in digits:
	  			digits.remove(letter)
		if not digits:
	 		print "Case #{}: {}".format(i, num)
	 		j=1
