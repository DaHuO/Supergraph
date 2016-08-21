def casePrint(n, v):
    print("Case #{}: {}".format(n, v))

def flip(v):
    return '+' if v == '-' else '-'

def f(number):
    s = [i for i in input()]
    actions = 0
    if len(s) == 1:
        if s[0] == '-':
            casePrint(number, 1)
            return
        else:
            casePrint(number, 0)
            return
    while s.count('-') != 0:
        actions += 1
        prefix = 0
        for i in range(len(s)):
            if s[i] != s[0]:
                break
            prefix += 1
        #print("a:{} s:{} p:{}".format(actions, s, prefix))
            
        for i in range(prefix):
            s[i] = flip(s[i])
    casePrint(number, actions)
    
        
    

N = int(input())
for n in range(N):
    f(n+1)
