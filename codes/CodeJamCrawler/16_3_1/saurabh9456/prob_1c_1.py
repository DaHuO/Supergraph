#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Saurabh
#
# Created:     08/05/2016
# Copyright:   (c) Saurabh 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import heapq
def main():
    fo = open("A-large.in","r")
    fp = open("output3.txt", "w")
    test = int(fo.readline())
    tri = 1
    while test > 0:
        sst = ""
        test -= 1
        n = int(fo.readline())
        ls = map(int, fo.readline().split())
        ls2 = []
        char = ['A','B', 'C', 'D','E','F','G','H','I','J', 'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for i in range(n):
            ls2.append([ls[i], char[i]])
        ls2.sort(reverse = True)

        var1 = [1,0]
        strs = ""
        while(ls2[0][0] > 0):
            if(len(ls2) > 2):
                if ls2[0][0] == 1 and ls2[1][0] == 1 and ls2[2][0] == 1:
                    ls2[2][0] = ls2[2][0] - 1
                    strs = ls2[2][1]
                    ls2.sort(reverse = True)
                elif ls2[0][0] == ls2[1][0]:
                    ls2[1][0] = ls2[1][0] - 1
                    ls2[0][0] = ls2[0][0] - 1
                    strs = ls2[0][1] + ls2[1][1]
                    ls2.sort(reverse = True)
                elif ls2[0][0] > ls2[1][0]:
                    ls2[0][0] = ls2[0][0] - 1
                    strs = ls2[0][1]
                    ls2.sort(reverse = True)
            else:
                 if ls2[0][0] > ls2[1][0]:
                    ls2[0][0] = ls2[0][0] - 1
                    strs = ls2[0][1]
                    ls2.sort(reverse = True)

                 else:
                    ls2[1][0] = ls2[1][0] - 1
                    ls2[0][0] = ls2[0][0] - 1
                    strs = ls2[0][1] + ls2[1][1]
                    ls2.sort(reverse = True)






            sst +=  strs+" "

        fp.write("Case #"+str(tri)+": "+sst)
        tri+=1
        fp.write("\n")

if __name__ == '__main__':
    main()
