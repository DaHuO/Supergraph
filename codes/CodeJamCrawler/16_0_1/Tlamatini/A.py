f = open('A-large.in', 'r')
g = open('output_A_large.txt', 'w')
num_loops = int(f.readline())

for i in range(0,num_loops):
    seen = []
    N = 0
    thisline = int(f.readline())
    if thisline == 0:
        print "Case #" + str(i+1) + ": INSOMNIA"
        string = str('Case #' + str(i+1) + ": INSOMNIA" + '\n')
        g.write(string)
        continue
    else:
        while len(seen) < 10:
            N = N+1
            thisline2 = int(thisline)*N
            #print thisline2
            strInt = str(thisline2)
            strIntList = list(strInt)
            for j in strIntList:
                if (j not in seen) and (j !="\n"):
                    seen.append(j)
            #print seen
    print "Case #" + str(i+1) + ": " + str(thisline2)
    string = str('Case #' + str(i+1) + ': ' + str(thisline2) + '\n')
    g.write(string)
f.close()
g.close()
