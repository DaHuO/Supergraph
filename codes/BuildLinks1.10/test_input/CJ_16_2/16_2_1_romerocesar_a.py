import collections
import logging

logging.basicConfig(level=logging.WARN)

candidates = collections.defaultdict(list)
digit = {}

def init():
    words = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    for word in words:
        for c in word:
            candidates[c].append(word)
    logging.debug(candidates)
    for d,w in enumerate(words):
        digit[w] = str(d)
    logging.debug(digit)

def clean(s, candidate):
    logging.debug('clean({}, {})'.format(s,candidate))
    if len(s) < len(candidate):
        return s, candidate
    ans = []
    for c in s:
        if c in candidate:
            candidate.remove(c)
        else:
            ans.append(c)
    logging.debug('candidate: {}'.format(candidate))
    logging.info('cleaned: {}'.format(str(ans)))
    return ''.join(ans), candidate


def phone_number(s):
    logging.debug('phone_number({})'.format(s))
    if not s:
        return ''
    for c in s:
        for candidate in candidates[c]:
            d = digit[candidate]
            ns, rest = clean(s, list(candidate))
            if rest:
                continue
            pn = phone_number(ns)
            if pn == False:
                continue
            return ''.join(list(sorted(d + pn)))
    else:
         return False       

if __name__ == '__main__':
    init()
    T = int(input())
    for case in range(T):
        S = input()
        print('Case #{}: {}'.format(case + 1, phone_number(S)))

