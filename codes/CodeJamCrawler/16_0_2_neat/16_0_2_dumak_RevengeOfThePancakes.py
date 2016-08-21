def solve():
    n = int(input())

    # na poczatku obracam raz, w srodku trzy razy , na koncu dwa
    for i in range(n):
        pancakes = raw_input()
        result = 0
        is_start = True
        j = 0
        while j < len(pancakes):
            if pancakes[j] == '-':
                if is_start:
                    result += 1
                else:
                    result += 2
                while j < len(pancakes) and pancakes[j] == '-':
                    j += 1
            j += 1
            is_start = False
        print("Case #%s: %s" % (i + 1, result))


solve()