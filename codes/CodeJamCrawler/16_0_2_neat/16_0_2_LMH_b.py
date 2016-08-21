input = open('./bl.in')
output = open('./bl.out', 'w')

T = int(input.readline())
for k in range(1, T + 1):
    S = input.readline()
    S = S[:-1] if S[-1] == '\n' else S
    s = ''
    ans = 0
    for x in S:
        if(len(s) == 0 or x != s[-1]):
            s += x
    if(len(s) == 1):
        ans = 1 if s[0] == '-' else 0
    elif(len(s) % 2 == 0):
        ans = len(s) - 1 if s[0] == '-' else len(s)
    else:
        ans = len(s) if s[0] == '-' else len(s) - 1
    output.write('Case #%d: %s\n' % (k, ans))