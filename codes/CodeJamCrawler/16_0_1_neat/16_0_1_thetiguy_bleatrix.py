def get_sheep(n):
    unseen = set('0123456789')
    i = 0
    while n and unseen:
        i += 1
        unseen = unseen.difference(set(str(i * n)))
    return  str(i * n) if n else "INSOMNIA"

with open('large.in') as f:
    for i, n in enumerate(f.readlines()[1:], start=1):
        print("Case #{}: {}".format(str(i), get_sheep(int(n.strip()))))
