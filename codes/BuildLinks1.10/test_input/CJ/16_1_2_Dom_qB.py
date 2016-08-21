import ju

results = []
FILE = "B-large"
f = ju.jopen(FILE)

T = int(f.readline())
for t in range(T):
    N = int(f.readline())
    lists = []
    sortIndex = 0
    counts = {}
    for l in range(2*N-1):
        split = map(int,f.readline().split())
        for num in split:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
    print counts
    odds = []
    for num in counts.keys():
        if counts[num] % 2 == 1:
            odds += [num]
    odds.sort()
    print odds
    resultString = ""
    for odd in odds:
        resultString += str(odd) + " "
    results += [resultString]



ju.jout(FILE, results)
