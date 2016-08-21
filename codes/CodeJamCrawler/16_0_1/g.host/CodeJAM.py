def parseIn(inputFile):
    cases = 0
    case_N =[]
    with open(inputFile,"r") as f_in:    
        cases = int(f_in.readline())
        for line in f_in.readlines():
            N = [long(i) for i in line.split()]
            case_N.append(N)
    f_in.closed

    return cases, case_N
def parseOut(finList):
    with open("A-large.out",'w') as f_out:
        for i in range(len(finList)):
            x = 'Case #{}: {}\n'.format(i+1,finList[i])
            f_out.write(x)
    f_out.closed

def main():
    cases, case_N = parseIn("A-large.in")
    finVal = []
    for case in range(cases):
        Visited = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        Num = case_N[case][0]
        i = 0
        while Visited != [] and (Num != 0):
            i += 1
            copy = Num*i
            while copy != 0:
                x = copy%10
                if x in Visited:
                    a = Visited.index(x)
                    Visited.pop(a)
                copy /= 10
        if Num == 0:
            finVal.append('INSOMNIA')
        else:
            finVal.append(Num*(i))
    parseOut(finVal)

main()