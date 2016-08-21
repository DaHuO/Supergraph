import math

def lowest_divisor(number):
    for x in range(2,min(int(math.sqrt(number))+3,1500)):
        if(number%x==0):
            return x
    return -1

def isCoinJam(number):
    divisors=[]
    for i in range(2,11):
        based_num=int(str(number),i)
        divisor=lowest_divisor(based_num)
        if(divisor==-1):
            break
        divisors.append(divisor)
    else:
        print(number,end=" ")
        for div in range(8):
            print(divisors[div],end=" ")
        print(divisors[8])
        return True
    return False

def readFile(path=r"C:\Users\Saar\Desktop\ap.txt"):
    with open(path,'r') as f:
        lst=f.read().splitlines()
    return lst

if __name__ == '__main__':
    file=readFile(r"C:\Users\Saar\Desktop\C-large.in")
    del(file[0])
    N,J=file[0].split(" ")
    N=int(N)
    J=int(J)
    default_number=10**(N-1)+1
    counter=0
    print("Case #1:")
    for x in range(int(('1'*(N-2)),2)):
        numb=default_number+int(bin(x)[2:])*10
        if(isCoinJam(numb)):
            counter+=1
        if(counter>=J):
            break