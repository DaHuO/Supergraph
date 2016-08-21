t = int(input())


def solve(lists):
    biggestNumber = 0
    for l in lists:
        biggestNumber = max(biggestNumber, max(l))

    heights = []
    for i in range(biggestNumber + 1):
        heights.append(0)

    for l in lists:
        for num in l:
            heights[num] += 1

    missingList = []
    for h in range(len(heights)):
        if heights[h] % 2 != 0:
            missingList.append(h)

    s = ""
    for m in missingList:
        s += " " + str(m)
    return s[1:]

for i in range(1, t + 1):
    n = int(input())
    lists = []
    for j in range(2*n - 1):
        newList = []
        nextLine = str(input())
        numbers = nextLine.split(" ")
        for asdf in numbers:
            newList.append(int(asdf))
        lists.append(newList)
    solution = solve(lists)
    print("Case #{}: {}".format(i, solution))
