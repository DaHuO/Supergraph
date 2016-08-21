f = [line.rstrip() for line in open('/Users/roshil/Desktop/B-small-attempt0 (3).in')]
out = open('/Users/roshil/Desktop/out.txt','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for i in range(1,testcases+1):
    pan = f[line]
    line += 1
    temp = pan[0]
    for j in range(1,len(pan)):
        if pan[j]!= pan[j-1]:
            temp += pan[j]
    if temp[-1]=='-':
        ans = len(temp)
    else:
        ans = len(temp)-1
    print  ans
    
    out.write("Case #"+str(i)+": "+ str(ans) + "\n")
out.close()