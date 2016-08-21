T = int(input())

for i in range(1, T + 1):
    S = input().rstrip()
    ans = ''
    for char in S:
        ans = max(ans + char, char + ans)
    print('Case #{}:'.format(i), ans)