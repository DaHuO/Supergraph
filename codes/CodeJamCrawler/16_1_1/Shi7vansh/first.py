with open('A-large (1).in') as f:
    lines = f.readlines()
for test in range(int(lines[0])):
    s=lines[test+1]
    s=list(s)
    ans=list()
    ans.append(s[0])
    s.remove(s[0])
    for i in s:
        if i>=ans[0]:
            ans.insert(0,i)
        else:
            ans.append(i)
    ans="".join(ans)
    print('Case #',test+1,': ',ans,sep='')
    
