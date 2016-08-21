
# GCJ 2016 Qual B jeremy.holman@gmail.com

T = int(raw_input())


def reverse_stack(stack):
    def reverse_cake(cake):
        return '-' if cake is '+' else '+'
    for idx in xrange((len(stack)+1)/2):
        tmp = stack[idx]
        stack[idx] = reverse_cake(stack[-idx-1])
        stack[-idx-1] = reverse_cake(tmp)
    return stack

def flip_n(stack, n):
    return reverse_stack(stack[:n]) + stack[n:]

def initial_happy(stack):
    cnt = 0
    while cnt < len(stack) and stack[cnt] == '+':
        cnt += 1
    return cnt

def final_happy(stack):
    cnt = 0
    while cnt < len(stack) and stack[-cnt-1] == '+':
        cnt += 1
    return cnt

def count_flips(stack):
    ih = initial_happy(stack)
    if ih == len(stack):
        return 0
    fh = final_happy(stack)
    if ih == 0:
        return 1 + count_flips(flip_n(stack, len(stack)-fh))
    else:
        partial = flip_n(stack, ih)
        return 2 + count_flips(flip_n(partial, len(partial)-fh))

for t in xrange(T):
    X = list(raw_input())
    print "Case #%i: %i" % (t+1, count_flips(X))
