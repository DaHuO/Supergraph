#!/usr/bin/env python

variable = 0

def checkarr(array):
    for i in range(0,10):
    	if array[i] == 0:
		return 0
    return 1

def findnums(N):
    #         0 1 2 3 4 5 6 7 8 9
    digits = [0,0,0,0,0,0,0,0,0,0]
    num = N
    orig = N
    count=0
    while checkarr(digits) != 1:
    	count=count+1
    	num = N*count
    	while (num>0):
       	    digit = num%10
       	    num=num/10
            digits[digit] = 1
	if count > 1000000:
	    return -1
    N=N*(count)
    return N

if __name__ == "__main__":
    """ Usage:  ./small.py input.txt > output.txt """
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1,T+1):
        N = long(f.readline())
	if N != 0:
	    N = findnums(N)
            print("Case #{0}: {1}".format(case, N))
	else:
	    print("Case #{0}: INSOMNIA".format(case))
