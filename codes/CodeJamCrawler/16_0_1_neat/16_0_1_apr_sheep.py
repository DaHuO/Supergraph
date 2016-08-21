def solve(onum, num, st, tries):
    st = st | set(str(num))
    if len(st) == 10:
        return str(num)
    else:
        nnum = onum + num
        if nnum == num or tries == 100000000:
            return "INSOMNIA"
        return solve(onum, nnum,st,tries+1)





f = open('input.txt', 'r')
o = open('output.txt', 'w')
lines = f.readlines()
T = int(lines[0])
for i in range(T):
    num = int(lines[i+1].strip())
    ans = "Case #" + str(i+1) + ": " + solve(num,num,set(""),0)
    o.write(ans + "\n")
