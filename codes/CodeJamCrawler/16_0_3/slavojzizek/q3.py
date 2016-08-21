#Import itertools
import itertools

#Read the number of test cases
T = input()

#Read in the jamcoin length and number of inputs
N, J = [int(x) for x in raw_input().split()]

#List the bases and initialise list of jamcoins
bases = [2,3,4,5,6,7,8,9,10]
jamcoins = []

#Generate the candidate jamcoins
candidates = ['10000000000000000'+"".join(val)+'1' for val in itertools.product("01", repeat=16-2)]

#Function to find first non-trivial factor of integer
def findFactor(a):
    factor = 0
    i = 0
    while i < a and i < 1000:
        if i > 1 and a % i == 0:
            factor = i
            break
        i = i+1

    return factor

#Cycle through candidates looking for jamcoins
for c in candidates:
    proofs = []
    for b in bases:
        #Evaluate candidate in base b
        baseTen = int(c,b)
        factor = findFactor(baseTen)
        proofs.append(factor)

    #If no 0's, this is a jamcoin
    if 0 in proofs:
        pass
    else:
        jamcoins.append([c, proofs])

    #Exit on J jamcoins
    if len(jamcoins) >= J:
        break

print "Case #1:"
for j in jamcoins:
    print str(j[0])+" "+" ".join([str(val) for val in j[1]])
