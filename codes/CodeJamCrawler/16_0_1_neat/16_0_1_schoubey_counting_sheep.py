import sys
import numpy as np
std_in = sys.stdin

num_found = [0,0,0,0,0,0,0,0,0,0]

def setnum_found(N, num_found):
    S = str(N)
    for i in range(len(S)):
        num_found[int(S[i])] = 1
    return num_found

def check(nf):
    for i in range(len(nf)):
        if nf[i] == 0:
            return 0
    return 1

def main():
    num_found = [0,0,0,0,0,0,0,0,0,0]
    no_of_cases = int(std_in.readline())
    for i in range(no_of_cases):
        for j in range(10):
            num_found[j] = 0
    
        N = int(std_in.readline())
        if N == 0:
            print("Case #" + str(i+1) + ": INSOMNIA")
        else:
            cur = N
            num_found = setnum_found(N, num_found)
            k = 1
            while check(num_found) != 1:
                k = k + 1
                cur = N * k
                num_found = setnum_found(cur, num_found)
            print("Case #" + str(i+1) + ": " + str(cur))

main()