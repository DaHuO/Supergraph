import sys

def rev(s, l):
    temp = list(s[:l])
    temp2 = list(s[l:])
    for i in xrange(len(temp)):
        if temp[i] == "+":
            temp[i] = "-"
        else:
            temp[i] = "+"
    temp.reverse()
    return "".join(temp)+"".join(temp2)


caseNum = input()
for i in xrange(caseNum):
    s = raw_input()
    count = 0
    case = i + 1
    if "-" not in s:
        print "Case #{}: 0".format(case)
        continue
    while "-" in s:
        if s[0] == "+":
            front = s.index("-")
            s = rev(s,front)
            count += 1
        end = s.rindex("-")
        s = rev(s,end+1)
        count += 1
    print "Case #{}: {}".format(case,count)
