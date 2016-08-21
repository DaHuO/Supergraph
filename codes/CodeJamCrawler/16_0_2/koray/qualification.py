import sys



input = open("input.in")
output = open("output.out", "w")
testCases = int(input.readline())



def qualificationB():

    for testCase in range(1, testCases + 1):
        ret = 0;
        x = input.readline()
        x = x.rstrip()
        for i in range(1 , len(x)):
            if(x[i] != x[i-1]):
                ret += 1;
        if( (x[0] == "-" and ret % 2 == 0) or (x[0] == "+" and ret % 2 == 1) ):
            ret +=1;
        # print x
        print >> output, "Case #" + str(testCase) + ": " + str(ret)
        print "Case #" + str(testCase) + ": " + str(ret)


if __name__ == "__main__":
    # qualificationA()
    qualificationB()
    # qualificationC()
    # qualificationD()
