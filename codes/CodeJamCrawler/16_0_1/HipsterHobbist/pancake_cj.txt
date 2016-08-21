f = [line.rstrip() for line in open('/Users/prajjwaldangal/Downloads/A-large.in')]
out = open('/Users/prajjwaldangal/Desktop/codejam_out.txt','w')
index = 0
testcases = int(f[index])
index += 1
for i in range(1,testcases+1):
    n = f[index]
    gap = f[index]
    index += 1
    l = set(n)
    j = 2
    while len(l) < 10 and n != "0":
        n = str(j*int(gap))
        j += 1
        l = l.union(set(n))
    if n =="0":
        ans = "INSOMNIA"
    else:
        ans = n
    print (ans)
    out.write("Case #"+str(i)+": "+ str(ans) + "\n")
out.close()