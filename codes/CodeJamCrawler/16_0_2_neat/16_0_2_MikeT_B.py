f = open('B-large.in', 'r')
fout = open('out.txt', 'w')

T = int(f.readline())

for t in range(T):
    pcakes = f.readline().strip()
    
    flips = 0
    currentRun = pcakes[0]
    
    for i in range(1, len(pcakes)):
        if pcakes[i] != currentRun:
            flips += 1
            currentRun = pcakes[i]
            

    if pcakes[len(pcakes) - 1] == '-':
        flips += 1
        
    fout.write("Case #%d: %d\n" % (t+1, flips))

f.close()
fout.close()
