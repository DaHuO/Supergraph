
def bleatrix(n):

    track=[]
    if n==0:
        return "INSOMNIA"
    i=1
    while 1:
        f=str(i*n)
        i=i+1
        l=[]   #empty list to append digits for each no. locally
        for j in f:
            l.append(j)

        for j in l:
            if j not in track:
                track.append(j)
            #else:
             #   continue
        if len(track)==10:
            return int(f)
            break
        
                
            



t = int(raw_input())
for i in range(t):
    a = int(raw_input().strip())
    print "Case #{}: {}".format(i+1, bleatrix(a))
