import sys
f = sys.stdin
cases = int(f.readline())
for case in range(1,1+cases):
    string = f.readline()
    res = 0
    
    while "-" in string:
        length = len(string)
        origin = string[0]
        replace = "-" if origin == "+" else "+"
        new = string.lstrip(origin) 
        string = replace * (length - len(new)) + new
        res += 1
    
    print "Case #%d: %d" % (case, res)
        
