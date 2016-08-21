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


@memo
def last_word(s):
    letters = iter(s)
    new_s = letters.next()

    for letter in letters:
        front = new_s[0]
        new_s = letter + new_s if letter >= front else new_s + letter

    return new_s


def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        S = raw_input()
        print 'Case #{}: {}'.format(t, last_word(S))


if __name__ == '__main__':
    main()
