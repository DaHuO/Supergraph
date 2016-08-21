#!/usr/bin/python
# -*- coding: utf-8 -*-

def CountingSheep():

    file = open("A-large.in")
    T = int(file.readline())

    out = open("A-large.out", "w")
    for n in range(T):
        N = file.readline()
        seen = set()
        i = 1

        while len(seen) != 10:
            y = int(N) * i
            if y == 0:
                print "Case #{}: {}".format(int(n+1), "INSOMNIA")
                out.write("Case #{}: {}\n".format(int(n+1), "INSOMNIA"))
                break
            y = str(y)
            for ch in y:
                if ch not in seen:
                    seen.add(ch)
            if len(seen) == 10:
                print "Case #{}: {}".format(int(n+1), y)
                out.write("Case #{}: {}\n".format(int(n+1), y))
                break
            i += 1
    file.close()
    out.close()

if __name__ == '__main__':
    CountingSheep()
