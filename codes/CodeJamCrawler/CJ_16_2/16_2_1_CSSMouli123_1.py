from __future__ import print_function
t=int(raw_input().strip())
chars=set('ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE')
nums=['ONE','THREE']

for _ in xrange(t):
    print('Case #{}:'.replace('{}',str(_+1)),end=' ')
    s=sorted(list(raw_input().strip()))
    count={i:0 for i in xrange(10)}
    if 'Z' in s:
        count[0]=s.count('Z')
    
    if 'G' in s:
        count[8]=s.count('G')
    
    if 'W' in s:
        count[2]=s.count('W')

    if 'S' in s:
        x=s.count('S')
        if 'X' in s:
            count[6]=s.count('X')
        count[7]=x-count[6]

    if 'F' in s:
        x=s.count('F')
        if 'V' in s:
            count[5]=s.count('V')-count[7]
        count[4]=x-count[5]
    if 'O' in s:
        x=s.count('O')
        count[1]=x-count[0]-count[2]-count[4]
        
    if 'N' in s:
        count[9]=(s.count('N')-count[7]-count[1])/2

    if 'H' in s:
        x=s.count('H')
        count[3]=x-count[8]
    
    for i in xrange(10):
        print(str(i)*count[i],end='')
    print('')
    
    
