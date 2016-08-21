digits = [str(x) for x in range(10)]
digits = set(digits)
n = int(input())
for it in range(n):
    i = int(input())
    origi = i
    ct = 2
    seen = set()
    ans = ""
    for j in range(5000):
        stri = set(str(i))
        seen = (seen | stri)
        if len(digits - seen)==0:
            ans = i
            break
        else:
            i = origi*ct
            ct+=1
    if not ans: ans = "INSOMNIA"
    print("Case #{}: {}".format(it+1,ans))
