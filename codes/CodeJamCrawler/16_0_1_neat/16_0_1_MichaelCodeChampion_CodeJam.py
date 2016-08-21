#Sheep counting

file = open('Input_SheepSmall.txt', 'r')

for i in next(file).split():
    length = int(i)
x = []
for line in file:
    for i in line.split():
        x.append(int(i))

zeros = []
y = []
for i in range(length):
    quersum = 0
    dig = [0]*10
    counter = 1
    current = x[i]
    while quersum < 10:
        if current == 0:
            y.append(-1)
            zeros.append(i)
            break
        else:
            strcur = str(current)
            for ch in strcur:
                dig[int(ch)] = 1
        quersum = sum(dig)
        if quersum == 10:
            y.append(current)
        counter = counter + 1
        current = counter*x[i]



#write output
out = open('Output_SheepSmall.txt', 'w')
for j in range(length):
    i = j+1
    if y[j] > -1:
        out.write("Case #%s: %s\n" % (i, y[j]))
    else:
        out.write("Case #%s: INSOMNIA\n" % i)


out.close()
