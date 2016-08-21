def sol(val):
    count = 0
    l = len(val) - 1
    while count > -1:
        i = 0
        if val[0] == 1:
            while i < l:
                if val[i+1] != 1:
                    break
                i += 1
            if i == l:
                return count
        else:
            i = l
            while i >= 0 and val[i] == 1:
                i -= 1
                l -= 1
        k = 0
        j = i
        while k <= j:
            temp = 1 - val[k]
            val[k] = 1 - val[j]
            val[j] = temp
            j -= 1
            k += 1
        count += 1
    return count

out = open("output_file.txt","w")
file_in = []
case = 1
with open("B-large.in",'r') as inp:
    next(inp)
    for n in inp:
        res = []
        i = 0
        val = list(n.strip('\n'))
        for i in val:
            if i == '-':
                res.append(0)
            else:
                res.append(1)
        count = (sol(res))
        out.write("Case #" + str(case) + ": " + str(count)+"\n")
        case += 1
inp.close()
out.close()
