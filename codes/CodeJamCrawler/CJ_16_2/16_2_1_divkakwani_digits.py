

allnums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

allnums = ['ONE', 'THREE', 'FIVE', 'SEVEN', 'NINE']

# if there is a 'Z' -> zero must
# if 'W' <-> TWO
# if 'U' <-> FOUR
# if 'X' <-> SIX
# if 'G' <-> EIGHT

# Next Level
# if 'F' -> Five
# if 'T' -> Three
# if 'S' -> Seven
# if 'O' -> One

# else Nine

def remove(freqs, word):
    for c in word:
        freqs[c] -= 1

def iter_decom(freqs):

    numlist = []


    while True:
        if freqs['Z'] > 0:
            remove(freqs, 'ZERO')
            numlist.append(str(0))
        elif freqs['W'] > 0:
            remove(freqs, 'TWO')
            numlist.append(str(2))
        elif freqs['U'] > 0:
            remove(freqs, 'FOUR')
            numlist.append(str(4))
        elif freqs['X'] > 0:
            remove(freqs, 'SIX')
            numlist.append(str(6))
        elif freqs['G'] > 0:
            remove(freqs, 'EIGHT')
            numlist.append(str(8))
        elif freqs['F'] > 0:
            remove(freqs, 'FIVE')
            numlist.append(str(5))
        elif freqs['T'] > 0:
            remove(freqs, 'THREE')
            numlist.append(str(3))
        elif freqs['S'] > 0:
            remove(freqs, 'SEVEN')
            numlist.append(str(7))
        elif freqs['O'] > 0:
            remove(freqs, 'ONE')
            numlist.append(str(1))
        elif freqs['N'] > 1:
            remove(freqs, 'NINE')
            numlist.append(str(9))
        else:
            break

    return ''.join(sorted(numlist))


def get_freqs(s):
    f = {chr(c): 0 for c in range(65, 91)}
    for c in s:
        f[c] += 1
    return f

t = int(input())

for casid in range(1, t+1):
    s = input()
    print("Case #%s: %s" % (casid, iter_decom(get_freqs(s))))
