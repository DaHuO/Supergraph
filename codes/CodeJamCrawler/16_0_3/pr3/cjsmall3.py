import sys
import math
import time
## Promila Agarwal
## March 12, 2016
## Jam Coin 

def Pogo():
	
	in_f = open('C-small-attempt0.in', 'r')
	out_f = open('jam_out_l.txt', 'w')
	num_of_case = int(in_f.readline().rstrip('\n'))
	for i in range(1, num_of_case+1):
		jam_coin(in_f, out_f, i)
	

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True, 0
    if n == 3:
        return True, 0
    if n % 2 == 0:
        return False, 2
    if n % 3 == 0:
        return False, 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False, i

        i += w
        w = 6 - w

    return True, 0

def gen_all_sequences(outcomes, length):
    '''
    iterative function that enumerates the set of all sequences of outcomes of given length;
    original code from the lecture, do not modify
    '''
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def convertB(in_str,base):
    lin = len(in_str)
    num = 0
    for i in range(lin):
        if (in_str[i] == 1):
            num += 1*base** (lin-1-i)
            
    return num

def getDiv(num, base):
    for i in range(2,num):
        if (num % i == 0):
            return i
    return 0
    
    

def jam_coin(in_f, out_f, case_index):
	in_s = in_f.readline().rstrip('\n').split(" ")
	N = int(in_s[0])
	J = int(in_s[1])

	A1 = gen_all_sequences([0,1], N)
	A = list(A1)
	lenA = len(A)

	numA = 0
	i = 0
	out_f.write("Case #{}: \n".format(case_index))
	while (i < J) and (numA < lenA) :
		
		if (A[numA][0] == 1) and (A[numA][-1] == 1):
			list1 = []
			list2 = []
			for j in range(2,11):
				b = convertB(A[numA],j)
				result, div1 = isprime(b)
            
				if result:
					break
				else :
					#div = getDiv(b,j)
					#list1.append(div)
					list2.append(div1)
					if (j == 10) :
						# get the divisors for this number
						i +=1
						str1 = ''.join(map(str, A[numA]))
						str2 = ' '.join(map(str, list2))
						#print str1+" "+str2
						#print str2
						#print list2
						str3 = str1+" "+str2
						out_f.write("{}\n".format(str3))
						
						
		numA +=1
	
	#out_f.write("Case #{}: {}\n".format(case_index, str1))
	#out_f.write("Case #{}: \n{}".format(case_index, str1))
	return 
	
if __name__ == '__main__':    
    Pogo()
