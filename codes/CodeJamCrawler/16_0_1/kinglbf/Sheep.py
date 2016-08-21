f = open('C:\Users\Barry\Desktop\codejam\Sheep\A-large.in', 'r+')
data = []

for line in f:
    data.append(int(line.strip()))
    

for i in range (data[0]):
    satisfied = 0
    check = [1,1,1,1,1,1,1,1,1,1]
    increment = data[i + 1];
    number = 0;
    if (increment == 0):
        print "Case #" + str(i + 1) + ": INSOMNIA"
        continue
    while satisfied < 10:
        number += increment
        string = set(str(number))
        for j in range(len(check)):
            if (check[j] == 1 and str(j) in string):
                check[j] = 0
                satisfied += 1
    print "Case #" + str(i + 1) + ": " + str(number)
