def gen_all_pat(n):
    temp = "{{:0<{}}}".format(n)
    for r in range(0,n-1,2):
        c = n/(r+2)
        for j in range(1,c+1):
            for i in range(n-((r+2)*j)+1):
                yield temp.format("0"*i + ("1" + "0"*r + "1")*j)
                
raw_input()
print "Case #1:"
n, j = map(int, raw_input().strip().split())
for p in gen_all_pat(n-2):
    print "1" + str(p) + "1", " ".join(map(str, (b+1 for b in range(2,11))))
    j -= 1
    if not j:
        break
