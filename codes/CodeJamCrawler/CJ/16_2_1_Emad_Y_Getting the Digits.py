# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:58:50 2016

@author: Emad Yehya
"""

inp = open('A-large.in', 'r')
o = open('out.txt', 'w')

def char_pos(c):
    return ord(c)- ord('A')

T = int(inp.readline())
for t in range(1, T+1):
    S = inp.readline()[:-1]
    print S
    NB = [0]*26
    ans = [0]*10
    for i in S:
        NB[ord(i) - ord('A')] += 1
        
    #zero
    ans[0] += NB[char_pos('Z')]
    s = "ZERO"
    for c in s:
        NB[char_pos(c)] -= ans[0]
        
    ans[2] += NB[char_pos('W')]
    s = "TWO"
    for c in s:
        NB[char_pos(c)] -= ans[2]
    
    ans[4] += NB[char_pos('U')]
    s = "FOUR"
    for c in s:
        NB[char_pos(c)] -= ans[4]
    
    ans[5] += NB[char_pos('F')]
    s = "FIVE"
    for c in s:
        NB[char_pos(c)] -= ans[5]
        
    ans[6] += NB[char_pos('X')]
    s = "SIX"
    for c in s:
        NB[char_pos(c)] -= ans[6]
        
    ans[7] += NB[char_pos('V')]
    s = "SEVEN"
    for c in s:
        NB[char_pos(c)] -= ans[7]
        
    ans[8] += NB[char_pos('G')]
    s = "EIGHT"
    for c in s:
        NB[char_pos(c)] -= ans[8]
        
    ans[9] += NB[char_pos('I')]
    s = "NINE"
    for c in s:
        NB[char_pos(c)] -= ans[9]
        
    ans[3] += NB[char_pos('T')]
    s = "THREE"
    for c in s:
        NB[char_pos(c)] -= ans[3]
        
    ans[1] += NB[char_pos('O')]
    s = "ONE"
    for c in s:
        NB[char_pos(c)] -= ans[7]
    sans = ""
    for i in range(0, 10):
        sans += str(i)*ans[i]
        
    o.write("Case #" + str(t) + ": " + sans + "\n")
        
        
        