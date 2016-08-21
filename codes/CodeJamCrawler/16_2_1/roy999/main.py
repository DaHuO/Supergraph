from itertools import count

DIGITS_WORDS = [
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
]

DIGITS_WORDS_STATISTICS = []

UNIQUE = []


def init():
    global DIGITS_WORDS

    digits_words_stats = [None] * 10
    for i, word in enumerate(DIGITS_WORDS):
        stats = {}
        for s in word:
            stats.setdefault(s, 0)
            stats[s] += 1
        digits_words_stats[i] = stats.items()

    global DIGITS_WORDS_STATISTICS
    DIGITS_WORDS_STATISTICS = digits_words_stats

    digits = set(range(10))
    unique = []

    for level in count():
        unique.append([])
        digits_words = [(i, DIGITS_WORDS[i]) for i in digits]
        for i, word in digits_words:
            for s in word:
                for j, other in digits_words:
                    if i != j and s in other:
                        break
                else:
                    unique[level].append((s, i))
                    digits.discard(i)
                    break

        if not digits:
            break

    global UNIQUE
    UNIQUE = unique

init()


def process(input_file, out):

    t = int(input_file.readline())

    for i in range(1, t + 1):
        string = input_file.readline()

        result = ''.join(map(str, solve(string)))
        out.write("Case #%i: %s\n" % (i, result))


def solve(string):
    stats = {}
    digits = []

    for s in string:
        stats.setdefault(s, 0)
        stats[s] += 1

    for unique in UNIQUE:
        for s, i in unique:
            while stats.get(s, 0) > 0:
                digits.append(i)

                for w, k in DIGITS_WORDS_STATISTICS[i]:
                    stats[w] -= k

    digits.sort()
    return digits






