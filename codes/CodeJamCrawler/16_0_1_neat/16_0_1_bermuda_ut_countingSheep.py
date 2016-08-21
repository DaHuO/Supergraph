MAX_TEST = 300000

tests = int(input(""))
i = 0

def printCounts(case, digit):
    result = "INSOMNIA"
    currMultiple = 1;
    seen = []


    for i in range(0,10):
        seen.append(False)

    for i in range(1, MAX_TEST):
        currDigit = digit * i

        for d in str(currDigit):
            seen[int(d)] = True

        if(sum(seen)) == 10:
            result = currDigit
            break


    print("Case #{}: {}".format(case+1, result))

while i < tests:
    digit = int(input(""))

    printCounts(i, digit)

    i+=1
