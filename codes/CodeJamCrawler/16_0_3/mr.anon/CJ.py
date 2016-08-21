from math import pow
from math import sqrt
from itertools import permutations
class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1

def find_factors(n):
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			return i

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def check(num):
	flag = True
	if num[0] == 0 or num[len(num)-1] == 0:
		flag = False
	else:
		for i in range(2,11):
			temp = int(str(''.join(str(x) for x in num)),i)
			if is_prime(temp) == True:
				flag = False
				break
	return flag

t = input()
for case in range(0,t):
	num = map(int,raw_input().split())
	N = num[0]
	J = num[1]
	print "Case #%d:"%(case+1)
	for i in range(0,N-1):
		coin = [0]*i
		for i in range(0,N-i):
			coin.append(1)
		a = list(perm_unique(coin))
		for p in a:
			if check(p) == True:
				print ''.join(str(x) for x in p)," ",
				for i in range(2,11):
					temp = int(str(''.join(str(x) for x in p)),i)
					print find_factors(temp)," ",
				print
				J = J - 1
			if J == 0:
				break
