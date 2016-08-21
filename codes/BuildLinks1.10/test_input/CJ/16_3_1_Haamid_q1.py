def findMax(arr):
    mymax = max(arr)
    indices = []
    for i in range(0, len(arr)):
        if arr[i]==mymax:
            indices.append(i)
    if len(indices)>1:
        return [mymax, mymax, indices]

    secMax = -1000;
    ind = -1000;
    for i in range(0, len(arr)):
        if arr[i]>secMax and i!=indices[0]:
            secMax = arr[i]
            ind = i
    return [mymax, secMax, [indices[0], ind]]

def allOnes(arr):
    all1s = True
    for a in arr:
        if a!=1:
            return [False]
    ind = []
    for i in range(0,len(arr)):
        if arr[i]==1:
            ind.append(i)
    return [True, ind]


ifile = open('i.txt' ,'r')
ofile = open('o.txt' ,'w')

t = int(ifile.readline().strip("\n"))

count=0
for i in range(0,t):
    count+=1

    ofile.write("Case #"+str(count)+":")

    n = int(ifile.readline().strip("\n"))
    arr = ifile.readline().split(" ")
    for j in range(0, len(arr)):
        arr[j] = int(arr[j])

    # print;
    # print arr

    toWrite = ""
    while (True):
        toWrite+=" "

        res2 = allOnes(arr)
        res = findMax(arr)

        done = True
        for a in arr:
            if a!=0:
                done = False
                break
        if (done):
            break

        if res2[0]:
            if len(res2[1])%2==1:
                toWrite+=str(unichr(65+res2[1][0]))
                arr[res2[1][0]]-=1
            else:
                toWrite+=str(unichr(65+res2[1][0])) 
                toWrite+=str(unichr(65+res2[1][1]))
                arr[res2[1][0]]-=1
                arr[res2[1][1]]-=1
        else:
            if res[0]==res[1]:
                toWrite+=str(unichr(65+res[2][0]))
                toWrite+=str(unichr(65+res[2][1]))
                arr[res[2][0]]-=1
                arr[res[2][1]]-=1
            elif res[0]%2==1 and res[0]!=1:
                toWrite+=str(unichr(65+res[2][0]))
                toWrite+=str(unichr(65+res[2][0]))
                arr[res[2][0]]-=2
            # elif res[0]%2==1 and res[0]!=1:
            #     print str(unichr(65+res[2][0]))
            #     arr[res[2][0]]-=1
            elif res[0]%2==0 and res[0]!=1:
                toWrite+=str(unichr(65+res[2][0]))
                arr[res[2][0]]-=1
    # print toWrite
    ofile.write(toWrite+"\n")

    # break

ifile.close()
ofile.close()