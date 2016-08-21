import sys

def lastNumberAfterEncounteringAllDigits(n):
    DIGITS = set("0123456789")
    encounteredDigits = set(str(n))
    
    if n == 0:
        return None
    
    curVal = n
    while encounteredDigits != DIGITS:
        curVal = curVal + n
        encounteredDigits |= set(str(curVal))
        
    return curVal

def main():
    ln = 0
    T = None
    for line in sys.stdin:
        if ln == 0:
            T = int(line)
            ln += 1
        else:
            N = int(line)
            sol = lastNumberAfterEncounteringAllDigits(N)
            if sol:
                print("Case #{0}: {1}".format(ln, sol))
            else:
                print("Case #{0}: INSOMNIA".format(ln))
            ln += 1

if __name__ == '__main__':
    main()
