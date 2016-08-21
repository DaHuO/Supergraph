'''
Created on 09/04/2016

@author: gandalf
'''

def sheep(n):
    if ( n <= 0):
        return -1
    booleanMap = {x:True for x in range(0,10)}
    count = 0
    while len(booleanMap) > 0:
        count += 1
        number = count * n
        
        while number != 0:
            digit = number % 10
            try:
                del booleanMap[digit]
            except KeyError:
                pass
            number /= 10
    return count * n

def main():
    T = input()
    T += 1
    for i in range(1,T):
        N = input()
         
        result = sheep(N)
        
        if result <= -1:
            print "Case #%d: INSOMNIA" % i
        else:
            print "Case #%d: %d" % (i,result)

if __name__ == '__main__':
    main()