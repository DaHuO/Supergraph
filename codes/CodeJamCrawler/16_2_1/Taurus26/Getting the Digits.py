File=open("A-large.txt",'w')

T=int(raw_input())
for t in range(T):
    S=raw_input()
    s=[l for l in S]
    Y=[]
    while True:
        if 'Z' in s:
            Y.append(0)
            for l in "ZERO":
                s.remove(l)
            if len(s)==0:
                break
        if 'W' in s:
            Y.append(2)
            for l in "TWO":
                s.remove(l)
            if len(s)==0:
                break
        if 'U' in s:
            Y.append(4)
            for l in "FOUR":
                s.remove(l)
            if len(s)==0:
                break
        if 'X' in s:
            Y.append(6)
            for l in "SIX":
                s.remove(l)
            if len(s)==0:
                break
        if 'G' in s:
            Y.append(8)
            for l in "EIGHT":
                s.remove(l)
            if len(s)==0:
                    break
        if 'H' in s:
            if not 'G' in s:
                Y.append(3)
                for l in "THREE":
                    s.remove(l)
            if len(s)==0:
                break
        if 'F' in s:
            if not 'U' in s:
                Y.append(5)
                for l in "FIVE":
                    s.remove(l)
            if len(s)==0:
                break
        if 'S' in s:
            if not 'X' in s:
                Y.append(7)
                for l in "SEVEN":
                    s.remove(l)
            if len(s)==0:
                break
        if 'O' in s:
            if not 'Z' in s:
                if not 'W' in s:
                    if not 'U' in s:
                        Y.append(1)
                        for l in "ONE":
                            s.remove(l)
            if len(s)==0:
                break
        if 'N' in s:
            if not 'O' in s:
                if not 'V' in s:
                    Y.append(9)
                    for l in "NINE":
                        s.remove(l)
            if len(s)==0:
                break
    Y.sort()
    y=''.join([str(i) for i in Y])
    print >> File, "Case #%d: %s" %(t+1,y)
File.close()
