import utils

def removeTwo(total,la,lb,ps):
    remo = total - 2 
    if remo == 0:
        return True
    flag = True
    for i in range(len(ps)):
        if la == i:
            if (ps[la] -1) / float(remo) > 0.5:
                flag = False
                return flag
        elif lb == i:
            if (ps[lb] -1) / float(remo) > 0.5:
                flag = False
                return flag
        else:
            if ps[i] / float(remo) > 0.5:
                flag = False
                return flag
    return flag

if __name__ == "__main__":
    inputFile = "inputQ1"
    inputFile = "test"
    inputFile = "A-small-attempt1.in"
    #inputFile = "A-large.in"
    #inputFile = "A-large.in.txt"
    #inputFile = "inputQ3"
    outputFile = "outputQ1"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.strip()
    vec = {0:'A',1:'B',2:'C'}
    for index in range(1, int(cases) + 1):
        print "case ", index
        rowData = inputData.next()
        rowData = rowData.strip()
        N = int(rowData)
        rowData = inputData.next()
        rowData = rowData.strip()
        P = rowData.split(' ')
        ps = [int(p) for p in P]
        total = sum(ps)
        print total
        print ps
        s = []
        while total > 0:
            m1 = -1
            m2 = -1
            la = -1
            lb = -1
            print ps
            for i in range(len(ps)):
                if ps[i] > m1:
                    la = i
                    m1 = ps[i]
            for i in range(len(ps)):
                if i == la:
                    continue
                if ps[i] > m2:
                    lb = i
                    m2 = ps[i]
        
                print 'lb loop', la, lb
            print s
            if removeTwo(total, la,lb,ps):
                s.append(vec[la] + vec[lb])  
                ps[la] -= 1
                ps[lb] -= 1
                total -= 2
            else:
                s.append(vec[la])
                ps[la] -= 1
                total -= 1
            
        output = ' '.join(s)
        outputString = "Case #" + str(index)+ ": " + output + "\n"
        print outputString
        outputData.write(outputString)
                
            
