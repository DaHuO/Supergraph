import numpy as np

import fileinput


def prime(N):
    if N % 2 == 0:
        return False
    else:
        for i in range(3,int(N**0.5),2):
            if N % i == 0:
                return False
    return True
    


def get_number(N):
    
    while True:
        sizes=N-2
        s = list(np.random.randint(2, size=sizes))
        s.insert(0,1)
        s.append(1)
        num=''.join(str(i) for i in s)
        factors=[]
        check=True

        for i in range(2,11):
            change_num = int(num,i)
            if not prime(change_num):

                if change_num % 2 ==0:
                    factors.append(str(2))
                else:
                    for j in range(3,int(change_num**0.5),2):
                       if change_num%j==0:
                           factors.append(str(j))
                           break
            else:
                check=0
                break
        if check:
            return num,factors


if __name__ == "__main__":

    f = fileinput.input()
    T=int(f.readline())
    for case in range(1,T+1):
         Val = [int(x) for x in f.readline().split()]
         N=Val[0]
         C=Val[1]
         output={}
         c=0
         print("Case #{0}:".format(case))
         while c<C:
            T=get_number(N)
            if T[0] in output.keys():
                continue
            else:
                output[T[0]]=T[1]
                c+=1
                print (T[0]+' '+ ' '.join(T[1]))