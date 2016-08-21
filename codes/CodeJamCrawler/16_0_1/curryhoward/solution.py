import sys
data = sys.stdin.readlines()

def solve_prob(i, N):
    res = ""
    if N == 0:
        res = "INSOMNIA"
    else:
        solved = False
        seenMap = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        subject = N
        j = 1
        while not solved:
            subject = j * N
            j += 1
            # iterate digits, adding them to seenMap when seen
            numStr = str(subject)
            # print "   "+numStr
            for k in range(0, len(numStr)):
                seenMap[numStr[k]] += 1

            #check if seen all digits
            seenAll = True
            for key in seenMap:
                if seenMap[key] == 0:
                    seenAll = False
                    break;
            if seenAll is True:
                solved = True

        # if we get here, we solved it
        res = str(subject)
    #print solution
    print "Case #"+str(i)+": "+res

    #if i == 3:
    #    exit()

T = int(data[0])
for i in range(1,T+1):
    N = int(data[i])
    solve_prob(i, N)
