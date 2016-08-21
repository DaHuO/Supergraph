import sys
import operator


def read_one_line():
  return sys.stdin.readline().rstrip()


numbers = {
    'ONE': 1,
    'TWO': 2,
    'THREE': 3,
    'FOUR': 4,
    'FIVE': 5,
    'SIX': 6,
    'SEVEN': 7,
    'EIGHT': 8,
    'NINE': 9,
    'ZERO': 0
}

numbers_to_words = {v:k for k, v in numbers.iteritems()}

letters_to_candidates = {}

for literal, number in numbers.iteritems():
    for letter in literal:
        letters_to_candidates.setdefault(letter, [])
        letters_to_candidates[letter].append(number)
        letters_to_candidates[letter] = list(set(letters_to_candidates[letter]))


def remove_letters(string, letters):
    string = list(string)

    for letter in letters:
        string.remove(letter)

    return ''.join(string)



def decode(encoded):
    # phone number must be ascending
    decoded = []

    while len(encoded) != 0:
        occurrences = {}

        for letter in encoded:
            candidates = letters_to_candidates[letter]

            if len(candidates) == 1:
                num = candidates[0]
                decoded.append(num)
                word = numbers_to_words[num]
                encoded = remove_letters(encoded, word)
                continue

            for c in candidates:
                occurrences.setdefault(c, 0)
                occurrences[c] += 1

        occurrences = sorted(occurrences.items(), key=operator.itemgetter(1), reverse=True)

        for num, oc in occurrences:
            word = numbers_to_words[num]

            can_remove_word = all([encoded.count(letter) >= word.count(letter) for letter in word])

            if can_remove_word:
                decoded.append(num)
                encoded = remove_letters(encoded, word)

    return ''.join([str(num) for num in sorted(decoded)])


if __name__ == '__main__':
  num_cases = int(read_one_line())

  for case in xrange(num_cases):
    phone_encoded = read_one_line()

    phone_number = decode(phone_encoded)

    result = phone_number

    print 'Case #%d: %s' % (case + 1, result)