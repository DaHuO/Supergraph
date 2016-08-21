print('Case #1:')
T = int(input())
N, J = map(int, input().split())
for i in range(1, J + 1):
    print('1' + bin(i)[2:].zfill(N // 2 - 1) + bin(i)[2:].zfill(N // 2 - 1) + '1', 3, 4, 5, 6, 7, 8, 9, 10, 11)
