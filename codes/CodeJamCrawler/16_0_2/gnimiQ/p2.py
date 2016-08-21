import sys
debug = False


def answer(S):
    S = list(filter(lambda x: x == '+' or x == '-', S))
    # length
    l = len(S)
    # sum
    sum = 0
    for i in range(0,l-1):
        # for every change of direction
        # at least one flip is needed
        if S[i] != S[i+1]:
            sum += 1

    if S[l-1] == '-':
        sum += 1
    if debug:
        print(S)
        print("length: " + str(l))
    return sum


if __name__ == '__main__':
    filenm = list(sys.argv)[1]
    f = open(filenm, 'r')
    csnmbr = f.readline()
    if debug:
        print("case number: " + csnmbr )
    counter = 0
    for line in f:
        counter += 1
        r = answer(line)
        print("Case #" + str(counter) + ": " + str(r))
        

    
