T = input()
for x in range(0,T):
    k = raw_input()
    k = int(k[0])+1
    res = "1"
    for i in range(2,k):
        res = res + " " + str(i)
    print "Case #{}: {}".format(x+1,res)