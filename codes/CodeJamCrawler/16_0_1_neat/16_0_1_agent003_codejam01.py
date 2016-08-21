n=0
fobj = open(r"C:\Users\Ekansh\Downloads\A-large.in")
fout = open(r"C:\Users\Ekansh\Downloads\output2.txt","w")
for line in fobj:
    n = line.rstrip()
    break
x = 1
for i in fobj:
    a = i.rstrip()
    if(int(a) == 0):
        fout.write(str("Case #"+str(x)+":"+" INSOMNIA\n"))
        x += 1
        continue
    l = list(set(a))
    j=2
    while len(l)!=10:
        c = str(int(a)*j)
        j += 1
        b = list(set(c))
        l = list(set(l) | set(b))
    fout.write(str("Case #"+str(x)+":"+" "+c+"\n"))
    x += 1
fobj.close()
fout.close()
