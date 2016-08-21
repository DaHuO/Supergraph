def solve_2(pancakes, count):
    #print pancakes
    wrong = -1
    for i in range(len(pancakes)):
        if pancakes[i]!='+':
            wrong = i

    if wrong==-1:
        return count

    else:
        first = pancakes[0]
        if first=='+':
            i=0
            while pancakes[i]=='+':
                pancakes[i]='-'
                i+=1
            return solve_2(pancakes, count+1)
        else:
            i=0
            while i<len(pancakes) and pancakes[i]=='-':
                pancakes[i]='+'
                i+=1
            return solve_2(pancakes, count+1)



nCases = int(raw_input())
for i in range(nCases):
    n = list(raw_input())
    print "Case #"+str(i+1)+": "+str(solve_2(n, 0))

#for i in range(1000000):
    #print solve_1(i)
