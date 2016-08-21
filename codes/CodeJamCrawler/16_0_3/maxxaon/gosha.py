n, k = map(int, input().split())
ans = 0
print("Case #1:")
def check(s) :
    global ans
   # print(s)
    a = []
    for i in range(2, 11) : 
        cur = 0
        for j in range(len(s)) :
            if (s[j] == '1') :
                cur += i ** j
        if (cur % 3 == 0) :
            a.append(3)
        elif(cur % 5 == 0) :
            a.append(5)
        elif(cur % 7 == 0) : 
            a.append(7)
        else :
            return
    ans += 1
    s = s[::-1]
    print(s, end=' ')
    print(' '.join(map(str, a)))
    
def pereb(s) :
    global ans
    if (ans == k) :
        return
    if (len(s) == n - 2) :
        check('1' + s + '1')
    else :
        pereb(s + '1')
        pereb(s + '0')
pereb("")