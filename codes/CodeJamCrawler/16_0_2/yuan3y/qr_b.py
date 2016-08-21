def flip_math(s):
    flip = 0
    prev = None
    for c in s:
        if prev:
            if c != prev:
                flip += 1
            prev = c
        else:
            prev = c
    if prev == '-':
        flip += 1
    return flip


t = int(input())
for i in range(t):
    s = input().strip()
    result1 = flip_math(s)
    print("Case #%d: %s" % (i+1, result1))
