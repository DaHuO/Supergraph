import sys

stream = sys.stdin

def presult(i, res):
    print "Case #"+str(i)+":", res

# 65 is A
# 90 is Z

# 0 is A
# 26 is Z

# number of tests
t = int(stream.readline().strip())

def evacuate(inside):
    res = []
    left = sum([k for i,k in inside])
    while left:
        # sort
        inside = sorted(inside, key=lambda x: x[1])
        if left==1:
            cc = chr(inside[-1][0]+65)
            res.append(cc)
            left -= 1
            inside[-1] = (inside[-1][0],inside[-1][1]-1)
        elif left==2:
            left -= 2
            cc = chr(inside[-1][0]+65)+chr(inside[-2][0]+65)
            res.append(cc)
            inside[-1] = (inside[-1][0],inside[-1][1]-1)
            inside[-2] = (inside[-2][0],inside[-2][1]-1)
        elif left==3:
            cc = chr(inside[-1][0]+65)
            res.append(cc)
            left -= 1
            inside[-1] = (inside[-1][0],inside[-1][1]-1)
        else:
            if inside[-1][1]==inside[-2][1] or inside[-1][1]==(inside[-2][1]+1):
                left -= 2
                cc = chr(inside[-1][0]+65)+chr(inside[-2][0]+65)
                res.append(cc)
                inside[-1] = (inside[-1][0],inside[-1][1]-1)
                inside[-2] = (inside[-2][0],inside[-2][1]-1)
            else:
                left -= 2
                cc = chr(inside[-1][0]+65)+chr(inside[-1][0]+65)
                inside[-1] = (inside[-1][0],inside[-1][1]-2)
                res.append(cc)
    # convert '0' to 'A'
    # 26 to 'Z'
    return " ".join(res)

for pp in range(t):
    n = int(stream.readline().strip())
    inside = stream.readline().split()
    inside = [(i,int(li)) for (i,li) in enumerate(inside)]
    res = evacuate(inside)
    presult(pp+1, res)
