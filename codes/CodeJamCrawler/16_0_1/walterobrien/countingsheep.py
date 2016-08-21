__author__ = 'WALTER'

def enuf(setin):
    for i in range(0,10):
        if i not in setin:
            return False
    return True

def splitdigits(choice):
    listing=[]
    for each in list(str(choice)):
        each=int(each)
        listing.append(each)
    return listing

def func(choice):
    globallist=set([])
    for j in range(1,9000,1):
        listing=splitdigits(j*choice)
        for each in listing:
            globallist.add(each)
        if enuf(globallist)==True:
            return j*choice
    return "INSOMNIA"


cases=int(input())

for i in range(0,cases,1):
    choice=int(input())
    print('Case #'+ str(i+1) + ': ' + str(func(choice))+'\n')