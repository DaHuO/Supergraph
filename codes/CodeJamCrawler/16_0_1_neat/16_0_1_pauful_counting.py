#!/usr/bin/python

# from set import Set

def extractDigits(number, dig):
    for i in str(number):
        dig.add(i)
    return dig

def counting(number):
    if number == 0:
        return 'INSOMNIA'
    dig = set([])
    i = 1
    last = number
    dig = extractDigits(last,dig)
    initial = number
    while(len(dig) < 10):
        i+=1
        last = i * number
        # print '-->> ' + str(last)
        dig = extractDigits(last,dig)
        # print '.... ' + str(dig)
        # print 'len  ' + str(len(dig))
        # if i == 10:
        #     return 'HAIL'

    return str(last)

def readFile(fileName, fileWrite):
    fw = open(fileWrite, "w")
    fo = open(fileName, "rw+")

    lineNum = int(fo.readline())
    for i in range(0,lineNum):
        start = int(fo.readline())
        print str(start)
        fw.write('Case #'+str(i+1)+': '+counting(start)+'\n')
        print counting(start)
        print '----------------'
        # if i == 3:
        #     quit()

    fo.close()
    fw.close()

readFile('A-large.in', 'result.txt')
