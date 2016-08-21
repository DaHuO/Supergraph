import sys



input = open("input.in")
output = open("output.out", "w")
testCases = int(input.readline())

def qualificationB():
    for testCase in range(1, testCases + 1):
        ret = 0
        x = input.readline()
        x = x.rstrip()
        for i in range(1 , len(x)):
            if(x[i] != x[i-1]):
                ret += 1
        if( (x[0] == "-" and ret % 2 == 0) or (x[0] == "+" and ret % 2 == 1) ):
            ret +=1
        print >> output, "Case #" + str(testCase) + ": " + str(ret)
        print "Case #" + str(testCase) + ": " + str(ret)

def qualificationC():
    N = 32;
    J= 500;
    print >> output, "Case #" + str(1) + ": "
    for i in range(0 , J):
        number = "11"
        for c in bin(i)[2:].zfill( (N-4)/2 ):
            number += "11" if c =="1" else "00"
        number += "11"
        print >> output, number + " 3 2 5 2 7 2 3 2 11"



def qualificationA():
    for testCase in range(1, testCases + 1):
        ret = 0
        list = [False] * 10
        x = input.readline()
        for i in range(1 , 1000):
            ret = str(int(x) * i)
            for c in ret:
                list[ord(c) - 48] = True
            if not any(not item for item in list):
                break
        if any(not item for item in list):
            print >> output, "Case #" + str(testCase) + ": INSOMNIA"
            print "Case #" + str(testCase) + ": INSOMNIA"
        else:
            print "Case #" + str(testCase) + ": " + str(ret)
            print >> output, "Case #" + str(testCase) + ": " + str(ret)


if __name__ == "__main__":
    # qualificationA()
    # qualificationB()
    qualificationC()
    # qualificationD()
