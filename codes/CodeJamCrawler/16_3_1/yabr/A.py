def func(P):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    output = ""

    while True:
        numZeros = P.count(None)

        if numZeros == len(P):
            return output

        minimum = min(filter(None, P))
        maximum = max(filter(None, P))

        index = P.index(maximum)

        if minimum == maximum and numZeros == (len(P) - 2):
            output += str(letters[index])
            if P[index] == 1:
                P[index] = None
            else:
                P[index] -= 1

            index = P.index(minimum)
            output += str(letters[index])
            if P[index] == 1:
                P[index] = None
            else:
                P[index] -= 1
        else:
            if P[index] == 1:
                P[index] = None
            else:
                P[index] -= 1

            output += str(letters[index])

        output += " "

T = int(input())

for t in range(T):
    N = int(input())
    P = input().split(' ')
    P = list(map(int, P))
    print('Case #' + str(t+1) + ': ' + func(P))

