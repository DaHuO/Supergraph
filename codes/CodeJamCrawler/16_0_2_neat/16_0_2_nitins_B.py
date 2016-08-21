def check(qstr):
    str_len = len(qstr)
    for i in range(str_len):
        if qstr[i] == '-':
            return False
    return True


tests = int(input())
it = 0

def update_pans(pans):
    str_len = len(pans)
    pans = list(pans)

    if pans[0] == '-':
        # start from back until all positives done
        t = str_len - 1
        while t > 0 and pans[t] == '+':
            t -= 1

        for i in range(int((t + 1)/2)):
            x1 = pans[i]
            x2 = pans[t-i]

            x1 = '+' if x1 == '-' else '-'
            x2 = '+' if x2 == '-' else '-'

            pans[t-i] = x1
            pans[i] = x2

        if((t+1)%2 == 1):
            pans[int(t/2)] = '+' if pans[int(t/2)] == '-' else '-'
    else:
        # find the first negative after positives
        t = 0
        while t+1 < str_len and pans[t] == pans[t+1]:
            t += 1

        temp = 0
        while temp < t+1:
            pans[temp] = '-'
            temp += 1

    #print(pans)
    return "".join(pans)

while it < tests:
    it += 1

    pans = input()

    flips = 0
    while not check(pans):
        pans = update_pans(pans)
        flips += 1

    print("Case #{}: {}".format(it, flips))
