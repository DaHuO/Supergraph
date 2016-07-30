
before = [[0, 2], [0, 1], [2 , 1]]

def new_seq(seq):
    res = []
    for c in seq:
        res.extend(before[c])
    return res

def final_seq(n):
    res = [0]
    for i in range(n):
        res = new_seq(res)
    return res

def counts(seq):
    res = [0, 0, 0]
    for c in seq:
        res[c] += 1
    return res

def char_seq(seq, chars):
    res = []
    for c in seq:
        res.append(chars[c])
    return res

def sort_seq(seq):
    if len(seq) == 1:
        return seq

    l = len(seq) // 2

    a, b = sort_seq(seq[:l]), sort_seq(seq[l:])
   
    if a < b:
        return a + b
    return b + a

def winner(a, b):
    if a == b:
        raise Exception
    if [a, b] == ['P', 'S'] or [a, b] == ['S', 'P']:
        return 'S'
    return min(a, b)

def check(seq):
    res = seq

    while (len(res) > 1):
        nres = []
        for i in range(len(res) // 2):
            nres.append(winner(res[2*i], res[2*i+1]))
        res = nres


def solve():
    n, r, p, s = map(int, input().split())

    seq = final_seq(n)
    cou = counts(seq)

    chseq = []
    if [p, r, s] == cou:
        chseq.append(char_seq(seq, ['P', 'R', 'S']))
    if [r, s, p] == cou:
        chseq.append(char_seq(seq, ['R', 'S', 'P']))
    if [s, p, r] == cou:
        chseq.append(char_seq(seq, ['S', 'P', 'R']))

    if len(chseq) == 0:
        return "IMPOSSIBLE"

    chseq = map(sort_seq, chseq)

    res = "".join(min(chseq))
    
    check(res)
    return res

T = int(input())
for t in range(T):
    print("Case #{}: {}".format(t+1, solve()))
