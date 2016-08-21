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
def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))



def main():
    fo = open("B-large.in","r")
    fp = open("output2.txt", "w")
    test = int(fo.readline())
    tri = 1
    while test > 0:
        test -= 1
        n = int(fo.readline())
        ls = []
        for i in range(2*n-1):
            ls.append(map(int, fo.readline().split()))
        ds = []
        for i in ls:
            for k in i:
                ds.append(k)
        counts = dict()
        for i in ds:
            counts[i] = counts.get(i, 0) + 1
        print counts

        fs = []
        for key, value in counts.iteritems():
            if value % 2 == 1:
                fs.append(key)
        fs.sort()
        fp.write("Case #"+str(tri)+": ",)

        for i in (fs):
            fp.write(str(i)+" ",)

        tri+=1
        fp.write("\n")

if __name__ == '__main__':
    main()
