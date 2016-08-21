#!/usr/bin/python

import sys
from math import sqrt
from itertools import count, islice


in_file_name = sys.argv[1]
out_file_name = sys.argv[2]

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def create_string(n):
    n = int(n)
    n -= 2
    
    rtn = "1"
    for i in range(0, n):
        rtn += "0"
    rtn += "1"

    return rtn

def increase_number(n):
    n = str(n)
    n = n[1:]
    n = n[:-1]
    l = len(n)

    n = bin(int(n, 2) + int("1", 2))
    n = n[2:]

    while len(n) != l:
        n = "0" + n

    n = "1" + n + "1"
    return n

def get_numb_base(n):
    rtn = dict()
    for i in range(2, 11):
        rtn[i] = int(n, i)
    return rtn

def find_devidor(n):
    n = int(n)

    i = 2
    while i <= n:
        if n%i == 0:
            return i
        i += 1


row_number = 0
with open(in_file_name, "r") as in_file:
    with open(out_file_name, "w") as out_file:
        for line in in_file:
            if row_number == 0:
                row_number += 1
                continue
               
            n = line.rstrip().split(" ")[0]
            j = line.rstrip().split(" ")[1]

            string = create_string(n)

            out_file.write("Case #" + str(row_number) + ":\n")
            
            found = 0
            while found < int(j):
                base_set = get_numb_base(string)

                found_prime = False
                for base, num in base_set.iteritems():
                    if is_prime(num):
                        found_prime = True
                        break

                if found_prime:
                    string = increase_number(string)
                    continue
                else:
                    out_file.write(string + " ")
                    for base, num in base_set.iteritems():
                        out_file.write(str(find_devidor(num)) + " ")

                    out_file.write("\n")
                    row_number += 1
                    found += 1
                
                if found == int(j):
                    break

                string = increase_number(string)
