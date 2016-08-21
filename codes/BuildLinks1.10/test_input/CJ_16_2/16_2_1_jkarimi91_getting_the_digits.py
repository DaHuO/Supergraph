
# coding: utf-8

# In[ ]:

t = int(raw_input())
for case in range(1,t+1):
    s = raw_input().lower()
    digits = []
    count = [0]*26
    for letter in s:
        count[ord(letter)-97] += 1
    
    while count[ord('z')-97] > 0:
        digits.append(0)
        for letter in 'zero':
            count[ord(letter)-97] -= 1
    while count[ord('w')-97] > 0:
        digits.append(2)
        for letter in 'two':
            count[ord(letter)-97] -= 1
    while count[ord('g')-97] > 0:
        digits.append(8)
        for letter in 'eight':
            count[ord(letter)-97] -= 1
    while count[ord('x')-97] > 0:
        digits.append(6)
        for letter in 'six':
            count[ord(letter)-97] -= 1
    while count[ord('u')-97] > 0:
        digits.append(4)
        for letter in 'four':
            count[ord(letter)-97] -= 1
    while count[ord('r')-97] > 0:
        digits.append(3)
        for letter in 'three':
            count[ord(letter)-97] -= 1
    while count[ord('f')-97] > 0:
        digits.append(5)
        for letter in 'five':
            count[ord(letter)-97] -= 1
    while count[ord('s')-97] > 0:
        digits.append(7)
        for letter in 'seven':
            count[ord(letter)-97] -= 1
    while count[ord('o')-97] > 0:
        digits.append(1)
        for letter in 'one':
            count[ord(letter)-97] -= 1
    while count[ord('n')-97] > 0:
        digits.append(9)
        for letter in 'nine':
            count[ord(letter)-97] -= 1
        
    result = ''.join(map(str,sorted(digits)))
    
    print "Case #{}: {}".format(case,result)


            
        
        


# In[ ]:



