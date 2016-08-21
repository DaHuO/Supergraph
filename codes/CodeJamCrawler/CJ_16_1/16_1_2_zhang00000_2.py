# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
temp = []
for i in range(1, t + 1):
    n = int(input())
    papers = []
    for k in range(2*n-1):
        papers += [[int(s) for s in input().split(" ")]]
    for k in range(n):
        temp = []
        for j in range(2*n-1):
            temp += [papers[j][k]]
        temp = sorted(temp)
        if k == n-1:
            break
        if temp[2*k]!=temp[2*k+1]:
            break
    unique = temp[2*k]
    for j in range(2*n-1):
        if papers[j][k]==unique:
            minus = papers[j]
            break
    temp1 = temp
    for item in minus:
        for j in range(len(temp1)):
            if temp1[j] == item:
                temp1.pop(j)
                break
    temp1.append(unique)
    temp1 = sorted(temp1)
    out = "Case #{}:".format(i)
    for item in temp1:
        out += " {}".format(item)
    print(out)
    # check out .format's specification for more formatting options
