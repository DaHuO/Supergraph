

def replace(s):
    r = ""
    for i in s:
        if i == "+": r += '-'
        else: r += '+'
    return r

def findMinTosses(stk):
    s = stk[-1::-1]
    flips, i, l = 0, 0, len(s)
    while i < l and s[i] == '+': i = i + 1
    
    while i < l:
        while i < l and s[i] == '-':
            i = i + 1
        flips = flips + 1
        s = replace(s)
        
    return flips

def main():
    t = int(input())
    for i in range(t):
        stk = input()
        print("Case #%s:" %(i+1), findMinTosses(stk))


main()
