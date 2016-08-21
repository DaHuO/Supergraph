
def calc(cake):
    if cake == "-":
        return 1
    elif cake == "+":
        return 0
    i = 0
    j = 1
    ans = 0
    diff = False
    allN = True
    while j < len(cake):
        if cake[i] == '+':
            allN = False
        if cake[i] == cake[j]:
            j += 1
            i += 1
        else:
            ans += 1
            diff = True
            i += 1
            j += 1
    if allN:
        return 1
    if diff and cake[j-1] == '-':
        ans += 1
    return ans

for case in range(input()):
    cake = raw_input().strip()
    print "Case #"+str((case+1))+": "+str(calc(cake))