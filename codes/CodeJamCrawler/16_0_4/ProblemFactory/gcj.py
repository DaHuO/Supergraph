import math
def perms(n):
    if not n:
        return
    for i in range(2**n):
        s = bin(i)[2:]
        s = "0" * (n-len(s)) + s
        yield s


def find_factor(num):
    if num == 1 or num == 2:
        return False
    for i in range(2,min(1000,num)):
        if num % i == 0:
            return i
    return False
        
    
    
def jamcoins(N,J):
    gen = perms(N-2)
    d = dict()
    while (len(d) < J):
        num_str = '1'+next(gen)+'1'
        temp_list = []
        for i in range(2,11):
            temp = find_factor(int(num_str,i))
            temp_list.append(temp)
            if type(temp) == bool:
                break
        else:
            d[num_str] = temp_list
    return d
        

N = 32
J = 500
if __name__=='__main__':
    with open('output.txt','w') as f:
        f.write('Case #1:\n')
        d = jamcoins(N,J)
        for i in d:
            f.write(i+' ')
            for j in d[i]:
                f.write(str(j) + ' ')
            f.write('\n')


        
