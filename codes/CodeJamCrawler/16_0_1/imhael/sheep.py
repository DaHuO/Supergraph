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
        cases.append(int(line))

for i in cases:
    seen = {}
    num = i
    if i == 0:
        ans.append("INSOMNIA")
        continue
    while True:
        for k in str(num):
            if k not in seen:
                seen[k] = True
        if len(seen) == 10:
            ans.append(num)
            break
        num += i

f = open('output', 'w')

for i, a in enumerate(ans):
    f.write("Case #%i: %s" % ((i+1), str(a)))
    f.write('\n')
f.close
end = time.clock()
print("Time used {} seconds").format(end - start)
