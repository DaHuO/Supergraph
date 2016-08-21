s = open("B-large.in",'r')
l=[]
number=0
for i,line in enumerate(s):
    if i > 0:
        l.append(line.rstrip('\n'))
    else:
        number=int(line[:-1])

result=[]
for i in range(number):
    pancakes=l[i]
    optimal=0

    while '-' in pancakes:
        top_panecake=pancakes[0]

        count=0
        for j in range(len(pancakes)):
            if pancakes[j] != top_panecake:
                count=j
                break;

        temp=list(['-' if top_panecake == '+' else '+' for p in pancakes[:count]])

        if len(temp)>0:
            pancakes = list(temp+list(pancakes[count:]))
        else:
            pancakes = list(['-' if top_panecake == '+' else '+' for p in pancakes])

        optimal+=1

    result.append("Case #"+str(i+1)+": "+str(optimal))

file1 = open("ba",'w')
file1.write("\n".join(result))