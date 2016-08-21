def reverse(s):
    s = s.replace('-','=')
    s = s.replace('+','-')
    s = s.replace('=','+')
    return s
T = int(input())
for i in range(1,T+1):
    s = input()
    count = 0
    if s == '+'*len(s):
        print("Case #{}: {}".format(i, 0))
    elif s=='-'*len(s):
        print("Case #{}: {}".format(i, 1))
    else :
        while len(s)>0:
            if s[-1]=='+':
                s = s[:-1]
            else :
                s = reverse(s)
                count += 1
        print("Case #{}: {}".format(i, count))
