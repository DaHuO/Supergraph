fin = open('B-large.in', 'r')
fout=open('results-b-large', 'w+')

def count_groups(s):
    return sum(s[i] != s[i+1] for i in range(len(s)-1)) + 1


t = int(fin.readline())


for i in range(t):
    s = fin.readline()[:-1]

    res = count_groups(s) - 1 + (1 if s[-1] == "-" else 0)
    fout.write("Case #" + str(i + 1) + ": " + str(res) +"\n")

fout.close()
