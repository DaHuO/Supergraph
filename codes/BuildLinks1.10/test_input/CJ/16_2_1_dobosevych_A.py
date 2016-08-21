T = int(input())

for i in range(T):
    phone = [0] * 10
    s = input()
    lst = [0] * 26
    for c in s:
        lst[ord(c) - ord('A')] += 1
    
    # ZERO
    phone[0] = lst[ord('Z') - ord('A')]
    for c in 'ZERO':
        lst[ord(c) - ord('A')] -= phone[0]
    
    # SIX
    phone[6] = lst[ord('X') - ord('A')]
    for c in 'SIX':
        lst[ord(c) - ord('A')] -= phone[6]
    
    # SEVEN
    phone[7] = lst[ord('S') - ord('A')]
    for c in 'SEVEN':
        lst[ord(c) - ord('A')] -= phone[7]
        
    # FIVE 
    phone[5] = lst[ord('V') - ord('A')]
    for c in 'FIVE':
        lst[ord(c) - ord('A')] -= phone[5]
    
    # FOUR
    phone[4] = lst[ord('F') - ord('A')]
    for c in 'FOUR':
        lst[ord(c) - ord('A')] -= phone[4]
        
    # TWO
    phone[2] = lst[ord('W') - ord('A')]
    for c in 'TWO':
        lst[ord(c) - ord('A')] -= phone[2]

    # THREE
    phone[3] = lst[ord('R') - ord('A')]
    for c in 'THREE':
        lst[ord(c) - ord('A')] -= phone[3]
    
    # EIGHT
    phone[8] = lst[ord('G') - ord('A')]
    for c in 'EIGHT':
        lst[ord(c) - ord('A')] -= phone[8]
    
    # ONE
    phone[1] = lst[ord('O') - ord('A')]
    for c in 'ONE':
        lst[ord(c) - ord('A')] -= phone[1]

    # NINE
    phone[9] = lst[ord('I') - ord('A')]
    for c in 'NINE':
        lst[ord(c) - ord('A')] -= phone[9]
    
    
    s = ''
    for j in range(10):
        s += phone[j] * str(j)
    
    print('Case #' + str(i + 1) + ': ' + s)
        
    
    