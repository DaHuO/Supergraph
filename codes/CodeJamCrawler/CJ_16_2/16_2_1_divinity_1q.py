t = raw_input()
t = int(t)
s = ""
x = 1
numbers = {0:'ZERO', 1:'SIX', 2:'FOUR', 3:'FIVE', 4:'SEVEN', 5:'TWO', 6:'ONE', 7:'THREE', 8:'EIGHT', 9:'NINE'}
while x <= t:
    st = raw_input()
    n = len(st)
    k = 0
    prevs = st
    ans = []
    anss = ''
    while k <= 9:
        curs = prevs
        sts = numbers[k]
        c = len(sts)
        temp = 0
        flag = 0
        while temp < c:
            flag = curs.find(sts[temp], 0)
            if flag==-1 :
                break
            curs = curs.replace(sts[temp], '0', 1)
            temp = temp + 1
        if flag == -1:
            curs = prevs
            k = k + 1
        else:
            prevs = curs
            if k == 1 :
                ans.append(6)
            elif k == 2 :
                ans.append(4)
            elif k == 3 :
                ans.append(5)
            elif k == 4 :
                ans.append(7)
            elif k == 5 :
                ans.append(2)
            elif k == 6 :
                ans.append(1)
            elif k == 7 :
                ans.append(3)
            else:
                ans.append(k)
            try:
                if int(curs) == 0:
                    break;
            except ValueError:
                continue
        if k > 9:
            k = 0
    ans.sort()
    for key in ans:
        anss = anss + str(key)
    print "Case #" + str(x) + ": " + anss
    x = x + 1
