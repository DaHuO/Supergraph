
def SaveDigits(dList, s):
    sList = map(int,str(s))
    for i in range(len(sList)):
        dList[sList[i]] = 1
    return dList

def Multi(N):

    dList = list('0000000000')
    bList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    k = 100
    for i in range(1,k):
        S = N * i
        DL = SaveDigits(dList,S)
        if DL == bList:
            return S
            break

    return "INSOMNIA"

ASmallFile = 'A-large.in'

f = open(ASmallFile, 'r')
T = int(f.readline())

p = open('A-large-output.txt','w')

for i in range(T):
    N = int(f.readline())
    A = Multi(N)

    p.write('Case #' + str(i+1) + ': ' + str(A) + '\n' )

f.close()
p.close()




