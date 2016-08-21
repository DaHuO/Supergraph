def flippingPancakes(cakes):
    # edge cases:
    if ('-' not in cakes):
        return 0
    if ('+' not in cakes):
        return 1
    # if the bottom is happy, just worry about the rest
    if (cakes[-1] == '+'):
        return flippingPancakes(cakes[:-1])
    # bottom is not happy, so we have to flip the stack, as long as top is currently sad
    if (cakes[0] == '-'):
        return 1 + flippingPancakes(cakes[::-1].replace('+', '0').replace('-', '+').replace('0', '-'))
    # flip as many as are currently sad, will use full flip next time.
    i = 1
    while (cakes[i] == '+'):
        i += 1
    return 1 + flippingPancakes('-'*i + cakes[i:])
    # return 1 + flippingPancakes('-'+cakes[1:])

#
with open("B-large.in", "r") as f:
    nCases = int(f.readline())
    with open("B-large.out", "w") as fout:
        for iCase in range(nCases):
            cakes = f.readline().strip()
            print("Case #%d: %s" % (iCase+1, flippingPancakes(cakes)), file=fout)

# print(flippingPancakes('-')) # 1
# print(flippingPancakes('-+')) # 1
# print(flippingPancakes('+-')) # 2
# print(flippingPancakes('+++')) # 0
# print(flippingPancakes('--+-')) # 3
