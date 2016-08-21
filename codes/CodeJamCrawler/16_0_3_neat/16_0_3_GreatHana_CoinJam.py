def prime(num): #find whether num is a prime
    up = int(num**0.5)
    for i in range(2, up):
        if num%i == 0:
            #return False
            return i
    #return True
    return 0


def CoinJam(N, J):
    mustadd = {base:base**(N-1)+1 for base in range(2,11)}
    valid_jamcoins = []
    tried_jamcoins = set()
    while len(valid_jamcoins) < J:
        # randomly get a possible jamcoin
        import random
        S = ""
        for i in range(N-2):
            c = str(random.randrange(0,2))
            S += c
        jamcoin = "1" + S + "1"
        if jamcoin in tried_jamcoins:
            continue
        tried_jamcoins.add(jamcoin)
        # validation
        valid_divisors = []
        for base in range(2,11):
            interpretation = sum([int(S[i])*(base**(N-2-i)) for i in range(N-2)]) + mustadd[base]
            vn = prime(interpretation)
            if vn == 0:
                break
            valid_divisors.append(str(vn))
            #print(interpretation)
        if vn == 0:
            continue
        tmp = [jamcoin]
        tmp.extend(valid_divisors)
        valid_jamcoins.append(tmp)
    out = ""
    for vj in valid_jamcoins:
        out = out + " ".join(vj) + "\n"
    return out

def ansCoinJam(n, tests):
    output = ""
    for i in range(n):
        test = TestCase[i]
        N = int(test.split()[0])
        J = int(test.split()[1])
        outputline = "Case #" + str(i+1) + ":\n" + CoinJam(N,J)
        output = output + outputline + "\n"
    #output_file = open("CoinJam_output.txt", "w")
    output_file = open("C-small_output"+attempt+".txt", "w")
    output_file.write(output)
    output_file.close()

import sys
# transfer TestCase from file to input suitable for the function
TestCase = []
#testname = sys.argv[1]
attempt = str(sys.argv[1])
testname = "C-small-attempt" + attempt + ".in.txt"
test_file = open(testname, "r")
n = 0
for line in test_file:
    if n == 0:
        n = int(line)
    else:
        TestCase.append(line.rstrip('\n'))
test_file.close()
# start 
ansCoinJam(n, TestCase);
