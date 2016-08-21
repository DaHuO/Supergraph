import sys


def checkFull(alist):
	for i in range(10):
		if not str(i) in alist:
			return False
	return True
    
def main():
    result={}
    with open(raw_input("Enter the file name:"),'r') as fp:
        m=fp.read().split('\n')
    for i in range(1,int(m[0])+1):
        n = m[i]
        z=n
        count=1
        temp=list(n)
        if set(n)==set('0'):
            result[i]='INSOMNIA'
        else:
            while True:
                count+=1
                if checkFull(temp):
                    result[i]=z
                    break
                t=eval(n)
                z=str(t*count)
                temp.extend(list(z))
    with open('U:/Muralidhar Ramarao/Work Allocation/Document/GoogleCodeJam/A-large-attempt1.out','a') as fp:
        for i in sorted(result.keys()):
            fp.write('Case #%d: %s'%(i,result[i]))
            fp.write('\n')

if __name__=='__main__':
    main()
#['0', '1', '2', '11', '1692']
