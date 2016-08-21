from __future__ import print_function
import math
import sys
sys.stdout = open('out2.txt', 'w')


def prime(n):
    isp = 1
    factor = 1
    for i in range(2, int(math.sqrt(n) + 2)):
        if n % i == 0:
            isp = 0
            factor = i
            break
    return (isp, factor)


def change(s, b):
    ans = 0
    i = 0
    for x in reversed(s):
        ans += int(x) * pow(b, i)
        i = i + 1
    return ans


final_ans = []
total = 0
print("Case #1:")
for n in range(32769, 65536):

    if total == 50:
        break

    if n % 2 == 0:
        continue

    bs = '{0:b}'.format(n)
    flag = 1
    ans = [None] * 10
    for x in ans:
        x = None
    ans[0] = bs

    for base in range(2, 11):
        if flag is 0:
            break
        nos = int(change(bs, base))
        pr_tuple = prime(nos)
        if pr_tuple[0]:
            flag = 0
            break
        else:
            ans[base - 1] = pr_tuple[1]

    if flag is 1:
        final_ans.append(ans)
        total = total + 1

for ans in final_ans:
    for item in ans:
        print(item, "", end="")
    print()
