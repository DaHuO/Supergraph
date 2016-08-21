fin = open('A-large.in', 'r')
fout=open('results', 'w+')

t = int(fin.readline())

for i in range(t):
    n = int(fin.readline())
    if n == 0:
        fout.write("Case #" + str(i + 1) + ": INSOMNIA\n")
        continue

    appearances = {str(x): 0 for x in range(10)}

    j = 1
    while(True):
        for ch in  str(n * j):
            appearances[ch] += 1

        if sum(v > 0 for _, v in appearances.items()) >= 10:
            fout.write("Case #" + str(i + 1) + ": " + str(n*j) +"\n")
            break

        j += 1


