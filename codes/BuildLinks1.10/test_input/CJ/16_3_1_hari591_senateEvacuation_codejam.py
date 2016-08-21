def checkIfAllareOnes(f):
    for each in f:
        if each[1] == 1 or each[1] == 0:
            pass
        else:
            return False
    return True

t = input()
j = 0
while t:
    j += 1
    t-=1
    n = input()
    s = raw_input().strip().split()
    i = 0
    total = 0
    d = {}
    while i < len(s):
        d[chr(i + 65)] = int(s[i])
        total += int(s[i])
        i += 1

    output = ""
    while True:
        f = sorted(d.items(), key=lambda x: x[1], reverse=True)

        if f[0][1] == 0:
            break
        if checkIfAllareOnes(f):
            if sum(d.values()) == 2:
                pass
            else:
                output += f[0][0] + " "
                d[f[0][0]] -= 1
                total -= 1
                continue



        if f[0][1] == f[1][1]:
            output += f[0][0] + f[1][0] + " "
            total -= 2
            d[f[0][0]] -= 1
            d[f[1][0]] -= 1
            continue
        if f[0][1] > total - f[0][1]:
            if f[0][1] > 1:
                output += (f[0][0] *2) + " "
                d[f[0][0]] -= 2
                total -= 2
            else:
                output += f[0][0] + " "
                d[f[0][0]] -= 1
                total -= 1
        else:
            if f[1][1] > 0:
                output += f[0][0] + f[1][0] + " "
                d[f[1][0]] -= 1
                d[f[0][0]] -= 1
                total -= 2

            elif f[0][1] == 1:
                output += f[0][0] + " "
                d[f[0][0]] -=  1
                total -= 1
            else:
                output += (f[0][0] *2) + " "
                d[f[0][0]] -=  2
                total -= 2
    print "Case #" + str(j) + ": " + output


