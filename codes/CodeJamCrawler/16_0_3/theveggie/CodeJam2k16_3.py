import sys
sys.setrecursionlimit(1800000)

file=open('test.txt','r')
#file=open('C-small-attempt0.in','r')
file1=open('output-c-large.txt','w')

def recurse(num,length):
    global count

    if not count:
        return
    if length==0:
        num='1'+num+'1'
        output=[num]
        legit=True
        for i in range(2,11):
            number=int(num,i)
            found=False
            for j in range(2,int(number**0.5)):
                if not number%j:
                    found=True
                    break
            else:
                legit=False
                break
            output.append(str(j))
        if legit:
            print(' '.join(output))
            file1.write(' '.join(output))
            file1.write('\n')
            count-=1
        return
    recurse(num+'0',length-1)
    recurse(num+'1',length-1)

for i in range(int(file.readline())):
    n,count = map(int, file.readline().split())
    print("Case %d:" %(i+1))
    file1.write("Case %d:\n" %(i+1))
    recurse('',n-2)

