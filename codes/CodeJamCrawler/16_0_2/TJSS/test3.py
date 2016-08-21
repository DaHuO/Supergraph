__author__ = 'tegjyot'
import fileinput

def getFlips(str1):

    pancakes = str1[0]
    c = 0
    for t in str1[1::]:
        if pancakes != t:
            c +=1
            pancakes = t

    if str1[-1] =='-':
        c +=1
    return c



if __name__ == "__main__":
    f = fileinput.input()
    T=int(f.readline())
    for line in range(1,T+1):
         N = [x for x in f.readline().split()][0]
         print("Case #{0}: {1}".format(line, getFlips(N)))


