

digits = list()

def resetDigits():
    global digits
    digits = list()
    for i in range(0,10):
        digits.append(False)


def setDigits(val):
    global digits
    while val is not 0:
        a = val%10
        digits[a] = True
        val = val/10


def allDigits():
    global digits
    ret = True
    for x in digits:
        if not x:
            ret = False
    return ret

def runCalc(N):
    global digits
    if N is 0: return "INSOMNIA"
    resetDigits()
    j = 1
    while True:
        v = N*j
        setDigits(v)
        if allDigits():
            break
        j += 1
    print N, v
    return str(v)

#open file for WRITING
filename_write = "output_large"
fw = open(filename_write, 'w')
# open file for READING:
filename = "A-large.in"
fr = open(filename, 'r')

# read number of test cases
T = fr.readline().split('\n')[0]
print T

T = int(T)
# read rest of the values accordingly
for i in range (0, T):
    readin = fr.readline().split('\n')[0]
    if (readin == ""): break
    N = int(readin)
    #for each of the values run calculations
    val = runCalc(N)
    output = "Case #" + str(i+1) + ": " + str(val) + '\n'
    #write the return from calcualations to the file for each case
    fw.write(output)

#close all files

fr.close()
fw.close()

