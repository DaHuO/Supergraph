def allSeen(digits):
    result = True
    for i in range(0, 10):
        result = result and digits[i]
    return result

def mark(digits, N):
    #print("mark({}, {})".format(digits, N))
    N = str(N)
    numDigits = len(N)
    for i in range(0, numDigits):
        digits[int(N[i])] = True

def getAnswer(N):
    digits = {}
    for j in range(0, 10):
        digits[j] = False

    if N == 0:
        return "INSOMNIA"

    currentCount = N
    mark(digits, N)  
    while allSeen(digits) == False:
        currentCount = currentCount + N
        mark(digits, currentCount)
    return currentCount    

T = int(input())  # read number of cases

for i in range(1, T + 1): # starting with 2 to avoid first line (TODO: remove)
    N = [int(s) for s in input().split(" ")][0]


    result = getAnswer(N)
    print("Case #{}: {}".format(i, result))


