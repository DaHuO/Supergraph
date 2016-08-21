count = 0

def flip(base, position):
    global count
    count += 1
    return ''.join(['+' if x == '-' else '-' for x in base[:position][::-1]]) + base[position:]

tests = int(raw_input())
for index in range(1, tests + 1):
    base = raw_input()
    j = len(base) - 1
    count = 0
    while base:
        while j >= 0 and base[j] == '+':
            j -= 1
        base = base[:j + 1]
        if not base:
            break
        i = 0
        if base[i] == '-':
            base = flip(base, j + 1)
        else:
            while i < j and base[i] == '+':
                i += 1
            base = flip(base, i)
            base = flip(base, j + 1)
    print("Case #%i: %i" % (index, count))
