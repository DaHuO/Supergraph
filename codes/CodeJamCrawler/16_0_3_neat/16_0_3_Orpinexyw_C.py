
# def decimalToAny(num,n):
#    baseStr = {10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",16:"g",17:"h",18:"i",19:"j"}
#    new_num_str = ""
#    while num != 0:
#        remainder = num % n
#        if 20 > remainder > 9:
#            remainder_string = baseStr[remainder]
#        elif remainder >=20:
#            remainder_string = "("+str(remainder)+")"
#        else:
#            remainder_string = str(remainder)
#        new_num_str = remainder_string+new_num_str
#        num = num / n
#    return new_num_str

import math

def isPrime(n):  
    if n <= 1:  
        return False 
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:  
            return i 
    return -1

def anyToDecimal(num,n):
   baseStr = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
              "a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19}
   new_num = 0
   nNum = len(num) - 1
   for i in num:         
       new_num = new_num  + baseStr[i]*pow(n,nNum)
       nNum = nNum -1 
   return new_num

def main():
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')
    T = int(fin.readline())
    for t in xrange(T):
        fout.write('Case #{}:\n'.format(t + 1))
        N, J = map(int, fin.readline().split())
        s = ['0' for _ in xrange(N)]
        s[0] = s[-1] = '1'
        cnt = 0
        while True:
            for i in xrange(N - 2):
                if s[N - i - 2] == '0':
                    s[N - i - 2] = '1'
                    break
                else:
                    s[N - i - 2] = '0'
            ans = []
            flag = True
            for i in xrange(2, 11):
                ans.append(isPrime(anyToDecimal("".join(s), i)))
                if ans[-1] == -1:
                    flag = False
                    break
            if flag:
                fout.write('{} {}\n'.format("".join(s), ' '.join(map(str, ans))))
                cnt += 1
            if cnt == J:
                break
    fout.close()



if __name__ == "__main__":
    main()