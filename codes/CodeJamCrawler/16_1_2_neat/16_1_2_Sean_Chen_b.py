def solve(n):
    num = 2*n - 1
    items = []
    ans = []
    digs=set()

    for i in xrange(num):
        tmp = map(int,raw_input().split())

        for mem in tmp:
            items.append(mem)
            digs.add(mem)

    for i in digs:
        if items.count(i) % 2 == 1:
            ans.append(i)
    ans.sort()
    return ans

T=int(raw_input())
for cas in xrange(1,T+1):
    N=int(raw_input())
    ans = solve(N)

    print "Case #{}: {}".format(cas," ".join(map(str,ans)))

#("1{0:0>"+str(sub-2)+"b}1").format(i)
#("1{0:07b}1").format(10)

#print "Case #1:"
#for i in res:
#    print i," ".join(divs)





