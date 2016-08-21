import time
import itertools

outFile = "output.out"
inFile = "C-large.in"

##def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
##    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def unique_permutations(seq):
    """
    Yield only unique permutations of seq in an efficient way.

    A python implementation of Knuth's "Algorithm L", also known from the 
    std::next_permutation function of C++, and as the permutation algorithm 
    of Narayana Pandita.
    """

    # Precalculate the indices we'll be iterating over for speed
    i_indices = range(len(seq) - 1, -1, -1)
    k_indices = i_indices[1:]

    # The algorithm specifies to start with a sorted version
    seq = sorted(seq)

    while True:
        yield seq

        # Working backwards from the last-but-one index,           k
        # we find the index of the first decrease in value.  0 0 1 0 1 1 1 0
        for k in k_indices:
            if seq[k] < seq[k + 1]:
                break
        else:
            # Introducing the slightly unknown python for-else syntax:
            # else is executed only if the break statement was never reached.
            # If this is the case, seq is weakly decreasing, and we're done.
            return

        # Get item from sequence only once, for speed
        k_val = seq[k]

        # Working backwards starting with the last item,           k     i
        # find the first one greater than the one at k       0 0 1 0 1 1 1 0
        for i in i_indices:
            if k_val < seq[i]:
                break

        # Swap them in the most efficient way
        (seq[k], seq[i]) = (seq[i], seq[k])                #       k     i
                                                           # 0 0 1 1 1 1 0 0

        # Reverse the part after but not                           k
        # including k, also efficiently.                     0 0 1 1 0 0 1 1
        seq[k + 1:] = seq[-1:k:-1]

def divisor(num, maxTime=-1):
    startTime = time.time()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return i
        if maxTime >= 0 and time.time() - startTime >= maxTime:
            break
    return num

def factorsInBases(numStr, minBase, maxBase):
    lst = list()
    for b in range(minBase, maxBase+1):
        numInBase = int(numStr, base=b)
        factor = divisor(numInBase, 0.01)
        if factor == numInBase:
            factor = 0
        lst.append(factor)
    return lst


def generateCoins(length, numCoins):
    numToGenerateInside = length - 2
    numZeros = minZeros = 0
    maxZeros = numToGenerateInside - numToGenerateInside % 2
    #donePermutations = set()
    solutions = list()
    while len(solutions) < numCoins and numZeros <= maxZeros:
        curInside = "0"*numZeros + "1"*(numToGenerateInside-numZeros)
        permutations = unique_permutations(curInside)
        i = 0
        for perm in permutations:
##            if perm in donePermutations:
##                continue
##            donePermutations.add(perm)
            perm = "1"+ "".join(perm) +"1"
            factors = factorsInBases(perm, 2, 10)
            if 0 in factors:
                continue
            solutions.append((perm, factors))
            print("Currently " + str(len(solutions)) + " solutions")
            if len(solutions) >= numCoins:
                break
        numZeros += 2
    return solutions

def generateProofStr(solutionStr, factors):
    outStr = solutionStr + " " + " ".join(factors)
    return outStr
            

with open(inFile, "r") as f:
    with open(outFile, "w") as of:
        num = int(f.readline())
        content = [x.strip('\n').split(" ", 1) for x in f.readlines()]
        for i in range(num):
            N = int(content[i][0])
            J = int(content[i][1])
            solutions = generateCoins(N, J)
            print("Generated coins")
            of.write("Case #" + str(i+1) + ":\n")
            #a = 1
            for solution in solutions:
                sStr = solution[0]
                factors = [str(s) for s in solution[1]]
                proofStr = generateProofStr(sStr, factors)
                #print("Factoring: " + str(int(solution, base=2)))
                #a += 1
                of.write(proofStr + "\n")
print("done!")
