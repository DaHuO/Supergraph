def solve(s):
    l = len(s)
    result = 0
    i = l-1
    status = '+'
    while (i>=0):
        j = i
        while(j>=0 and s[j]==s[i]):
            j -= 1
        if s[i] != status:
            result += 1
            if status == "-":
                status = "+"
            else:
                status = "-"
        i = j
    return result

t = int(raw_input())
for i in range(1,t+1):
    s = raw_input()
    print "Case #%d:"%i,solve(s)

