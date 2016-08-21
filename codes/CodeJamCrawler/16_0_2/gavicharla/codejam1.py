def flip(s,l):
    str1 = []
    for i in range(l):
        if(s[i] == '-'):
            str1.append('+')
        else:
            str1.append('-')
    return "".join(str1)
test_cases = int(raw_input())
for test in range(test_cases):
    s = raw_input()
    l = len(s)
    count = l
    let =0
    while ('-' in s):
        let+=1
        last_m = s[:count].rfind("-")
        s = flip(s[:last_m+1],last_m+1)+s[last_m+1:]
        count = s.rfind("+")
    print "case #"+str(test+1)+": "+str(let)