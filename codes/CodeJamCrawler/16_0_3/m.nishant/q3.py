
import itertools
def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

# benchmarked on an old single-core system with 2GB RAM.

from math import sqrt

def is_prime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1

def next_prime(num):
    if (not num & 1) and (num != 2):
        num += 1
    if is_prime(num):
        num += 1
    while True:
        if is_prime(num):
            break
        num += 2
    return num



def first_factor(n):
	for num in xrange(2 , int(sqrt(n))+1):
	    if n % num == 0:
	        return num

'''
s = "100011"

for i in range(2,11):
	print(int(s , i))
'''
#n = 10**50
#print(next_prime(n))

#if is_prime(10000000000000000000000000000033):
#print "TRRUEE"

count =0
n = 14
c=50
print "Case #1:"
lst = list(itertools.product([0, 1], repeat=n))
for i in lst:
	s = "1"
	for k in i:
		s+=str(k)
	s+="1"
	
	flag=0
	nums = list()
	fact = list()
	for j in range(2,11):
		x = int(s , j)
		fact.append(first_factor(x))
		nums.append(x)
		if is_prime(x):
			flag=1
			break
	if flag==0:
		count+=1

		print s , 
		st = ""
		for h in fact:
			st+= str(h)+" "
		print st	
	if count==c:
		break		


	



'''
for i in x :
	print i
'''