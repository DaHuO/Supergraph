import sys
import time
start_time = time.time()
sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

# import random
# for i in range(100):
#     print(random.randint(10**5,10**6))

sys.stdout = open("output.txt", "w")
sys.stdout = sys.__stdout__
for testcases in range(int(input())):

    d = {}
    for j in range(0,10):
        d[str(j)] = 1
    n = int(input())
    cnt = 0
    res = 1
    if n == 0:
        sys.stdout = open("output.txt", "a")
        print("Case #" + str(testcases + 1) + ": "+ "INSOMNIA")
        sys.stdout = sys.__stdout__
        print("Case #" + str(testcases + 1) + ": Done")
        continue
    while cnt < 10:
        num = n*res
        for j in str(num):
            if d[j] == 1:
                d[j] = 0
                cnt += 1
        res += 1
    sys.stdout = open("output.txt", "a")
    print("Case #" + str(testcases + 1) + ": " + str(n*(res-1)))
    sys.stdout = sys.__stdout__
    print("Case #" + str(testcases + 1) + ": Done")

sys.stdout = sys.__stdout__
print(time.time() - start_time)