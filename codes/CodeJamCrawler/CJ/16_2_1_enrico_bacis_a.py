from pep import Counter

def single(func):
    return func(raw_input())

def row(func):
    return map(func, raw_input().split())

def printcase(case, out, pattern='Case #%d: %s'):
    print pattern % (case, out)

def repeat(func, times):
    return [func() for _ in xrange(times)]

numbers = {0: 'ZERO', 1: 'ONE', 2: 'TWO',   3: 'THREE', 4: 'FOUR',
           5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}
numbers = {k: Counter(v) for k,v in numbers.iteritems()}

def number_from(letters, acc):
    if not letters: return ''.join(map(str, sorted(acc)))
    for num, numletters in numbers.items():
        if numletters <= letters:
            res = number_from(letters - numletters, acc[:] + [num])
            if res is not None: return res

T = single(int)
for t in xrange(1, T + 1):
    letters = Counter(raw_input())
    res = number_from(letters, [])
    printcase(t, res)

