def find_sub(l):   #not recurring
    n = len(l)
    l_rev = list(reversed(l))
    return l[0:n-l_rev.index(0)]

def flip(l, m):  #m = no of flips
    n = len(l)
    sub_l = l[0:m+1]
    rev_sub_l = list(reversed(sub_l))
    l_out = []
    for i in rev_sub_l:
        l_out.append(int(not i))
    return l_out+l[m+1:]
        
def find_flip(l):
    n = len(l)
    if 1 not in l:
        return [1]*n
    i = l.index(1)
    return [1]*i+l[i:]

def main_algo(l):
    n = len(l)
    m = n-list(reversed(l)).index(1)-1
    return flip(l, m)



def count(l1):
    l =  find_sub(l1)
    count = 0
    while 1:
        if 1 not in l:
            break
        if l[0] == 1:
            count = count - 1
        l = find_flip(l)
        count = count + 1
        if 1 not in l:
            break
        l = main_algo(l)
        count = count + 1
    return count+1

def answer(l):
    if 0 not in l:
        return 0
    elif 1 not in l:
        return 1
    else: return count(l)

def f(x):
    if x=='+':
        return 1
    else: return 0

    
t=int(raw_input())
for i in range(t):
    c=raw_input()
    c1=list(c)
    l=map(f,c1)
    print "Case #{}: {}".format(i+1, answer(l))

