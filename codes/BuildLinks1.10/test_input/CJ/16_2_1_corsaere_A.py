INPUT_FILE = "A-small-attempt0.in"
OUTPUT_FILE = "A-small.out"
def solve(d, numbers, prepotential):
    if all(d[key] == 0 for key in d):
        return prepotential
    for letternumber in numbers.keys():
        potential = [x for x in prepotential]
        dcopy = d.copy()
        bad = False
        for letter in letternumber:
            if letter in dcopy and dcopy[letter] > 0:
                dcopy[letter] -= 1
            else:
                bad = True
                break
        if not bad:
            potential.append(numbers[letternumber])
            val = solve(dcopy, numbers, potential)
            if val:
                return val


with open(INPUT_FILE) as f:
    with open(OUTPUT_FILE, "w") as of:
        cases = int(f.readline())
        i = 1
        for x in f.readlines():
            x = x.strip()
            d = {}
            for letter in x:
                if letter in d:
                    d[letter] = d[letter] + 1
                else:
                    d[letter] = 1
            numbers = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}
            nrs = [str(x) for x in sorted(solve(d, numbers, list()))]
            of.write("CASE #{0}: {1}".format(i, ''.join(nrs)))
            of.write("\n")
            i = i + 1
