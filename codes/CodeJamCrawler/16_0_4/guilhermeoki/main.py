'''
Created on 09/04/2016

@author: gandalf
'''

def solutions(start,end):
    result = ""

    for number in range(start,end):
        result += " "+str(number)
    return result
        
def fractiles(K,C,S):
    if K == 1:
        return " 1"
    if C == 1:
        if S < K:
            return " IMPOSSIBLE"
        else:
            return solutions(1,K+1)
    if S < K -1:
        return " IMPOSSIBLE"
    else:
        return solutions(2, K+1)

def main():
    T = input()
    
    for i in range(1,T+1):
        K,C,S = map(int,raw_input().split())
        result = fractiles(K, C, S)
        
        print "Case #%d:%s" % (i,result)
    

if __name__ == '__main__':
    main()