import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    num = 0
    if N == 0:
        print("Case #" + str(t) + ": INSOMNIA")
    else:
        seen = [False] * 10
        while False in seen:
            num += N
            for cijfer in str(num):
                seen[int(cijfer)] = True

        print("Case #" + str(t) + ": " + str(num))