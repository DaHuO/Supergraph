import sys

test_cases = open(sys.argv[1], 'r')
n = -1
i = 1

for test in test_cases:
    numbers = []
    if n == -1:
        n = int(test)
        continue

    number = test.replace('\n', '').replace('\r', '')
    number = number.split(" ")
    K = int(number[0])
    C = int(number[1])
    S = int(number[2])

    if C == 1:
        if K <= S and S==1:
            print("Case #" + str(i) + ": 1")
        elif K<=S:
            text = ""
            for j in range(1, K+1):
                text += str(j)
                if not j == K+1:
                    text += " "
            print("Case #" + str(i) + ": " + text)
        else:
            print("Case #" + str(i) + ": IMPOSSIBLE")  
    else:
        if K == 1:
            print("Case #" + str(i) + ": 1")
        elif K-1 <= S:
            text = ""
            for j in range(2, K+1):
                text += str(j)
                if not j == K+1:
                    text += " "
            print("Case #" + str(i) + ": " + text)
        else:
            print("Case #" + str(i) + ": IMPOSSIBLE")
    i += 1