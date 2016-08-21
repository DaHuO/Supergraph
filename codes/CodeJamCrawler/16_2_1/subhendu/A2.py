# Google Code Jam 2016 Round 1B Problem A.  Getting the Digits
digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

memory ={}

def solve(s):
    res = []
    sl = [c for c in s]
    rc,res = solveA(sl)
    return "".join(str(i) for i in res)

def solveA(sl):
    key = tuple(sl)
    if len(sl) < 3:
        return True , []
    if key in memory :
        return memory[key]

    res = []
    anyFound = False
    for i,d in enumerate(digits):
        found = True
        while(found):
            sb = sl[:]
            for dc in d:

                if dc not in sl:
                    found = False
                    break
                else:
                    sl.remove(dc)

            if found:
                
                rc , res2 = solveA(sl[:])
                if (not rc):
                    found = False
                    sl = sb[:]
                else:
                    res.append(i)
                    anyFound = True
                    memory[key]= (rc and True,res+res2)
                    return True,res+res2
            else:
                sl = sb[:]

    if anyFound:
        rc , res2 = solveA(sl[:])
        if (not rc):
            memory[key]= (False,[])
            return False,[]
        else:
            memory[key]= (rc and True,res+res2)
            return rc and True , res+res2
    else:
        memory[key]= (False,[])
        return False,[]


if __name__ == "__main__":
    t = int(input())
    for ti in range(1, t + 1):
        s = input().strip()
        res = solve(s)
        print("Case #{0}: {1}".format(ti, res))
