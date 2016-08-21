def countsheep(n):

    if (n==0):
        return -1;

    dd = [0]*10;

    i = 1;

    done = 0;
    while (True):
        temp = n*i;

        s = str(temp);
        for j in range(len(s)):
            if (dd[int(s[j])] == 0):
                dd[int(s[j])] = 1;
                done +=1;
                if (done == 10):
                    return temp;
        i +=1;

if __name__ == '__main__':

    f = open('A-small-attempt0.in', 'r');
    g = open('res.txt', 'w')

    t = int(f.readline());

    for i in range(t):
        prt = "Case #"+str(i+1)+": ";
        n = int(f.readline());
        res = countsheep(n);
        if (res == -1):
            prt += "INSOMNIA";
        else:
            prt += str(res);
        print prt
        g.write(prt)
    
