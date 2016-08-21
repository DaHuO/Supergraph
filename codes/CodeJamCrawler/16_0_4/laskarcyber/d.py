T = int(input())
for tc in range(1,T+1):
    K, C, S = map(int, input().split(' '))
    print("Case #{0}: ".format(tc), end="")
    print(1, end=" ")
    for pos in range(2,K+1):
        jumlah = 0
        for i in range(1, C):
            jumlah += K**i * (pos-1)

        jumlah += pos
        print(jumlah, end=" ")
    print("")