import sys

digits = "0123456789"

def count_til(n):
    if n == 0:
        return "INSOMNIA"
    seen = []
    current = n
    while len(seen) < 10:
        as_str = str(current)
        for digit in digits:
            if digit in seen:
                continue
            if digit in as_str:
                seen.append(digit)
        if len(seen) == 10:
            break
        current += n
    return current

def getData(fileName):
    f = open(fileName, 'r+')
    lines = [line for line in f]
    nCases = int(lines[0])
    k = 1
    while k <= nCases:
        tmp = int(lines[k])
        result = count_til(tmp)
        print "Case #"+str(k)+": "+str(result)
        k = k+1

if __name__ == "__main__":
    fileName = sys.argv[1]
    getData(fileName)
