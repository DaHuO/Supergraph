for j in range(int(input())):
    s = list(input())
    ans = 0
    tam = len(s)
    print('Case #' + str(j+1)+':', end=' ')
    while(True):
        if all(s[i] == '+' for i in range(tam)):
            break
        if s[0] == '-':
            for k in range(tam):
                if s[k] == '-':
                    s[k] = '+'
                else:
                    break
        else:
            for k in range(tam):
                if s[k] == '+':
                    s[k] = '-'
                else:
                    break
        ans+=1
    print(ans)
