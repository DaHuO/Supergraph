import numpy as np

def readInput(name):
    f = open("./result", 'w+')
    with open(name, "r") as mf:
        data = mf.readlines()
        

    #print data[1:]
    ind = 1
    for d in data[1:]:
        d = d.replace('\n','')
        
        flips = 0
        state = '+'
        for t in reversed(d):
            if t != state:
                state = t
                flips += 1

        line = "Case #"+str(ind)+": "+str(int(flips))+"\n"
        ind += 1
        #print line
        f.write(line)
