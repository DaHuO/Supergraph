import sys
import os


def ComputeLastNamedNo(N):

    charSet = set([c for c in str(N)])
    lastNamedNo = N
    
    while len(charSet) < 10:
        lastNamedNo += N
        charSet.update([c for c in str(lastNamedNo)])

    return lastNamedNo

def main():

    T = int(raw_input())

    for testNo in range(1,T+1):
        N = int(raw_input())

        if N == 0:
            print "Case #%d: INSOMNIA"%(testNo)
        else:
            print "Case #%d: %d"%(testNo,ComputeLastNamedNo(N))

if __name__ == "__main__":
    main()
