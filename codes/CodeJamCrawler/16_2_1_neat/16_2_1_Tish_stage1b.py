import sys



f = open('C:\\Users\\Tish\\Desktop\\A-large (1).in', 'r')
g = open('C:\\Users\\Tish\\Desktop\\output.txt', 'w')
def read():
        return f.readline()
    
def finish(a):
    for i in range(10):
        if (a[i]==0):
            return 0
    return 1


def output(i,out):
    g.write('Case #'+str(i+1)+': '+str(out)+'\n')

def my_print(x):
    g.write(x)



def q1():
    x=read()
    res=[0]*26
    for i in range(len(x)):
        if( ord(x[i])>=ord('A')) and ( ord(x[i])<=ord('Z')):
            res[ord(x[i])-ord('A')]=res[ord(x[i])-ord('A')]+1
    res2='0'*res[ord('Z')-ord('A')]+'1'*(res[ord('O')-ord('A')]-res[ord('Z')-ord('A')]-res[ord('W')-ord('A')]-res[ord('U')-ord('A')])+'2'*res[ord('W')-ord('A')]+'3'*(res[ord('H')-ord('A')]-res[ord('G')-ord('A')])+'4'*res[ord('U')-ord('A')]
    res2=res2+'5'*(res[ord('F')-ord('A')]-res[ord('U')-ord('A')])+'6'*res[ord('X')-ord('A')]+'7'*(res[ord('S')-ord('A')]-res[ord('X')-ord('A')])+'8'*res[ord('G')-ord('A')]+'9'*(res[ord('I')-ord('A')]+res[ord('U')-ord('A')]-res[ord('F')-ord('A')]-res[ord('G')-ord('A')]-res[ord('X')-ord('A')])
    return res2
def main():
    t = int(read())
    for i in range(t):
        output(i,q1())
    g.close()

            
                
main()
