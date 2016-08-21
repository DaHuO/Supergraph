f = open('C:\Users\Barry\Desktop\codejam\pancakes\B-large.in', 'r+')
data = []

for line in f:
    data.append(line.strip())

for i in range(int(data[0])):
    pancakes = [int(x == '+') for x in list(data[i+1])]
    pancakes.reverse()
    moves = 0
    while 0 in pancakes:
        flip = pancakes.index(0)
        for x in range(len(pancakes[flip:])):
           pancakes[x+flip] = int(pancakes[x+flip] == 0)
        moves +=1
    print "Case #" +str(i+1) + ": " + str(moves)
        