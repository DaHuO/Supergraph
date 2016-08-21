out = []


def get_answer(i):
    if i == 0:
        return 'INSOMNIA'
    k = 1
    n = i
    track = set()
    while len(track) != 10:
        i = k * n
        while i > 0:
            j = i % 10
            track.add(j)
            i = i / 10
        k += 1
    return (k - 1) * n

with open('input.in') as f:
    c = int(f.readline().strip())

    for n in range(c):
        i = int(f.readline().strip())
        ans = get_answer(i)
        out.append('Case #{n}: {ans}'.format(n=n+1, ans=ans))

with open('output', 'w') as f:
    f.write('\n'.join(out))


