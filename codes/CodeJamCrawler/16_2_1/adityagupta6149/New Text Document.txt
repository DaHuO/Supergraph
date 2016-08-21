ta=int(raw_input())
for i in range(0,ta):
    a=[0,0,0,0,0,0,0,0,0,0]
    ans=''
    s=raw_input()
    a[0]=s.count('Z')
    a[2]=s.count('W')
    a[4]=s.count('U')
    a[6]=s.count('X')
    a[8]=s.count('G')
    a[1]=(s.count('O')-a[0]-a[2]-a[4])
    a[3]=(s.count('H')-a[8])
    a[5]=(s.count('F')-a[4])
    a[7]=(s.count('V')-a[5])
    a[9]=(s.count('I')-a[5]-a[6]-a[8])
    for j in range(0,10):
        ans+=str(j)*a[j]
    print("Case "+"#"+str(i+1)+": "+ans)