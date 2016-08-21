cases = int(input())

def f(i, ci, k):
    if(ci == 1):
        return [i]
    else:
        i2 = i - (int((i - 1) / k) * k)
        return [i2] + f(int((i - 1) / k) + 1, ci - 1, k)


def validate(varlist, k, c, y):
    for z in range(min(k - y*c, c)):
        if(varlist[z] != (c*y + 1) + z):
            return False

    return True


for z in range(1, cases + 1):
    inp = input().split(" ")
    k = int(inp[0])
    c = int(inp[1])
    s = int(inp[2])

    if(c*s < k):
        print("Case #"+str(z)+": IMPOSSIBLE")
        continue

    y = 0
    maxNum = (k ** c)
    while (k - c * y > 0):
        wanted = [i for i in range(c*y + 1, c*(y+1) + 1)]
        wantedIndex = 1
        wantedCount = 0

        for w in wanted:
            wantedIndex += (w - 1) * (k**wantedCount)
            wantedCount += 1

        ignoreCount = 1
        while (wantedIndex > maxNum):
            # Update wanted list
            # Can't always attain what you dream lel
            for ignore in range(c - ignoreCount, c):
                wanted[ignore] = 1

            ignoreCount += 1
            wantedIndex = 1
            wantedCount = 0
            for w in wanted:
                wantedIndex += (w - 1) * (k**wantedCount)
                wantedCount += 1                        

        if(y != 0):
            print(" ", end="", flush=True)
        else:
            print("Case #"+str(z)+": ", end="", flush=True)
        print(wantedIndex, end="", flush=True)
        y += 1

    print("")

