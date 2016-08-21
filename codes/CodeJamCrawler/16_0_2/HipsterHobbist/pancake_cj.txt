f = [line.rstrip() for line in open('/Users/prajjwaldangal/Downloads/B-small-attempt0.in')]
out = open('/Users/prajjwaldangal/Desktop/codejam_out.txt','w')
index = 0
testcases = int(f[index])
index += 1
for i in range(1,testcases+1):
    pancakes = f[index]
    index += 1
    final = pancakes[0]
    for j in range(1,len(pancakes)):
        if pancakes[j]!= pancakes[j-1]:
            final += pancakes[j]
    if final[-1]=='-':
        ans = len(final)
    else:
        ans = len(final)-1
    print  (ans)
    out.write("Case #"+str(i)+": "+ str(ans) + "\n")
out.close()