def runSheepCases(fname,outname):
    case = 0
    with open(fname,'rU') as f:
        for line in f:
            if case == 0: 
                cases = int(line)
                case+=1
                continue
            if case > cases: break
            ans = countSheep(line)
            outputCase(ans,outname,case)
            case+=1
 
def outputCase(ans,outname,case):
    if case == 1: f = open(outname,'w')
    else: f = open(outname,'a')
    f.write("Case #"+str(case)+": "+str(ans)+"\n")
          
def countSheep(line):
    base = int(line)
    digits = set()
    if base == 0: return "INSOMNIA"
    N = 0
    while len(digits) < 10:
        N += 1
        s = str(N*base)
        for char in s: digits.add(char)
    return N*base
    
      
runSheepCases("A-large.in","A-large.out")           
    