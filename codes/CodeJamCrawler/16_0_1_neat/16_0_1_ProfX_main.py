def CheckRes(res):
  sum = 0
  for i in range(len(res)):
    sum = sum + res[i]
  if (sum != 0):
    return False
  else :
    return True

def StoreNb(number, res):

	digit = [int(i) for i in str(number)]
	digit.sort()
	for i in range(len(digit)):
  		res[digit[i]] = 0
		

# Main
t = int(input())
nb = []

for i in range(t):
  nb.append(int(input()));

for i in range(len(nb)):
  if(nb[i] == 0):
  	print("Case #{}: {}".format(i+1, "INSOMNIA"))
  else:
  	res = [1,1,1,1,1,1,1,1,1,1]
  	j = 0
  	number = 0
  	while (CheckRes(res) == False):
  		j = j+1
  		number = nb[i]*j
  	#	print(number)
  		StoreNb(number,res)
  #		print(number,res,CheckRes(res))
  		
  	print("Case #{}: {}".format(i+1,number))
  			
