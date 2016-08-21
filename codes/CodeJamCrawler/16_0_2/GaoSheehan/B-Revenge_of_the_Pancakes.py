def compute(pankcakes):
    parts = 1
    for idx in range(1, len(pankcakes)):
        if pankcakes[idx] != pankcakes[idx-1]:
            parts += 1
    if pankcakes[-1] == '+':
        parts -= 1
    return parts

cases = input()
for idx in range(int(cases)):
    pankcakes = input()
    print("Case #{}: {}".format(idx+1, compute(pankcakes)))
