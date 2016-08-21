#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    # code
    for i, x in enumerate(range(int(input())), 1):
        sleep_set = set() # must contain all 0-9 before falling asleep
        n_prev = -1
        start_n = n = int(input())
        while len(sleep_set) < 10:
            if n_prev == n:
                start_n = 0
                break
            for x in str(n):
                sleep_set.add(int(x))
            n_prev = n
            n += start_n
        
        res = n - start_n
        if start_n == 0:
            res = 'INSOMNIA'
        
        print('Case #%d: %s' % (i, res))



if __name__ == "__main__":
    main()
