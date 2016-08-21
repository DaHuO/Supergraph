def sol(k,c,s):
    x = str(1)
    for i in range(2,s+1):
        x += " "+str(i)
    return x



fIn = open('input.txt', 'r')
fOut = open('output.txt', 'w')
case = 0
for line in fIn:
    print(case)
    if case > 0:
        k = int(line.split(' ')[0])
        c = int(line.split(' ')[1])
        s = int(line.split(' ')[2])
        fOut.write("Case #"+str(case)+": "+sol(k,c,s)+"\n")
    case += 1