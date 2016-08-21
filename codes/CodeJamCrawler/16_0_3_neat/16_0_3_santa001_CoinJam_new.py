import sys
from math import sqrt
from itertools import count, islice

def isPrime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def conToBaseN(num, base):
    temp = num
    sum = 0
    itr = 0;

    while (temp > 0):
        sum += (base ** itr) * (temp % 10)
    	temp /= 10
    	itr += 1
    return sum


def notPrime(num):
    temp = num/2
    i = 2
    while (i <= temp):
    	if ((num % i) == 0):
		return i
	i += 1
    else:
	return 0


def get_result(num):
	array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        base = 2
        val = 0

        while (base < 11):
		val = conToBaseN(num, base)
		if isPrime(val):
			return array, False
                ret = notPrime(val)
		array[base-2] = ret
		base += 1
	return array, True
        

def Solve(max_num, min_num):
    cur = min_num
    array = [0, 0, 0, 0, 0, 0, 0, 0, 0] 

    while (cur <= max_num):
        conv = int(bin(cur)[2:])
	array, success = get_result(conv)
        if (success == True):
		return array, True, cur, conv
	cur += 2

    return array, False, cur, 0


if __name__ == "__main__":
    T = int(raw_input())
    i = 0

    while i < T:
        temp = raw_input()
        N = int(temp.split()[0])
        J = int(temp.split()[1])
        k = 0
        max_num = 2**(int(N)) - 1
        min_num = 2**(int(N-1)) + 1

        print "Case #%d:" %(i+1)
	while k < J:
		array, ret, num, val = Solve(max_num, min_num)
	        print "%d" %(val),
		for m in array:
			print m,
                print
		k += 1
		min_num = num + 2
        i += 1
