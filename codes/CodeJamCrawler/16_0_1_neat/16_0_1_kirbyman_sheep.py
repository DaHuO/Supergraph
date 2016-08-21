Sleep={'6', '2', '9', '0', '8', '1', '4', '7', '5', '3'}
import sys
def one_solution(N):
    tmp=0
    solv=set()
    i=1
    while(Sleep!=solv and i<=10000000):
       tmp=i*N
       solv=solv.union(set(str(tmp)))
       i+=1
    if Sleep==solv:
        return str(tmp)
    else:
        return "INSOMNIA"
    
def Solution(file_name):
    stream=open(file_name,'r')
    read=((stream.readline()).split('\n'))[0]
    i=1
    while(read!=""):
        read=((stream.readline()).split('\n'))[0]
        if (read!=""):
            print("Case #{}: {}".format(i,one_solution(int(read))))
            i+=1
if __name__=="__main__":
    Solution(sys.argv[1])
    
    
