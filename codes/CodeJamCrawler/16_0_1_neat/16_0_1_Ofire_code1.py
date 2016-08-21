def containsAll(all):
    l=sorted([c for c in all])
    return True if l == ["0","1","2","3","4","5","6","7","8","9"] else False

s = open("A-large.in",'r')
l=[]
number=0
for i,line in enumerate(s):
    if i > 0:
        l.append(line.rstrip('\n'))
    else:
        number=int(line[:-1])
        print(number)


result=[]
for i in range(number):
    n_origin=l[i]
    n=n_origin
    count=0
    all=set([])

    while int(n) > 0 and containsAll(all) == False:
        count+=1
        n=str(int(n_origin)*count)
        for c in n:
            all.add(c)

    if int(n) == 0:
        result.append("Case #"+str(i+1)+": INSOMNIA")
    else:
        result.append("Case #"+str(i+1)+": "+n)

print("\n".join(result))
file1 = open("ba",'w')
file1.write("\n".join(result))
