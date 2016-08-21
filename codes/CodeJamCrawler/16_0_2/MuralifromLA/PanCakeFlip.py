def flip(astr):
    return astr.replace('+','_').replace('-','+').replace('_','-')[::-1]

def checkHappy(astr):
    return len(astr)==astr.count('+')

def happyFace(a):
    count = 0
    if a.count('++') == len(a): return count
    s=a[0]
    while not checkHappy(a):
        temp=''
        for i in a:
            if not i==s:
                break
            temp+=i
        temp=flip(temp)
        a=temp+a[len(temp):]
        count+=1
        if count>10:
            break
        if s=='-':
            s='+'
        else:
            s='-'
    return count
def main(filename):
    result={}
    with open(filename,'r') as fp:
        inputText=fp.read().split('\n')
    T = int(inputText[0])
    for i in range(1,len(inputText)-1):
        result[i]=happyFace(inputText[i].strip())
    for i in sorted(result.keys()):
        print 'Case #%d: %d'%(i,result[i])

if __name__=='__main__':
    import sys
    #main(raw_input('Enter File Name: '))
    main(sys.argv[1])
