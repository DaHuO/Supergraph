




def countsheep(n):
    if n == 0:
        return "INSOMNIA"
    else:
        number = n
        currnumber = 0
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        newdigits = ["0","1","2","3","4","5","6","7","8","9"]
        i = 1
        while newdigits != []:
            currnumber = number * i
            i = i + 1;
            digits = newdigits
            newdigits = []

            for d in digits:
                if str(currnumber).find(d) == -1:
                    newdigits.append(d)

        return currnumber


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
        print "Case #"+str(iter)+": "+ str(countsheep(int(n)))
        s = s + "Case #"+str(iter)+": "+ str(countsheep(int(n))) + "\n"
    iter = iter + 1
g.write(s)



