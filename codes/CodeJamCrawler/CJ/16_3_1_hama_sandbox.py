fin = open("A-large.in", 'r')
fout = open("large.out", 'w')

t = int(fin.readline())

for cases in range(1, t+1):
    n = int(fin.readline())
    raw_in = fin.readline().split()
    parties = []
    people = 0
    for i in range(n):
        parties.append([str(unichr(i+65)), int(raw_in[i])])
        people += int(raw_in[i])

    fout.write("Case #%d: " % cases)

    parties = sorted(parties, key=lambda party: party[1], reverse=True)
    window = ""
    while people > 0:
        max_party = parties[0]
        window = window + max_party[0]
        max_party[1] -= 1
        people -= 1
        parties = parties[1:]
        if max_party[1] > 0:
            flag = False
            for i in range(len(parties)):
                if parties[i][1] <= max_party[1]:
                    flag = True
                    parties.insert(i, max_party)
                    break
            if not flag:
                parties.append(max_party)
        if people == 0 or people == 2 or len(window) >= 2:
            fout.write("%s " % window)
            window = ""
    fout.write("\n")

fin.close()
fout.close()
