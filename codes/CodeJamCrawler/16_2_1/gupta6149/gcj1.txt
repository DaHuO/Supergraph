t=int(raw_input())
for i in range(0,t):
    arr=[0,0,0,0,0,0,0,0,0,0]
    ans=''
    s=raw_input()
    arr[0]=s.count('Z')
    arr[2]=s.count('W')
    arr[4]=s.count('U')
    arr[6]=s.count('X')
    arr[8]=s.count('G')
    arr[1]=(s.count('O')-arr[0]-arr[2]-arr[4])
    arr[3]=(s.count('H')-arr[8])
    arr[5]=(s.count('F')-arr[4])
    arr[7]=(s.count('V')-arr[5])
    arr[9]=(s.count('I')-arr[5]-arr[6]-arr[8])
    for j in range(0,10):
        ans+=str(j)*arr[j]
    print("Case "+"#"+str(i+1)+": "+ans)
        