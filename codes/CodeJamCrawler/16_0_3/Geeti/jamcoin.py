import math
import sys

def isNotPrime(num):
    if num <=3:
        return (False,0)
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return (True,i)
    return (False,0)

def toDecAllBase(jc):
    res=[]
    for base in range(2,11):
        s=0
        for i in range(len(jc)):
            s+=int(jc[i])*pow(base,len(jc)-i-1)
        res.append(s)
    return res

def printJamCoin(lenAndNum):
    jcLen = int(lenAndNum.split(' ')[0])
    jcNum = int(lenAndNum.split(' ')[1])
    varLen = jcLen-2
    start= ''.join(['0']*varLen)
    end  = ''.join(['1']*varLen)
    for i in range(int(start,2),int(end,2)):
        if jcNum==0:
            break
        jc = format(i,'0%sb' % len(end)).join(['1','1'])
        allBase = toDecAllBase(jc)
        divisors = [str(isNotPrime(n)[1]) for n in allBase]
        if '0' in divisors:
            continue
        else:
            print('%s %s' % (jc, ' '.join(divisors)))
            jcNum-=1

def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    for i in range(1,len(lines)):
        print('Case #%d:' % i)
        printJamCoin(lines[i])




if __name__ == '__main__':
    main()