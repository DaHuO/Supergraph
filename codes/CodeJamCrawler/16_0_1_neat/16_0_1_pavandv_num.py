T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    if N == 0:
        print "Case #" + str(i+1) + ": "  + "INSOMNIA"
    else:    
        map = {}
        multiplier = 1;
        result = 0;
        while len(map) < 10:
            result = str(multiplier*N);
            for char in result:
                map[char] = True
            multiplier +=1        
        print "Case #" + str(i+1) + ": "  + result