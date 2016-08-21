from collections import deque
from sets import Set

input = open('./A-small-attempt1.in', 'r').readlines()
output = open('./A-small-attempt1.out', 'w')

inputQueue = deque(input)
testCases = int(inputQueue.popleft())
for i in range(1, testCases+1):
    init_n = int(inputQueue.popleft())
    set = Set()
    count = 1
    n = init_n
    while True:
        #print "n "+str(n)
        n = init_n * count
        tmp = n
        while tmp != 0:
            set.add(tmp%10)
            tmp = tmp / 10

        #print "set "+str(set)
        count += 1
        if len(set) == 10:
            outputString = str(n)
            break
        if count == 100:
            outputString = "INSOMNIA"
            break
    print outputString
    output.write("Case #"+str(i)+": "+outputString+"\n")
output.close()