def runCases(fname,outname):
    case = 0
    with open(fname,'rU') as f:
        for line in f:
            if case == 0: 
                cases = int(line)
                case+=1
                continue
            if case > cases: break
            ans = cleanTiles(line)
            outputCase(ans,outname,case)
            case+=1

def outputCase(ans,outname,case):
    if case == 1: f = open(outname,'w')
    else: f = open(outname,'a')
    f.write("Case #"+str(case)+": "+str(ans)+"\n")
    
def cleanTiles(line):
    splitline = line.split(" ")
    K = int(splitline[0])
    C = int(splitline[1])
    S = int(splitline[2])
    if K == S: 
        ans = "1"
        for i in range(2,S+1):
            ans += " "+str(i)
        return ans
    return None
    
runCases("D-small-attempt0.in","D-small.out")
    
        