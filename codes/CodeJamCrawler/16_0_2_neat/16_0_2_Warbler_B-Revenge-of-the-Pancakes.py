
def reverse(packs, flag):
    positive=""
    negative=""
    if flag==True:
        positive="+"
        negative="-"
    else:
        positive="-"
        negative="+"

    cnt=0
    lenth=len(packs)
    if lenth<=0:
        return "",0

    i=lenth-1
    while i>=0:
        if packs[i]==positive:
            i=i-1
        else:
            break
    if i<0:
        return "", 0

    j=0
    if packs[0]==positive:
        while j<lenth:
            if packs[j]==positive:
                j=j+1
            else:
                break
        cnt=cnt+1

    while j<lenth:
        if packs[j]==negative:
            j=j+1
        else:
            break

    cnt=cnt+1
    if j>i:
        return "",cnt

    segmt=packs[j:i+1][::-1]
    return segmt,cnt


def solve(packs):
    total=0

    segmt=packs
    flag=True
    while len(segmt)>0:
        segmt,cnt=reverse(segmt,flag)
        total=total+cnt

        if flag==True:
            flag=False
        else:
            flag=True

    return total


testcases = input()
for caseNr in xrange(1, testcases+1):
    packs = raw_input()
    print("Case #%s: %s" % (caseNr, solve(packs)))