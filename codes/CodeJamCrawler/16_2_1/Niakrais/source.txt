fout = open("output.txt", 'w')
for t in range(1, T + 1):
#     print("test {}".format(t))
    answer = []
    s = i[t]
    
    newS = s
    for u, ind in unicsF:
        needToContinue = True;
        while needToContinue:
            newS, needToContinue = findAndDelete(newS, alpha[ind], u)
            if needToContinue:
                answer.append(ind)
                
    for u, ind in unicsS:
        needToContinue = True;
        while needToContinue:
            newS, needToContinue = findAndDelete(newS, alpha[ind], u)
            if needToContinue:
                answer.append(ind)
    
    answer.sort()
    outL = "Case #"+ str(t) + ": " + ''.join(map(str,answer)) + "\n"
    print(outL)
    fout.write(outL)
fout.close()
    
