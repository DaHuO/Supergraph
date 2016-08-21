def taskB():
    lines = [line.rstrip('\n') for line in open('B-large.in')]
    target = open('answer.out', 'w')
    caseNum = 1
    for i in lines[1:]:
        result = 1
        state = i[0]
        last = 0
        for j in range(len(i)):
            if i[j] == state:
                continue
            else:
                result += 1
                state = i[j]
                last = j
        if i == '+' * len(i):
            result = 0
        elif (last > 0) and (i[last] == '+'):
            result -= 1
        target.write("Case #" + str(caseNum) + ": " + str(result)+"\n")
        caseNum+=1
