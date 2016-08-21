import sys 
from sets import Set

def swap(x):
    if x == '+': return '-'
    else: return '+'

def happy(x):
    if len(Set(x)) == 1 and '+' in Set(x): return True
    else: return False

lines = sys.stdin.readlines()
for i in range((int(lines[0]))):
    s = list(lines[i+1].strip())
    k = 0
    while not happy(s):
        j = len(s)
        while s[j-1] != '-' and j > 0: j -= 1
        s = [swap(x) for x in s[:j]] + s[j:]
        k += 1
    print 'Case #'+str(i+1)+': '+str(k)
