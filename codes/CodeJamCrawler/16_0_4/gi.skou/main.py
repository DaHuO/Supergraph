from __future__ import print_function

import random
import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        count = int(f.readline())
        cases = [c.strip() for c in f.readlines()]
        for i in range(count):
            K, C, S  = cases[i].split()
            print("Case #{}:".format(i+1), end=' ')
            results = []
            if int(K) == 1:
                print(1)
            elif int(S) < int(K):
                print("IMPOSIBLE")
            elif int(C) == 1:
                for s in range(1, int(K)+1):
                    print("{}".format(s), end=' ')
                print()
            else:
                for s in range(2, int(K)+1):
                    print("{}".format(s), end=' ')
                print()
