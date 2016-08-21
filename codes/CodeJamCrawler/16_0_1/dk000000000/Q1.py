def CountShip(n):
    digit = []
    lastnumber = ""
    for t in range(1,100):
        temp = str(n*t)
        for ch in temp:
            if ch not in digit:
                digit.append(ch)
        if len(digit)==10:
            lastnumber = temp
            break
    return lastnumber

if __name__ == "__main__":
    cases = int(raw_input())
    ns = []
    for t in range(cases):
        ns.append(long(raw_input()))
    for t in range(cases):
        output = ""
        lastnum = CountShip(ns[t])
        if lastnum == "":
            output = "INSOMNIA"
        else:
            output = lastnum
        print "Case #{}: {}".format(t+1,output)
        
    
    
        
