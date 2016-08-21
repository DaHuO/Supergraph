import itertools

def isprime( n ):
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        array.append(2)
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
        	array.append(x)
        	return False
          
    return True   

				 	
def find(two):

	length = two[0]
	count = two[1]

	lst = list(itertools.product([0, 1], repeat=length))
	
	j = 0
	k = 0
	ans = []
	ansarr = []

	while k != len(lst)-1:
		
		if int(lst[k][0]) == 1 and int(lst[k][length-1]) == 1:
		
			a = 0
			global array 
			array = []
			work = str(reduce(lambda rst, d: rst * 10 + d, lst[k]))
			
			for l in range(2, 10+1):

				no = int(work, l)
						
				if isprime(no) is False:
					
					continue

				else :
					
					a = 1	
					break
	
			if a == 0  and len(array) == 9:
				j += 1
				ans.append(work)
				ansarr.append(array)

			if j == count:
				break

		k += 1		
	
	if j == count and len(ansarr) == count:
		return (ans, ansarr)				


a = int(raw_input())	
	
y = raw_input()
z = map(int, y.split())

sol = find(z)
fo = open('foo2.txt', 'w')

fo.write('Case #1:\n')
for  g in range(0, z[1]):	
	fo.write("%s %s \n" % (sol[0][g] ,' '.join(map(str, sol[1][g]))))
