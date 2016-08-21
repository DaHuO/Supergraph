import time
import fileinput

start = time.clock()
n = 0
cases = []
ans = []
for line in fileinput.input():
    if fileinput.isfirstline():
        n = int(line)
    else:
        cases.append(line.strip())


for s in cases:
    count = 1
    for i in range(len(s)-1):
        if s[i+1] != s[i]:
            count += 1
    if s[-1] == '+':
        count -= 1
    ans.append(count)

f = open('output', 'w')
for i, a in enumerate(ans):
    f.write("Case #%i: %s" % ((i+1), str(a)))
    f.write('\n')
f.close


# print time usage
end = time.clock()
print("Time used {} seconds").format(end - start)
