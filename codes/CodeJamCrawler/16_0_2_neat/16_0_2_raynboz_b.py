fin = open('bin.txt', 'r')
fout = open('bout.txt', 'w')

T = int(fin.readline())

def solve():
    s = fin.readline().split()[0]
    a = s[0]
    curr = a
    count = 1

    for c in s:
        if c != curr:
            count += 1
            curr = c
    ans = count - 1
    if a == "-" and count % 2 == 1:
        ans += 1
    if a == "+" and count % 2 == 0:
        ans += 1
    #print(a, count, ans)
    return ans

for i in range(T):
    fout.write("Case #" + str(i+1) + ": " + str(solve()) + "\n")

fin.close()
fout.close()
