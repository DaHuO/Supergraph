import re


T = int(input())

for t in range(T):
    inp = raw_input()
    cor = "+"*len(inp)
    
    cnt = 0;
    while inp != cor:
        cnt = cnt+1
        
        err = re.search(r'[^'+inp[0]+']', inp)
        if err is None: err = len(inp)
        else: err = err.start()
                
        if inp[0] == '-':
            inp = err*'+' + inp[err:]
        else:
            inp = err*'-' + inp[err:]
       
    print "Case #{0}: {1}".format(t+1, cnt)
        
