#!/usr/bin/env python

def has_enough_letters(d, char_count):
    word_map = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}

    for c in word_map[d]:
        if c not in char_count or char_count[c] <= 0:
            return False
        if (d == 3 or d == 7) and char_count['E'] < 2:
            return False
        if d == 9 and char_count['N'] < 2:
            return False

    return True

def use_dig(d, char_count):
    word_map = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}
   
    for c in word_map[d]:
        char_count[c] -= 1
   
def unuse_dig(d, char_count):
    word_map = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}
   
    for c in word_map[d]:
        char_count[c] += 1
   
def empty(char_count):
    for k, v in char_count.items():
        if v != 0:
            return False
    return True

def get_phone_number_helper(n, char_count, s):
    if empty(char_count):
        return True

    for d in range(10):
        if has_enough_letters(d, char_count):
            use_dig(d, char_count)
            s += str(d)
            if get_phone_number_helper(n, char_count, s):
                return True 
            unuse_dig(d, char_count)    
            s.pop() 
   
    return False

def get_phone_number(n):
    char_count = {}
    for ni in n:
        if ni not in char_count:
            char_count[ni] = 1
        else:
            char_count[ni] += 1

    phone_num = ['']
    get_phone_number_helper(n, char_count, phone_num)
    return ''.join(phone_num)

if __name__ == '__main__':
    T = int(raw_input())
    for tc in range(1, T + 1):
        num = raw_input()
        print 'Case #%d: %s' % (tc, get_phone_number(num))
