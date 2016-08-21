inp = open("input.txt")
output = open("output1.txt", "w")

for _ in range(int(inp.readline().strip())):
    string = inp.readline().strip()[ : : -1]
    count = 0
    here = 0
    N = len(string)
    while here < N:
        if count % 2:
            #print "hey"
            while here < N and string[here] != '+':
                here += 1
            here += 1
            if here <= N:
                count +=1
        
        else:
            #print "bey"
            while here < N and string[here] != '-':
                here +=1
            here += 1
            if here <= N:
                count +=1 
            
    output.write("Case #%d: %s" %(_ + 1, str(count) + '\n')) 
output.close()
