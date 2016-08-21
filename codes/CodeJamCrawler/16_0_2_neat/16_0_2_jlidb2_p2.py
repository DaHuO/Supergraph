f = open('B-large.in', 'r')
out = open('output.txt', 'w')
t = int(f.readline())
for i in range(t):
    s = f.readline().strip()
    count = 0
    if s[len(s)-1] == '-':
        count += 1
    for j in range(len(s)-1):
        if s[j] != s[j+1]:
            count += 1
    out.write("Case #{}: {}\n".format(i+1, count))
