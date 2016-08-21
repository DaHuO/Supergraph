file=open('A-large.in','r')
file1=open('output-a.txt','w')



for j in range(1,int(file.readline())+1):
    n=int(file.readline())
    if n==0:
        print("Case #"+str(j)+':',"INSOMNIA")
        file1.write("Case #%d: INSOMNIA\n" % (j))

    else:
        found=[False for i in range(10)]
        count=1

        while set(found)!={True}:
            for i in str(n*count):found[int(i)]=True
            count+=1

        print("Case #"+str(j)+':',n*(count-1))

        file1.write("Case #%d: %d\n" % (j,n*(count-1)))
file.close()
file1.close()



'''
n,shy=file.readline().split()
    n=int(n)
    standing=0
    added=0
    for i in range(n+1):
        if standing<i and shy[i]!='0':
            #print(i-standing)
            added+=i-standing
            standing+=added
        standing+=int(shy[i])
    file1.write(str("Case #"+str(j)+': '+str(added)+'\n'))
file1.close()
file.close()
'''