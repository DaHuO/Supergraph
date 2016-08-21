#f = open("input2.txt","r")
f = open("B-large.in","r")


g = open ("output.log","w")

runs = int(f.readline())

def get_number_of_toggles(stream):
    nr = 0
    last = stream[0]
    for i in range(1,len(stream)):
        #print "Checking %s"%stream[i]
        if stream[i] != last:
            #print "-> flipping"
            nr += 1
            last = stream[i]
    if (stream[0] == '-') and not(nr%2) : #First was - and even flips
        #print "full stack needs to be flipped"
        nr += 1
    if (stream[0] == '+') and (nr%2) : #First was + and odd flips
        #print "full stack needs to be flipped"
        nr += 1
    return nr

for i in range(runs) :
    stream = f.readline().strip()
    #print stream
    result = get_number_of_toggles(stream)

    line = "Case #%d: %d"%(i+1,result)
    print line
    g.write(line+'\n')

f.close()
g.close()