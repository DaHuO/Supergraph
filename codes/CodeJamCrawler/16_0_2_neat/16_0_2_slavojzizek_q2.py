#Read the number of test cases
N = input()

#Read in the inputs
inputs = []
for x in range(N):
    line = raw_input()
    inputs.append(line)

#Cycle through the test cases
k = 1
for case in inputs:
    #Set curr to keep track of last character
    #And count to track the number of distinct groups
    curr = ''
    count = 0
    for char in case:
        if char != curr:
            count += 1
            curr = char

    #If the final group is happy, subtract 1 from count
    if curr == '+':
        count += -1

    print "Case #"+str(k)+": "+str(count)
    #print case+"|"
    k += 1
