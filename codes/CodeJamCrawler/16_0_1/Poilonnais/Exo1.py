#!/usr/bin/python3

f = open("test2.in", 'r')
lines = f.readlines()
f.close()

t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
nb = 0
number = 0
for line in lines:
    if i == 0:
        nb = int(line)
    if i > 0:
        number = int(line)
        t2 = t[:]
        j = 1
        printer = True
        count = 0
        while len(t2) != 0:
            found = False
            res = j * number
            liste = [int(k) for k in str(res)]
            for n in liste:
                for num in t2:
                    if n == num:
                        t2.remove(num)
                        found = True
                        break
            if not found:
                count += 1
            if count > 1000:
                print("Case #{0}: INSOMNIA".format(i))
                printer = False
                break
            j += 1
        if printer:
            print("CASE #{0}: {1}".format(i, (j - 1) * number))
    i += 1
