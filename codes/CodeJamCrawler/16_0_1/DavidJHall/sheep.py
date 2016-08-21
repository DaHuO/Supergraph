import time
trials = 100000000

infilename ='A-large.in'

def solve(number):
    seen = str(number)
    tester = 0
    for i in range(1,trials):
        tester = number*i
        seen += str(tester)
        if len(set(str(seen)))==10:
            # print "bingo!", tester, number
            return tester
    return "INSOMNIA"

def altsolve(number):
    seen = {}
    numberstring =""
    for i in range(1,trials):
        tester = number*i
        numberstring = str(tester)
        for i in numberstring:
            seen[i] = True
        # print len(seen)
        if len(seen) >= 10:
            # print 'Bingo', tester
            return tester
    return 'Insomnia'


timestart = time.time()
iterations = 0
problem = []

f = open(infilename, 'r')
iterations = int(f.readline())
for i in range(0,iterations):
    print i
    problem.append(int(f.readline().strip()) )


fw = open('out2.txt', 'w')
print problem
num = 1
answer = ''
for i in problem:
    answer=str(altsolve(i))
    print "Case #"+str(num)+": "+answer
    fw.writelines("Case #"+str(num)+": "+answer+"\n")
    num +=1


print time.time()-timestart





