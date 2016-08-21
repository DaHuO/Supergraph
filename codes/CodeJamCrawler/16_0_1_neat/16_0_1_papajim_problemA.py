#!/usr/bin/python3

def solve(n):
    if n == 0: return "INSOMNIA"

    part = n
    found = False
    checkNums = "0123456789"
    while not found:
        newCheckNums = ""
        for k in checkNums:
            if k not in str(part):
                newCheckNums += k

        if newCheckNums == "":
            found = True
        else:
            part += n
            checkNums = newCheckNums
    return str(part)

if __name__ == "__main__":
    t = int(input())

    for i in range (1, t+1):
        n = int(input())
        res = solve(n)

        print("Case #{}: {}".format(i, res))

