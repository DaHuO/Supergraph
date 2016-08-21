for y in range(int(input())):

    n = int(input())

    if n == 0:
        print("Case #%d: INSOMNIA" % (y+1))
    else:

        i = 1
        test = {0:None,1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None}
        dic = {}

        while dic != test:

            for j in str(i * n):
                if j not in dic:
                    dic[int(j)] = None

            i += 1

        i -=1

        print("Case #%d: %d" %(y+1, i*n))
