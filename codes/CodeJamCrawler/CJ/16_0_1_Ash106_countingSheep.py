#open the file
file = open('A-large.in','r')
lines = file.readlines()

# number of test cases
T = int(lines[0])

# number picked
N = 0

# list of digits needed
digitsNeeded = [0,1,2,3,4,5,6,7,8,9]

for testCase in range(1, T+1):
    if(int(lines[testCase]) == 0):
        print("Case #"+str(testCase)+": INSOMNIA")

    else:
        # list of digits had
        digitsHad = []
        multiplier = 1
        N = int(lines[testCase].strip())
        while(digitsNeeded != sorted(digitsHad)):
            numToParse = N*multiplier
            for digit in str(numToParse):
                if int(digit) not in digitsHad:
                    digitsHad.append(int(digit))
            multiplier+=1

        print("Case #"+str(testCase)+": "+str(numToParse))
