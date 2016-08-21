def runCases(fname,outname):
    case = 0
    with open(fname,'rU') as f:
        for line in f:
            if case == 0: 
                cases = int(line)
                case+=1
                continue
            if case > cases: break
            ans = countFlips(line)
            outputCase(ans,outname,case)
            case+=1
 
def outputCase(ans,outname,case):
    if case == 1: f = open(outname,'w')
    else: f = open(outname,'a')
    f.write("Case #"+str(case)+": "+str(ans)+"\n")
          
def countFlips(line):
    numFlips = 0
    line = [c for c in line if c == "+" or c == "-"]
    for i in range(len(line)-1):
        if line[i] == "+" and line[i+1] == "-": numFlips += 1
        elif line[i] == "-" and line[i+1] == "+": numFlips += 1
    if line[-1] == "-": numFlips += 1
    return numFlips
        
runCases("B-large.in","B_large.out")   