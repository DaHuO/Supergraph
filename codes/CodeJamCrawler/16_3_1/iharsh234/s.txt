file = open('test.txt','r')
file1 = open('ouput.txt','w')
for x in xrange(int(file.readline())):
    n = int(file.readline())
    arr = map(int,file.readline().split())
    ans = []
    #print arr
    while arr.count(0) != len(arr):
        ab = max(arr)
        if arr.count(ab) == 2:
            cnt = 0
            idx = []
            for i in xrange(len(arr)):
                if arr[i] == ab:
                    arr[i] -= 1
                    cnt += 1
                    idx.append(i)
                if cnt == 2:break
            ans.append(chr(ord('A')+idx[0])+chr(ord('A')+idx[1]))
        else:
            t = arr.index(ab)
            arr[arr.index(ab)] -= 1
            ans.append(chr(ord('A')+t))
        #print arr


    file1.write("Case #%d:"%(x+1)+" "+' '.join(ans)+'\n')
