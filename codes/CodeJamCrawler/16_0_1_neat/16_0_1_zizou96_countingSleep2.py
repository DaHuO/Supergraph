#!/usr/bin/python3

testNb = int(input())
for test in range(1,testNb+1) :
    digit = [0,1,2,3,4,5,6,7,8,9]
    N = int(input())

    j = 1
    while len(digit) != 0 :
        for i in str(N*j) :
            if int(i) in digit :
                digit.remove(int(i))
        j += 1
        if j > 10**6 :
            break

    if j > 10**6:
        print("Case #" + str(test) + ": " + "INSOMNIA")
    else :
        print("Case #" + str(test) + ": " + str((j-1)*N))
