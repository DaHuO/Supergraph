def inv(c):
    return '-' if c == '+' else '+'

nb_tests = int(input())

for t in range(1, nb_tests + 1):
    pancakes = list(input())
    size = len(pancakes)
    j = 0
    turn_count = 0

    while '-' in pancakes:
        turn = False
        i = 0

        while j < size and pancakes[i] == pancakes[j]:
            j += 1

        while i < j:
            pancakes[i] = inv(pancakes[i])
            i += 1
            turn = True

        if turn:
            turn_count += 1

    print("Case #%d: %d" % (t, turn_count))
