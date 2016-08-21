import sys


N = 0
i = 0
d = []
for l in sys.stdin:
    i += 1
    if i == 1:
        N = int(l.strip())
        continue
    if l.strip():
        d.append(int(l.strip()))


def check(checked, digits):
    for d in digits:
        checked[int(d)] = 1


def main(num):
    checked = [0] * 10
    temp = num
    while True:
        check(checked, str(temp))
        if sum(checked) == 10:
            break
        temp += num
        if temp == 0:
            return "INSOMNIA"
    return temp

for i, n in enumerate(d):
    print "Case #{}: {}".format(i+1, main(n))

