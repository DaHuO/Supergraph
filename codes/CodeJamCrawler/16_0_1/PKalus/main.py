#!/usr/bin/python

import sys

input_file = open("./" + sys.argv[1], "r")
numbers = input_file.read().split()
test = numbers.pop(0)
got_it = []
lst = []
case = 0
f = open('output.out', 'w')
for number in numbers:
    local_number = int(number)
    case += 1
    counter = 0
    got_it.clear()
    if str(local_number) == '0':
        #print("Case #" + str(case) + ": INSOMNIA")
        f.write("Case #" + str(case) + ": INSOMNIA\n")
        continue
    while True:
        lst.clear()
        lst = list(str(local_number))
        #print(lst)
        for k in range(len(lst)):
            #print(lst[k])
            if got_it.count(lst[k]) == 0:
                got_it.append(lst[k])
        if counter >= 100:
            f.write("Case #" + str(case) + ": INSOMNIA\n")
            break
        if len(got_it) != 10:
            local_number += int(number)
            counter += 1
            continue
        else:
            f.write("Case #" + str(case) + ": " + str(local_number) + "\n")
            break
f.close()


