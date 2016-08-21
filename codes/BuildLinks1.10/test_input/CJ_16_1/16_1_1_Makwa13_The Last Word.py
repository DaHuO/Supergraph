#-------------------------------------------------------------------------------
# Name:        The Last Word
# Purpose:
#
# Author:      ma
#
# Created:     16/04/2016
# Copyright:   (c) ma 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
import string
def resolve(line):

    chlist=[]
    for index,ch in enumerate(line):
        if index == 0:
            chlist.append(ch)
        else:
            if  ch >= chlist[0]:
                chlist.insert(0, ch)
            else:
                chlist.append(ch)
    return "".join(chlist)

def main4():
    print(resolve("CAB"))
    print(resolve("JAM"))
    print(resolve("CODE"))
    print(resolve("ABAAB"))
    print(resolve("CABCBBABC"))
    print(resolve("ABCABCABC"))
    print(resolve("ZXCASDQWE"))
def main():
    with open("A-large (1).in", "r") as infile:
        with open("outputTheLastWord.txt", "w") as outfile:
            T= int(infile.readline() )
            for i in range(T):
                line = infile.readline().strip()
                ret = resolve(line)
                #print("Case #{0}: {1}".format(i+1, ret))
                outfile.write("Case #{0}: {1}\n".format(i+1, ret))
if __name__ == '__main__':
    main()
