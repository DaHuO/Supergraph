from __future__ import print_function
t = int(raw_input())

for i in xrange(1, t + 1):
    S = raw_input()
    count = [0 for x in xrange(256)]
    for j in xrange(0, len(S)):
        count[ord(S[j])] = count[ord(S[j])] + 1
    
    num = [0 for x in xrange(10)]
    
    # ZERO
    num[0] = count[ord('Z')]
    count[ord('Z')] -= num[0]
    count[ord('E')] -= num[0]
    count[ord('R')] -= num[0]
    count[ord('O')] -= num[0]
    
    # TWO
    num[2] = count[ord('W')]
    count[ord('T')] -= num[2]
    count[ord('w')] -= num[2]
    count[ord('O')] -= num[2]
    
    # FOUR
    num[4] = count[ord('U')]
    count[ord('F')] -= num[4]
    count[ord('O')] -= num[4]
    count[ord('U')] -= num[4]
    count[ord('R')] -= num[4]
    
    # SIX
    num[6] = count[ord('X')]
    count[ord('S')] -= num[6]
    count[ord('I')] -= num[6]
    count[ord('X')] -= num[6]
    
    # EIGHT
    num[8] = count[ord('G')]
    count[ord('E')] -= num[8]
    count[ord('I')] -= num[8]
    count[ord('G')] -= num[8]
    count[ord('H')] -= num[8]
    count[ord('T')] -= num[8]
    
    # ONE
    num[1] = count[ord('O')]
    count[ord('O')] -= num[1]
    count[ord('N')] -= num[1]
    count[ord('E')] -= num[1]
    
    # THREE
    num[3] = count[ord('T')]
    count[ord('T')] -= num[3]
    count[ord('H')] -= num[3]
    count[ord('R')] -= num[3]
    count[ord('E')] -= num[3]
    count[ord('E')] -= num[3]
    
    # FIVE
    num[5] = count[ord('F')]
    count[ord('F')] -= num[5]
    count[ord('I')] -= num[5]
    count[ord('V')] -= num[5]
    count[ord('E')] -= num[5]
    
    # SEVEN
    num[7] = count[ord('V')]
    count[ord('S')] -= num[7]
    count[ord('E')] -= num[7]
    count[ord('V')] -= num[7]
    count[ord('E')] -= num[7]
    count[ord('N')] -= num[7]
    
    # NINE
    num[9] = count[ord('E')]
    count[ord('N')] -= num[9]
    count[ord('I')] -= num[9]
    count[ord('N')] -= num[9]
    count[ord('E')] -= num[9]
    
    print("Case #{}: ".format(i), end="")
    for j in xrange(10):
        for k in xrange(num[j]):
            print(j, end="")
    print("")
