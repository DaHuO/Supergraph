l = []
with open('A-large.txt') as f:
    for line in f:
        l.append(line)
f = open('testoutlarge.txt', 'w')
y = int(l[0])
for j in range(y):
    s = list(l[j+1].strip('\n'))
    f.write('Case #' + str(j+1)+': ')
    ans = []
    ans.append(s[0])
    
    for i in range(1, len(s)):
        if s[i] >= ans[0]:
            ans.insert(0, s[i])
        else:
            ans.append(s[i])
    f.write(''.join(ans))
    f.write('\n')
    j += 1
f.close()
