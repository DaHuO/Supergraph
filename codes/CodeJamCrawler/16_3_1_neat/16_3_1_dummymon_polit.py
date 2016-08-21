def outp(a,b):
    file=open("output.txt","a")
    s="Case #"+str(a+1)+": "+str(b)+"\n"
    file.write(s)
    file.close
    print(s)

def checkm(exclude):
    global parties
    total = 0
    left = 0
    for name in parties:
        total += parties[name]
        if name in exclude:
            total -= 1
            if parties[name]-1 > 0:
                left += 1
        elif parties[name] > 0:
            left += 1
    if total == 0:
        return False
    for name in parties:
        if name in exclude:
            if left==2:
                if (parties[name]-1) >= total/2:
                    return False
            if (parties[name]-1) >= total/2:
                return True
        else:
            if parties[name]/ total >= 0.5:
                return True
    return False


q=open ("output.txt","w")
q.close()
inp = open("A-large.in","r")
a= []
for line in inp:
    if "\n" in line:
        a.append(line[0:-1])
    else:
        a.append(line)
inp.close()
inpNum =int(a.pop(0))
for ii in range(inpNum):
    n = int(a.pop(0))
    temp2 = a.pop(0)
    temp = temp2.split()
    parties = {}
    pplno =0
    ans = ''
    for name, party in enumerate(temp):
        parties[chr(name + 65)] = int(party)
        pplno += int(party)
    while pplno > 0:
        maxx = 0
        biggest = []
        for key in parties:
            if parties[key] == maxx:
                biggest.append(key)
            elif parties[key] > maxx:
                biggest = [key]
                maxx = parties[key]
        if len(biggest) > 1:
            if checkm([biggest[0], biggest[1]]):
                ans += biggest[0] +" "
                pplno -=1
                parties[biggest[0]] -= 1
                continue
            ans += biggest[0] + biggest[1] + " "
            pplno -= 2
            parties[biggest[0]] -= 1
            parties[biggest[1]] -= 1
            continue
        nextbig = ""
        maxx = 0
        for key in parties:
            if parties[key] in biggest:
                if parties[key]-1 > maxx:
                    nextbig = key
                    maxx = parties[key]-1
                    continue
            if parties[key] > maxx:
                nextbig = key
                maxx = parties[key]
        if checkm([biggest[0], nextbig]):
            ans += biggest[0] + " "
            pplno -= 1
            parties[biggest[0]] -= 1
            continue
        ans += biggest[0] + nextbig + " "
        pplno -= 2
        parties[biggest[0]] -= 1
        parties[nextbig] -= 1
    outp(ii, ans)






