from collections import defaultdict as dd

T = int(raw_input().strip())

cars = [
    (0, ["Z"], "ZERO"),
    (2, ["W"], "TWO"),
    (4, ["U"], "FOUR"),
    (5, ["F", "V"], "FIVE"),
    (6, ["S", "X"], "SIX"),
    (7, ["S", "V"], "SEVEN"),
    (8, ["G"], "EIGHT"),
    (9, ["N", "I"], "NINE"),
    (1, ["O"], "ONE"),
    (3, ["T"], "THREE")    
]

for i in xrange(1, T + 1):
    S = raw_input().strip()
    d = dd(int)
    for el in S:
        d[el] += 1
    sol = []

    for val, car, letters in cars:
        can = True
        while can:
            # print "sol: %s" % (sol,)
            # print "d: %s" % (d,)
            for c in car:
                if d[c] == 0:
                    can = False
                    break
            if can:
                for letter in letters:
                    d[letter] -= 1
                sol.append(val)
    print "Case #%s: %s" % (i, "".join(map(str, sorted(sol))))
    

