def solve(s):
    s = s.strip().rstrip('+')
    n = 0
    for j in range(1,len(s)):
        if s[j] != s[j-1]:
            n += 1
    if n == 0:
        return 1 if len(s) > 0 and s[0] == '-' else 0
    else:
        return n + 1

with open('input.txt') as f:
    data = f.readlines()

res = ""
N = int(data[0])
offset = 1
for i in range(N):
    x = data[i*offset+1].strip()
    res += "Case #{}: {}\n".format(i+1, solve(x))

with open('output.txt','w') as f:
    f.write(res)


