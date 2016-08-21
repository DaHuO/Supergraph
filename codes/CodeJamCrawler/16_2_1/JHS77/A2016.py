import sys

def solve(S):
    
    zero = S.count('Z')
    two = S.count('W')
    four = S.count('U')
    five = S.count('F') - four 
    six = S.count('X')
    seven = S.count('S') - six 
    eight = S.count('G')
    nine = S.count('I') - five - six - eight 
    one = S.count('O') - two - four - zero 
    three = S.count('R') - four - zero 
    
    
    res = '0'*zero + '1'*one + '2'*two+'3'*three+'4'*four+'5'*five + '6'*six+'7'*seven+'8'*eight+'9'*nine
#    print [zero, one, two, three, four, five, six, seven, eight, nine]
    return res
        

if __name__ == "__main__":
    f = open('A-2016.in','r')
    #f = open('practice','r')
    T = int(f.readline().strip())
    ctr = 0 
    w = open('a-large16.out','w')
    for i in xrange(T):
        ctr += 1
        N = map(str, f.readline().strip().split(' '))
        res =  "Case #" + str(ctr) + ": " + str(solve(N[0]))
        print res
        w.write(res + '\n')
    w.close() 
