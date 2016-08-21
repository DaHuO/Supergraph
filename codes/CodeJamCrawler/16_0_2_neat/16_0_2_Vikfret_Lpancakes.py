import sys

raw_input()
case = 1
for pancake in sys.stdin:
    pancake = pancake[:-1]
    ans = 0
    for idx in range(len(pancake)-1):
        if pancake[idx] != pancake[idx+1]:
            ans += 1
    if pancake[len(pancake)-1] == "-":
        ans += 1
    print "Case #"+str(case)+": "+str(ans)
    case += 1
