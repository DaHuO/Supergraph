def dec_eq(num1,base,len1):
	sum1 = 0
	for ch in num1:
		len1 -= 1
		sum1 += int(ch) * (base ** len1)		
	return(sum1)

def chk_prime(num):
	stop = 100	
	start = 0
	if num == 2: return (True,2)
	if num == 3: return (True,3)
	if num % 2 == 0: return (False,2)
	if num % 3 == 0: return (False,3)
	i = 5
	w = 2

	while i * i <= num:
        	if num % i == 0: return(False,i)
        	i += w
		w = 6 - w
		start += 1
		if start == stop: return(True,num)
	return (True,num)
    	
T = int(input())
len1,req = map(int,raw_input().split())
done = 0
comb = 2**(len1 -2)
print ('Case #1:')
for i in xrange(comb):
	str1 = '1'+bin(i)[2:].zfill(len1-2)+'1'
	mul = []
	for base in range(2,11):
		de = dec_eq(str1,base,len1)
		(chk,res) = chk_prime(de)
		if chk: break
		else: mul.append(res)
	else:

		print (str1),
		for val in mul: print (val),
		print
		done += 1
	if done == req: break 
