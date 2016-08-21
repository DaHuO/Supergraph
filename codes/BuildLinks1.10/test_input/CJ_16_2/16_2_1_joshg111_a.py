import fileinput
from collections import deque

       
def in_ana(h, digit_str):
    
    for c in digit_str:
        if c not in h:
            return False
        
        if h[c] < digits_h[digit_str][c]:
            return False
        
    return True
    
def extract_ana(h, digit_str):
    res = dict(h)
    for c in digit_str:
        res[c] -= 1
        if res[c] == 0:
            del res[c]
        
    return res
        
def find_sub_d(h, digit_str, res = ''):
    
    if not h:
        return res
    
    for digit_str in digits_l:
        while in_ana(h, digit_str):
            extract_ana(h, digit_str)
            res += d_to_n[digit_str]
            return find_sub_d(h, digit_str, res)

        
def get_h(line):
    h = {}
    for c in line:
        if c not in h:
            h[c] = 1
        else:
            h[c] += 1

    return h

    
def find_digits(h, s='', d_i = 0):
    global digits_l
    res = ''
        
    if not h:
        return s
        
    
    for i, digit_str in enumerate(digits_l[d_i:]):
        if in_ana(h, digit_str):
            h_n = extract_ana(h, digit_str)
            #print "s = " + str(s)
            res += find_digits(h_n, s+d_to_n[digit_str], i+d_i)
           
        # if h:
            # print "h = " + str(h)
            # print "res = " + str(res)
            #This case we did not find the right sequence. Need to backtrack. 
            # i = int(res.pop(0))
            # digits_l = digits_l[i+1:]
            # print "digits = " + str(digits_l)
            # h = get_h(line)
            # res = []
    
    #return ''.join(res)
    #print "res = " + str(res)
    return res
    
digits_l = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
digits_h = {}
for digit in digits_l:
    digits_h[digit] = {}
    for c in digit:
        if c not in digits_h[digit]:
            digits_h[digit][c] = 1
        else:
            digits_h[digit][c] += 1
    
d_to_n = {}
for i, digit in enumerate(digits_l):
    d_to_n[digit] = str(i)
    
f = open('workfile', 'w')

if __name__ == "__main__":
    
    i = 1
    f_i = fileinput.input()
    tests = f_i.next()
    for line in f_i:
        #s = map(int, line.split(' '))
        res = find_digits(get_h(line.rstrip()))
        f.write("Case #" + str(i) + ": " + str(res) + "\n")
        i += 1
        
    f.close()
    f_i.close()