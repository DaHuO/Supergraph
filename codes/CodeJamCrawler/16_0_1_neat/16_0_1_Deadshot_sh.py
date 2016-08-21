with open("input.txt","r+") as f:
    case = int(f.readline())
    w = open("output.txt","w")
    for j in range(1,case+1):
        m = int(f.readline())
        i = 1
        flag = [0]*10
        fl = 0
        while(i<500):
            res = i*m
            for r in range(0,10):
                if str(r) in str(res) and flag[r] == 0:
                    #print "hello"
                     flag[r] = 1
            if all(j == 1 for j in flag):
                fl = 1
                break
            i+=1
        if fl == 1:
            s = "Case #%d: %d\n"%(j,res)
            w.write(s)
        else:
            s = "Case #%d: "%(j)+"INSOMNIA\n"
            w.write(s)
        print m,"-----",res
f.close()
w.close()
