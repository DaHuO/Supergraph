from Solve import *

allDigits = {str(n) for n in range(10)}
    
def countSheep(args):
    nString = args[0]
    startN = int(nString)
    m = 0
    seenDigits = set()
    if startN == 0:
        return "INSOMNIA"

    while True:
        m += 1
        n = m * startN
        digits = {d for d in str(n)}
        seenDigits = seenDigits | digits
        if seenDigits == allDigits:
            return n
        
    return "INSOMNIA"

if __name__ == "__main__":
    solveF("A-large.in", countSheep, 1)
