t = int(input())

def solve(length, number):
    #You can do dumb stuff cuz N is always even
    binaryList = []
    n = 0
    while n < number:
        s = "1"
        for i in range(length // 2 - 1):
            if (n // 2**i) % 2 == 1:
                s += "11"
            else:
                s += "00"
        s += "1"
        binaryList.append(s)
        n += 1
    return binaryList

for i in range(1, t + 1):
    N, J = [int(s) for s in input().split(" ")]
    solution = solve(N, J)
    print("Case #1:", end = "")
    for i in range(J):
        print()
        print(solution[i], end = "")
        for b in range(1, 10):
            print(" " + str(b + 2), end = "")
