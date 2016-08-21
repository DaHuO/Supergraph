inp = open("in.txt", "r")
out = open("out.txt","w")
T= int((inp.readline()).rstrip())
for i in range(T):
    N=int((inp.readline()).rstrip())
    am=((inp.readline()).rstrip()).split()
    nam=[]
    syn=0
    for a in am:
        nam.append(int(a))
        syn+=int(a)
    sam=[]
    for j in range(len(nam)):
        sam.append([nam[j],j])
    sam.sort(key=lambda x: x[0],reverse=True)
    print(sam)
    out.write("Case #" + str(i+1) + ":")
    j=0
    while sam[0][0]!=0 and syn!=0:
        out.write(" ")
        ans=""
        if sam[j][0]>=2:
            syn-=2
            if j+1<N:
                if sam[j+1][0]>syn//2:
                    if j+2<N:
                        if sam[j+2][0]>syn//2:
                            syn+=1
                            sam[j][0]-=1
                            ans+=(chr(sam[j][1]+65))
                        else:
                            sam[j][0]-=1
                            sam[j+1][0]-=1
                            ans+=(chr(sam[j][1]+65))
                            ans+=(chr(sam[j+1][1]+65))
                    else:
                        sam[j][0]-=1
                        sam[j+1][0]-=1
                        ans+=(chr(sam[j][1]+65))
                        ans+=(chr(sam[j+1][1]+65))
                else:
                    sam[j][0]-=2
                    ans+=(chr(sam[j][1]+65))
                    ans+=(chr(sam[j][1]+65))
            else:
                print('malakia')
        else:
            syn-=1
            if j+1<N:
                if sam[j+1][0]>syn//2:
                    syn-=1
                    sam[j][0]-=1
                    sam[j+1][0]-=1
                    ans+=(chr(sam[j][1]+65))
                    ans+=(chr(sam[j+1][1]+65))
                else:
                    sam[j][0]-=1
                    ans+=(chr(sam[j][1]+65))
            else:
                print('malakia')
        print(sam)
        sam.sort(key=lambda x: x[0],reverse=True)
        out.write(ans)
    out.write("\n")