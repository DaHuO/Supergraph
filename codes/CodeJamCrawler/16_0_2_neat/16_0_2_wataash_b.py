def flip(S, i):
    L_flip = S[:i][::-1]
    L_flip = L_flip.replace('+', '_').replace('-', '+').replace('_', '-')
    return L_flip + S[i:]


with open('in.txt') as f:
    inp = f.readlines()

T = int(inp.pop(0))

for case in range(1, T + 1):
    S = inp.pop(0).replace('\n', '')
    ans = 0
    while True:
        if '-' not in S:
            break
        if S[0] == '+':
            i = S.index('-')  # First '-'
            S = flip(S, i)  # Frip consecutive '+'
            ans += 1
        else:
            i = S.rfind('-')  # Find the last '-'
            S = flip(S, i+1)  # Flip top - last '-'
            ans += 1

    print('Case #' + str(case) + ': ' + str(ans))
