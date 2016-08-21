def getanswer(p):
    answer = ""
    answer = answer +  p[0]
    p = p[1:]

    for i in p:
        if i == max(answer + i):
            answer = i + answer
        else:
            answer = answer + i

    return answer





f = open('testcases', 'r')
g = open('output', 'w')
content = f.readlines()
numOfCases = int(content[0])
iter = 0
s = ""
for n in content:
    if iter == 0:
        pass
    else:
        print "Case #"+str(iter)+": "+ str(getanswer(n))
        s = s + "Case #"+str(iter)+": "+ str(getanswer(n))
    iter = iter + 1
g.write(s)