import sys
import os

def main():

    T = int(raw_input())

    for testno in range(1,T+1):
        K,C,S = [int(s) for s in raw_input().split(" ")]
        if S==K:
            print "Case #%d: %s"%(testno," ".join(map(str,range(1,S+1))))
        else:
            print "S != K !! Exiting !"
            sys.exit(-1)

if __name__ == "__main__":
    main()
