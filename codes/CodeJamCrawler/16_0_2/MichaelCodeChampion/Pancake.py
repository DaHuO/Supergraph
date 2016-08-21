# Pancake

file = open('Input_PancakeLarge.txt', 'r')

for i in next(file).split():
    length = int(i)

y = []
for line in file:
    x = []
    for i in line:
        if str(i) == '+':
            x.append(1)
        elif i == '-':
            x.append(0)
    #compute optimal lifting maneuver
    lx = len(x)
    current = x[0]
    count = 0
    for i in range(lx):
        if x[i] != current:
            count  = count+1
            current = x[i]
    if x[lx-1] == 0:
        count = count +1
    y.append(count)

#write output
out = open('Output_PancakeLarge.txt', 'w')
for i in range(len(y)):
    j = i+1
    out.write("Case #%s: %s\n" % (j, y[i]))

out.close()