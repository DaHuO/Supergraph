from collections import Counter

words = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN',
         'EIGHT', 'NINE']

letters = list(map(lambda word: Counter(word), words))
uniques = {
    'Z': 0,
    'W': 2,
    'U': 4,
    'X': 6,
    'G': 8
}

t = int(input().strip())
s = []

for i in range(t):
    s.append(input().strip())

def subtract(counter, number, count):
    subtraction = Counter(letters[number])
    for letter in subtraction:
        subtraction[letter] *= count
    counter -= subtraction
    return [number]*count

for i, scrambled in enumerate(s):
    counter = Counter(scrambled)
    numbers = []

    for letter, number in uniques.items():
        if letter in counter:
            numbers += subtract(counter, number, counter[letter])

    if len(counter) > 0:
        if 'S' in counter:
            numbers += subtract(counter, 7, counter['S'])
        if 'V' in counter:
            numbers += subtract(counter, 5, counter['V'])
        if 'T' in counter:
            numbers += subtract(counter, 3, counter['T'])
        if 'I' in counter:
            numbers += subtract(counter, 9, counter['I'])
        if 'O' in counter:
            numbers += subtract(counter, 1, counter['O'])

    assert len(counter) == 0, str(counter)
    numbers.sort()
    print('Case #{}: {}'.format(i + 1, ''.join(map(str, numbers))))
