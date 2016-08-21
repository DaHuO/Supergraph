import sys
def one_solution(pile):
    i=0
    pile=list(pile)
    size=len(pile)-1
    j=0
    while (size>=0 and pile[size]=="+"):
        size-=1
    while( (set(pile)=={'-'} or set(pile)=={'+','-'}) and size>=0 ):
        pile=reverse(pile,size)
        while (size>=0 and pile[size]=="+"):
            size-=1
        i+=1
    return i
        
def reverse(pile,size):
    for i in range(size+1):
        if (pile[i]=='+'):
            pile[i]='-'
        else:
            pile[i]='+'
    return pile
        
def Solution(file_name):
    stream=open(file_name,'r')
    read=((stream.readline()).split('\n'))[0]
    i=1
    while(read!=""):
        read=((stream.readline()).split('\n'))[0]
        if (read!=""):
            print("Case #{}: {}".format(i,one_solution(read)))
            i+=1
        
if __name__=="__main__":
    Solution(sys.argv[1])
