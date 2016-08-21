#f='2016-stage1C-A-example'
#f='2016-stage1C-A-small-attempt0'
f='2016-stage1C-A-large'
#f='2016D-small'
#f='2016-stage1C-A-small'

in_file = open(f+'.in','r')
out_file = open(f+'.out','w')
num = int(in_file.readline().rstrip())
print(num)
for i in range(0,num):
    n = int(in_file.readline().rstrip())
    print(n)
    sen=list(map(int,in_file.readline().rstrip().split()))
    print(sen)
    res=[]
    sum=0
    for k in range(0,n):
        sum=sum+sen[k]
    print(sum)
    while sum>0:
        maior=0
        maior_ind=0
        for k in range(0,n):
            if sen[k]>maior:
                maior=sen[k]
                maior_ind=k
        sum=sum-1
        sen[maior_ind]=sen[maior_ind]-1
        st=chr(65+maior_ind)
        print(st)
        if sum!=2:
            maior=0
            maior_ind=0
            for k in range(0,n):
                if sen[k]>maior:
                    maior=sen[k]
                    maior_ind=k
            sum=sum-1
            sen[maior_ind]=sen[maior_ind]-1
            st=st+chr(65+maior_ind)
            print(st)
        res.append(st)    
    d = 'Case #'+str(i+1)+': '+' '.join(res)
    print(d)
    if i+1==num:
        out_file.write(d)
    else:    
        out_file.write(d+'\n')
out_file.close()
in_file.close()


