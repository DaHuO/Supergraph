from string import ascii_uppercase

for i in range(int(input())):
    n, result = int(input()), []
    freqs = list(map(int, input().split()))
    s = sum(freqs)

    while any(freqs):
        door = ''
        while len(door) < 2:
            m = max(freqs)
            mi = freqs.index(m)
            door += ascii_uppercase[mi]
            freqs[mi] -= 1
            if not any(freqs):
                break
        result.append(door)
    
    if s % 2 == 1: # UGH IT TOOK ME FOREVER TO REALIZE THIS EDGE CASE
        b, a = result.pop(), result.pop()
        result.append(a[0])
        result.append(str(a[1] + b))

    print("Case #{}: {}".format(i+1, ' '.join(result)))