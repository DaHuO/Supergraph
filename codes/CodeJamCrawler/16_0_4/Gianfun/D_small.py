filename = "C-large"
f = open(filename + ".in", "r")
output = open(filename + ".out", "w")

T = int(f.readline().strip())

for idx in range(T):
    caseNum = idx + 1

    K, C, S = [int(v) for v in f.readline().strip().split(" ")]
    print("K: ", K, "C: ", C, "S: ", S)

    #For the small task, since S = K, it is always possible to find
    #which, if any, tiles are gold.
    #If the first tile is Gold, voila!
    #If it isn't, the first K tiles are exactly the
    #original tileset. Therefore, if we check
    #all the K tiles, we will know, for certain, if one is gold.

    output.write("Case #%d: "%caseNum)
    s = ""
    for i in range(K):
        s += "%d "%i
    output.write(s + "\n")
    
f.close()
output.close()
        
    
