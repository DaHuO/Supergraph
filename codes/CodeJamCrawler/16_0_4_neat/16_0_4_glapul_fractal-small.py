t = int(input())
for tt in range(1, t+1):
    k, c, s = (int(i) for i in input().split())
    print("Case #{}: ".format(tt), end = "")
    for i in range(1, k**c + 1, k**(c-1) ):
        print(i, end=" ")
    print(" ")
