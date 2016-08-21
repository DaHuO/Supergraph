def lastNum(n):
    seen = [False for i in range(10)]
    for i in range(1,101):
        num = i*n
        numstr = str(num)
        digits = [0]*len(numstr)
        for index in range(len(numstr)):
            digits[index] = int(numstr[index])
        #print digits
        for digit in digits:
            seen[digit] = True
        if done(seen):
            return numstr
    return 'INSOMNIA'

def done(seen):
    for i in seen:
        if not i:
            return False
    return True


f = open('A-large.in','r')
out = open('out.txt','w')
case = 0
for line in f:
    if case == 0:
        case += 1
    else:
        print line
        out.write("Case #"+str(case)+": "+lastNum(int(line))+"\n")
        case+=1
