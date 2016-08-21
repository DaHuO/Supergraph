#Read the number of test cases
N = input()

#Read in the inputs
inputs = []
for x in range(N):
    line = raw_input()
    inputs.append(line)

#Cycle throgh the words
c = 1
for S in inputs:
    answer = ''
    n = 0
    for char in S:
        if n == 0:
            answer = answer+char
        else:
            if char >= answer[0]:
                answer = char+answer
            else:
                answer = answer+char
        n +=1

    print "Case #"+str(c)+": "+answer
    c+=1
