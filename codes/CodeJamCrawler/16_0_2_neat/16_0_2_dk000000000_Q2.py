def pancake(pcake):
    pindex = plusindex(pcake)
    cake = pcake[:pindex]
    flip = 0
    findPlus = True
    while cake!="":
        if cake[0]=="+":
            flip+=1
            temp = negate(cake)
            i = plusindex(temp)
            cake = temp[:i]
        elif cake[0]=="-":
            flip+=1
            temp = clip(cake)
            i = plusindex(temp)
            cake = temp[:i]
    return flip
                
            
def negate(pcake):
    clip = ""
    for c in pcake:
        if c == "+":
            clip+="-"
        elif c=="-":
            clip+="+"
    return clip


def clip(pcake):
    clip = ""
    toclip = pcake[::-1]
    for c in toclip:
        if c == "+":
            clip+="-"
        elif c=="-":
            clip+="+"
    return clip
        
def plusindex(pcake):
    for t in range(len(pcake)-1,-1,-1):
        if pcake[t]!="+":
            return t+1
    return 0

if __name__ == "__main__":
    cases = int(raw_input())
    ns = []
    for t in range(cases):
        ns.append(raw_input())
    for t in range(cases):
        flip = pancake(ns[t])
        print "Case #{}: {}".format(t+1,flip)
    
