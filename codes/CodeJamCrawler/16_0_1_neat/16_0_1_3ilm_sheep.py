"""
    Problem number 1 of GoodleJam 2016.
"""
from __future__ import print_function

#Read input T (test cases)
n = int(raw_input().strip())

#Algorithm
for x in range(1, n+1):

    #Variables
    _set = set()
    _out = 0

    #Read test case
    _num = raw_input().strip()
    _temp = _num

    #Cout variable
    c = 1

    while(len(_set) != 10):

        #INSOMNIA Case
        if(int(_num) != 0):
            #Last number saw
            _out = int(_temp)

            #Update unordered set
            _set.update([int(item) for item in list(_temp)])

            #(i + 1) * N number
            _temp = str(int(_num) * (c + 1))

            #Increment c
            c += 1

        #Otherwise
        else:
            _out = 0
            print("Case #" + str(x) + ": INSOMNIA")
            break

    if(_out != 0):
        #Print outputs
        print("Case #" + str(x) + ": " + str(_out))
