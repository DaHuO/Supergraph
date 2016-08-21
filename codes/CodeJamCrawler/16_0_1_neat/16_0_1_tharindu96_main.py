FILE_NAME = "A-large";

def getDigits(num):
    digits = set()
    while num:
        digits.add(num % 10)
        num //= 10
    return digits

def checkIfFound(s):
    for i in xrange(10):
        if not i in s:
            return False
    return True

def getResult(num):
    digits = set()
    nums = set()
    i = 0
    while True:
        n = (i + 1) * num
        d = getDigits(n)
        digits = digits.union(d)
        if checkIfFound(digits):
            return str(n)
        if(n in nums):
            return "INSOMNIA"
        nums.add(n)
        i += 1


def main():
    with open("./"+FILE_NAME+".in", "r") as f:
        with open("./"+FILE_NAME+".out", "w") as r:
            first = True
            j = 0
            for line in f:
                if first == True:
                    first = False
                    continue
                j += 1
                n = int(line)
                res = getResult(n)
                r.write("Case #"+ str(j) + ": " + res + "\n")


if __name__ == '__main__':
    main()
