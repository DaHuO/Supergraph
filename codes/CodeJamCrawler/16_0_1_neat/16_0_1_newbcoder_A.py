#!/usr/bin/python

import sys

def find_last(N):
    nums = list(map(str, list(range(10))))
    #print(nums)
    cur = 0
    if N == 0:
        return "INSOMNIA"
    for i in range(1,100000):
        cur += N
        #print("Curr : i*N = {:} * {:} = {:}".format(i,N,i*N))
        for num in list(nums):
            if num in str(cur):
                #print("REMOVING {:}".format(num))
                #if num == '2':
                #    print('-'*10)
                #    print('before remove')
                #    print(nums)
                #    nums.remove(num)
                #    print('after remove')
                #    print(nums)
                #    print('-'*10)
                #else:
                #    if num == '2' and '2' in str(i*N):
                #        print("WUT")
                #    nums.remove(num)
                nums.remove(num)

            if len(nums) == 0:
                return N*i
        #print("nums = ")
        #print(nums)
    if len(nums) == 0:
        return 10 * N
    return "INSOMNIA"

with open(sys.argv[1], 'r') as f:
    cases = int(f.readline())
    for case in range(cases):
        N = int(f.readline())
        ans = find_last(N)
        print("Case #{:}: {:}".format(case+1, ans))


