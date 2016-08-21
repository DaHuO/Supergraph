'''
Created on 13.04.2013

@author: Alex
'''
def analyse(n):
    if n == 0:
        return 'INSOMNIA'
    not_seen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_n = n
    multiplier = 1
    while len(not_seen) > 0:
        current_n = multiplier * n
        for char in str(current_n):
            if char in not_seen:
                not_seen.remove(char)            
        multiplier += 1
    return str(current_n)
    
if __name__ == '__main__':
    f = open('in/A-large.in', mode='r')
    g = open('out/A-large.out', mode='w')
    n = int(f.readline())
    for i in range(1,n+1):
        n = int(f.readline())
        g.write('Case #' + str(i) + ': ' + analyse(n) + '\n') 