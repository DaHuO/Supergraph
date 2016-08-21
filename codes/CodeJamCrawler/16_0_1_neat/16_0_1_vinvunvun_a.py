f = open('a.txt', 'r')
output = open('ar.txt','w')

f.readline()
result = []

for line in f.readlines():
    n = int(line.strip())

    s = set()
    if n == 0:
        result.append("INSOMNIA")
        continue

    i = 0
    r = n
    while(len(s) != 10):
        i += 1
        r = i*n
        for c in str(r):
            s.add(c)

    result.append(r)

print result
i = 1
for r in result:
    output.write("Case #"+ str(i) + ": " + str(r) + "\n")
    i += 1
