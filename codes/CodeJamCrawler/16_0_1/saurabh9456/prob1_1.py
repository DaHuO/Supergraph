#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Saurabh
#
# Created:     16/04/2016
# Copyright:   (c) Saurabh 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    fo = open("A-large.in","r")
    fp = open("output1.txt", "w")
    test = int(fo.readline())
    tri = 1
    while test > 0:
        test -= 1
        line = fo.readline()
        l = len(line)
        nw = []
        nw.append(line[0])
        for i in range(1,l):
            if(line[i] >= nw[i-1]):
                nw.append(line[i])
            else:
                nw.insert(0,line[i])
        fp.write("Case #"+str(tri)+": ",)

        for i in reversed(nw):
            fp.write(i,)
        tri+=1



if __name__ == '__main__':
    main()
