import ju

results = []
FILE = "A-large"
#FILE = "A-large"
#FILE = "qA"
f = ju.jopen(FILE)

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

T = int(f.readline())
for t in range(T):
    N = int(f.readline())
    senators = map(int, f.readline().split())
    partyCounts = []
    count = 0
    for n in range(N):
        partyCounts += [[senators[n],letters[n]]]
        count += senators[n]
    partyCounts.sort()
    partyCounts.reverse()

    result = ""

    print senators, partyCounts, count

    next = ""
    while count > 2:
        i = 0
        while i+1 < N and partyCounts[i][0] <= partyCounts[i+1][0]:
            i += 1
        if i == 0 and partyCounts[i][0] > partyCounts[i+1][0] + 1:
            result += " " + partyCounts[i][1]*2
            partyCounts[i][0] -= 2
            count -= 2
            continue

        next += partyCounts[i][1]
        partyCounts[i][0] -= 1
        count -= 1
        if count % 2 == 0 or len(next) >= 2:
            result += " " + next
            next = ""

    #print result
    lastTwo = ""
    for party in partyCounts:
        if party[0] > 0:
            lastTwo += party[1]*party[0]
    result = lastTwo if len(result) == 0 else (result[1:] + " " + lastTwo)
    print result
    results += [result]
print results

ju.jout(FILE, results)
