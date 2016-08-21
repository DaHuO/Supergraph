def solve(word):
    ret = ""
    for c in word:
        if len(ret) == 0:
            ret += c
            continue
        if(c >= ret[0]):
            ret = c + ret
        else:
            ret += c
        
    return ret
        
fin = open("A-large.in", "r")
fout = open("output.txt", "w")

T = int(fin.readline())
for t in range(T):
    word = fin.readline()[:-1]
    print "Case #{0}: {1}".format(t+1, solve(word))
    fout.write("Case #{0}: {1}\n".format(t+1, solve(word)))

fout.close()
fin.close()