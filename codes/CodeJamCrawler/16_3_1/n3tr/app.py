#!/usr/bin/python
import numpy as np

def read_file():
    f = open('A-large.in', 'r')
    return f.read().splitlines()

def calculate(n_party, members_in_party):
    order = []
    members = [int(n) for n in members_in_party.split(' ')]
    total_member = sum(members)

    while True:
        max_party = max(members)
        if max_party == 0:
            break

        index = members.index(max_party)
        order.append(index)
        members[index] -= 1


    a = ord('A')
    result = ''
    temp = ''
    if total_member % 2 != 0:
        tail = order[-3:]
        order = order[:len(order)-3]
        temp += chr(a + tail[0]) + ' ' + chr(a + tail[1]) + chr(a + tail[2])



    i = 0
    for n in order:
        result += chr(a + int(n))
        if i % 2 == 1 :
            result += ' '
        i += 1


    return (result + temp).strip().replace('0','A').replace('1','B').replace('2','C').replace('3','D')




lines = read_file()
t = int(lines[0])  # read a line with a single integer
for i in xrange(0, t):

    number_of_party =  int(lines[(i*2) + 1])
    parties = lines[(i*2) + 2]
    result = calculate(number_of_party, parties)
    print "Case #{}: {}".format(i+1, result)
