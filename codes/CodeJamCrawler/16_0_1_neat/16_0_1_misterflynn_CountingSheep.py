from array import *

# Bleatrix number is the final of a sequence of numbers N, N*2, N*3..
# given a number N such that the digits of all the numbers in the sequence
# minimally span 0 through 9.
def GetBleatrixNumber(N):
    decimalsFound = array('b', [0 for i in range(10)]);
    numDecimalsFound = 0
    multiplier = 1

    if N == 0:
        return -1

    while numDecimalsFound < 10:
        currentNumber = multiplier * N
        decimalString = currentNumber

        while decimalString != 0:
            decimal = decimalString % 10
            decimalString //= 10

            if decimalsFound[decimal] == 0:
                decimalsFound[decimal] = 1
                numDecimalsFound += 1

        multiplier += 1

    return currentNumber

numTests = int(raw_input())
for i in range(1, numTests + 1):
    N = int(raw_input())
    num = GetBleatrixNumber(N)

    if num < 0:
        print("Case #{}: INSOMNIA".format(i))
    else:
        print("Case #{}: {}".format(i, num))
