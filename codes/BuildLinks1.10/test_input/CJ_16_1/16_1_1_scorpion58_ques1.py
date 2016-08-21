with open('A-small-attempt0 (1).in') as d:
    lines = d.readlines()
for test in range(int(lines[0])):
    str1=lines[test+1]
    str1=list(str1)
    ans=list()
    ans.append(str1[0])
    str1.remove(str1[0])
    for i in str1:
        if i>=ans[0]:
            ans.insert(0,i)
        else:
            ans.append(i)
    ans="".join(ans)
    print('Case #',test+1,': ',ans,sep='')
    
