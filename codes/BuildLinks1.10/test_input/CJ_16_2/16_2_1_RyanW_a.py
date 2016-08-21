"""
Digits in non-decreasing order.
"""


words = tuple('ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE'.split())
mapping = {word: digit for digit,word in enumerate(words)}


def memo(f):
    """memoization decorator, taken from Peter Norvig's Design of Computer
    Programs course on Udacity.com"""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            result = cache[args] = f(*args)
            return result
        except TypeError:  # unhashable argument
            return f(*args)
    return _f


def try_remove_word(s, word):
    s2 = s

    for char in word:
        if char not in s:
            return s
        s2 = s2.replace(char, '', 1)

    return s2


@memo
def detect_words(s, words=words):
    if not s:
        return ()  # all words detected

    if not words:
        return None  # failure path

    word, rest = words[0], words[1:]
    s2 = try_remove_word(s, word)
    word_detected = len(s2) < len(s)

    # remove word from s and recurse if s gets smaller
    branch1 = None
    if word_detected:
        branch1 = detect_words(s2, words)
    if branch1 is not None:
        return branch1 + (word,)

    # remove word from s and words
    branch2 = None
    if word_detected:
        branch2 = detect_words(s2, rest)
    if branch2 is not None:
        return branch2 + (word,)

    # remove word from words, not from s
    branch3 = detect_words(s, rest)
    if branch3 is not None:
        return branch3


def map_words(words):
    return (mapping[word] for word in words)


def phone_number(s):
    return ''.join(str(n) for n in sorted(map_words(detect_words(s))))


def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        S = raw_input()
        print 'Case #{}: {}'.format(t, phone_number(S))


if __name__ == '__main__':
    main()
