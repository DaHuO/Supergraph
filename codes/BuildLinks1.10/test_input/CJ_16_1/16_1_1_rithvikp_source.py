myfile=open('input')
ansfile=open('ans','a')
for i in range(int(myfile.readline())):
    s=str(myfile.readline())
    ans=s[0]
    left=s[0]
    for k in s[1:]:
        if k>=left:
            ans=k+ans
            left=k
        else:
            ans=ans+k
    ansfile.write('Case #'+str(i+1)+': '+ans)
myfile.close()
ansfile.close()
