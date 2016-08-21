#By Luke Baird for Google CodeJam Qualifying round 2016
#problem A - Counting Sheep


#we start with a number N, and we do N*i (i=1, 2, 3, ...) until we have seen all 10 digits (0-9)
#we return the number we get when Bleatrix falls asleep. Google shall be forgiven for the sheep puns.

def calcFinalVal(N):
    if N==0:
        return "INSOMNIA" #Bleatrix never falls asleep
    seenDigits = []
    for i in range(1,100): #i is never greater than 100, more likely never greater than 45
        mVal = N*i
        #now we need to pull apart digits of mVal
        sVal = str(mVal)
        for s in list(sVal):
            if not s in seenDigits:
                seenDigits.append(s)
        #check to see if seenDigits has all 10
        if (len(seenDigits) > 9):
            #print("array:\n"+str(seenDigits))
            return mVal
    return "INSOMNIA"

for x in range(int(input())):
    #each test case here
    startVal = int(input())
    print("Case #"+str(x+1)+": "+str(calcFinalVal(startVal)))
