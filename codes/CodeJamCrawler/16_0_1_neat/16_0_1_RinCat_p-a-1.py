#!/usr/bin/python3 
import sys

def counting_sheep(case, n):
    current_numbers = []
    i = 1
    if n==0:
        print("Case #" + str(case) + ": INSOMNIA")
    else:
        while True:
            for c in str(i*n):
                if c not in current_numbers:
                    current_numbers.append(c)
                if len(current_numbers) == 10:
                    print("Case #" + str(case) + ": " + str(i*n))
                    return
            i = i +1

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding="UTF-8") as f:
        f.readline()
        line = 1
        for d in f:
            counting_sheep(line, int(d))
            line = line + 1
        




