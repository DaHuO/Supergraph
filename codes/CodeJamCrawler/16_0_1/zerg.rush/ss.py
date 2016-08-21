def recurse(s,pos,len,temp):
    if pos is len:
        return temp
    t1 = s[pos] + temp
    t2 = temp + s[pos]
    m1 = recurse(s, pos + 1, len, t1)
    m2 = recurse(s, pos + 1, len, t2)
    if(m1>m2):
        return m1
    else:
        return m2

with open("A-large.in") as infile:
    lines = [item for item in infile.readlines()]
    ntests = int(lines[0])
    stringses = lines[1:]
outfile = open("Output.txt", 'w')
lineno=0
for case in range(ntests):
    lineno=lineno+1
    s=stringses[case]    
    lenstr=len(s)
    fs=s[:-(lenstr-1)]
    if lenstr is 1:
        outfile.write("Case #{}: {}".format(lineno, fs))
        continue
    ans=recurse(s, 1, lenstr, fs)
    outfile.write("Case #{}: {}".format(lineno, ans))  