fin = open("B-large.in", 'r')
fout = open("large.out", 'w')

t = int(fin.readline())

for cases in range(1, t+1):
    pancakes = fin.readline()[:-1]

    # Trim pancakes at the middle which is already positive
    for i in range(len(pancakes)-1, -1, -1):
        if pancakes[i] == '-':
            break
    if pancakes[i] == '+':
        # All pancakes positive!
        pancakes = ""
        fout.write("Case #%d: 0\n" % (cases))
        continue
    pancakes = pancakes[:i+1]

    # Count clusters
    cluster_count = 1
    for i in range(1, len(pancakes)):
        if pancakes[i] != pancakes[i-1]:
            cluster_count += 1

    ans = "Case #%d: %d\n" % (cases, cluster_count)
    fout.write(ans)

fin.close()
fout.close()
