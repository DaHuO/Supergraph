
import sys

def solve(k):
if not int(k):
return "INSOMNIA"

dig = set()
st = int(k)
k = st

for d in str(k):
dig.add(d)
cnt = 0
while (len(dig)<10 and cnt < 650000):
k = k + st
cnt += 1
for d in str(k):
dig.add(d)
if len(dig) < 10:
return "INSOMNIA"
return k

inp = sys.stdin.readlines()
tn = inp[0]
ti = 1
for k in inp[1:]:
print("Case #{}: {}".format(ti,solve(k) ))
ti += 1
