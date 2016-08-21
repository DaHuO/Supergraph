T = int(input())
for t in range(T):
    S = input()
    count = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            count += 1
    if count % 2 == 0:
        if S[0] == '-':
            count += 1
    else:
        if S[0] == '+':
            count += 1
    print('Case #{}: {}'.format(t+1, count))
