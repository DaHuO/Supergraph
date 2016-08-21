def sumx(l, p):
    res = 0
    for i in range(len(l)):
        if i != p:
            res += l[i]
    return res

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for t in range(input()):

    n = input()
    sen = [int(x) for x in raw_input().split(" ")]
    res = []

    while sum(sen) > 0:

        part = ""
        mx = max(sen)
        
        i = sen.index(mx)
        sen[i] -= 1
        part += alph[i]
        
        for j in range(len(sen)):
            try:
                perc = sen[j] * 100 / sum(sen)
            except ZeroDivisionError:
                break
            if perc >= 50:
                sen[j] -= 1
                part += alph[j]
                break

        res.append(part)

    if len(res[len(res)-1]) < len(res[len(res)-2]):
        tmp = res[len(res)-1]
        res[len(res)-1] = res[len(res)-2]
        res[len(res)-2] = tmp

    print "Case #{}:".format(t+1),
    for x in res:
        print x,
    print
         
