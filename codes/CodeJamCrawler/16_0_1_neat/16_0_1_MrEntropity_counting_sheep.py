import sys

def chkList(l):
    if 0 in l:
        return False
    return True

def fillTbl(val, tbl):
    sval = str(val)

    for ch in sval:
        tbl[int(ch)] = 1


def solve(N):
    stbl = [0,0,0,0,0,0,0,0,0,0]
    found = False
    mult = 1

    if N == 0:
        return "INSOMNIA"
    else:
        # Search solution
        while(not found):
            val = mult*N
            # Analyze the current value:
            fillTbl(val, stbl)
            found = chkList(stbl)
            
            if found:
                return str(val)
            mult = mult + 1
    return str(1)

    

def main(argv):
    fName = argv[1]
    try:
        infile = open(fName)
    
        # Read the number of tests:
        NoOfTests = int(infile.readline())
    
        if NoOfTests < 1 or NoOfTests > 100:
            return 2

        # Calculate solution for each test case: 
        for idx in range(0, NoOfTests):
            N = int(infile.readline())
    
        
            if (N < 0):
                return 3
            if (N > 10**8):
                return 4

            print ("Case #" + str(1+idx) + ": " + solve(N))
            
        # At least we did not fine any errors...
        infile.close()
        return 0
    except:
        infile.close()
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

