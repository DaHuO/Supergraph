



def getLastWord(inp):
    ans = []
    ans.append(inp[0])
    for i in range(1,len(inp)):
        if ord(inp[i]) >= ord(ans[0]):
            ans.insert(0,inp[i])
        else:
            ans.append(inp[i])
    return "".join(ans)

for i in range(1,input()+1):
    ans = getLastWord(raw_input())
    print "Case #{0}: {1}".format(i,ans)