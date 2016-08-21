def code_jam():
    lines = [line.rstrip('\n') for line in open('A-large.in')]
    target = open('answer.out', 'w')
    #lines = [123, '6 1011021']
    caseNum = 1
    for i in lines[1:]:
        dct = {}
        count = 1
        flag = True
        result = 0
        while len(dct) < 10:
            result += 1
            if (count == 10) and (len(dct) == 1):
                target.write("Case #" + str(caseNum) + ": INSOMNIA\n")
                flag = False
                break
                
            N = str(result * int(i))
            for j in range(len(N)):
                dct[N[j]] = '1'
            count += 1
        if flag:
            target.write("Case #" + str(caseNum) + ": " + str(result*int(i))+"\n")
        caseNum+=1

    
                
        
        
