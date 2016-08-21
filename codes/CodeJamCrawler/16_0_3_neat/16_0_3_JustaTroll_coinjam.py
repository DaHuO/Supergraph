import random

t = int(input())

l = []

def nondiv(n):
    for i in range(2,n):
    	if n%i==0:
    		return i

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print ('\t',f)
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 

def gencojam(m):
	naam = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
	while (1):
		if naam not in l:
			flag = 1
			for i in range(2,11):
				sum = 0
				#print ("daaaamn")
				#print (i)
				#print (i**15)
				for j in range(0,16):
					sum = sum + naam[j]*(i**(15-j))
				#print (sum)
				if (is_prime(sum)):
					flag=0
					break
			if (flag):
				l.append(naam)
				return naam
		randvar = random.randint(1,14)
		if naam[randvar]==0:
			naam[randvar]=1
		else:
			naam[randvar]=0


def gennondiv(k):
	lol = []
	for i in range(2,11):
		sum = 0
		for j in range(0,16):
			sum = sum + k[j]*(i**(15-j))
			#print (sum)
		lol.append(nondiv(sum))
	return lol



def fufu(N,J):
	count = 0
	while (count<50):	
		cojam = gencojam(N)
		#print (cojam)
		#print (("").join(cojam))
		#print ("*******************************************")
		nums = gennondiv(cojam)
		#print (nums)
		count = count+1
		for i in range(0,len(nums)):
			nums[i] = str(nums[i])
	#print (nums)
		p = []
		for i in range(0,len(cojam)):
			p.append(str(cojam[i]))
		strr =	nums[0]+" "+nums[1]+" "+nums[2]+" "+nums[3]+" "+nums[4]+" "+nums[5]+" "+nums[6]+" "+nums[7]+" "+nums[8]
		print (("").join(p),strr)




for i in range(1, t+1):
  s = input()  # read a list of integers, 2 in this case 
  #print (s)
  #print ("Case #{}: {} ".format(fufu(16,50)))
 
  print ("Case #{0}:".format(i))
  fufu(16,50)