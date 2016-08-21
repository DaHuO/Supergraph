# -*- coding: utf-8 -*-

__author__ = 'acky'

if __name__ == "__main__":


    x = []
    imputs = []
    y = []
  
    fin = open('A-large.in', 'r')
    line1 = fin.readline()

    line1 = line1.rstrip('\n')
    T = int(line1)

    cnt = 1
    while cnt <= T:
        line1 = fin.readline()
        x.append(cnt)
        imputs.append(int(line1))
        # imputs.append(line1)
        cnt += 1
    fin.close()

    for n in imputs:
        # checker = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        checker = '0123456789'
        i = 1
        buff = n
        if n == 0:
            y.append('INSOMNIA')
        else:
            while checker != '':
                # for char in checker:
                # judge = n.find(char)
                #     if judge != -1:
                #     checker[0]
                #checker=checker.strip(str(buff))
                checker=checker.translate(None, str(buff))
                #print str(buff)
                # if checker == "":
                #     break
                i += 1
                buff = n * i

            y.append(buff - n)

    print x
    print y

    f = open("A-large.out","w")
    for num in x:
        f.write("Case #"+str(num)+": "+str(y[num-1]) + '\n')
    f.close()
# for line in fin:
# dat = line.rstrip('\n')  #改行コードを取り除く
# dat = dat.split(',')  #カンマでデータを区切る
# x.append(float(dat))
# y.append(np.log(float(dat[1])))
# ev.append(float(dat[1]))
#   intense.append(float(dat[3]))
