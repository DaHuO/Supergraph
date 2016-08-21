# first line is the number of inputs
numCases = int(input())  # read a line with a single integer
cases = []
digits = []
results = {}
finished = False
counter = 1
caseNumber = 0

for i in range(0, numCases):
    cases.append(int(input()))  # read a line with a single integer

for case in cases:
    finished = False
    counter = 1
    currNumber = 0
    digits = []
    if case == 0:
        results[caseNumber] = "INSOMNIA"
        caseNumber = caseNumber + 1
        finished = True
    while finished is False:
        product = counter * case
        counter = counter + 1
        currNumber = list(str(product))
        for i in currNumber:
            if i not in digits:
                digits.append(i)
        if len(digits) == 10:
            finished = True
            results[caseNumber] = product
            caseNumber = caseNumber + 1
for i in results:
    print("Case #{}: {}".format(i+1, results[i]))
