#!usr/local/bin/python
import sys
data = sys.stdin.readlines()

number_of_cases = int(data[0])

letters_to_numbers = {
    'z': ('zero', 0),
    'x': ('six', 6),
    'w': ('two', 2),
    'u': ('four', 4),
    'g': ('eight', 8),
    'f': ('five', 5),
    'h': ('three', 3),
    's': ('seven', 7),
    'o': ('one', 1),
    'i': ('nine', 9),
}

ordered_letters = 'zxwugfhsoi'


def convert_string(mess):
    """converts the mess in a hashtable of chars to number of occurrences
    """
    result = {}
    mess = mess.strip()
    mess = mess.lower()
    for char in mess:
        if result.get(char) is not None:
            result[char] += 1
        else:
            result[char] = 1
    return result


def remove_from_hash(number, _hash):
    """takes in a number, like 'three' and removes
    it from the hash
    """
    for char in number:
        _hash[char] -= 1
        if _hash[char] <= 0:
            del _hash[char]
    return _hash


def solve_one(mess):
    """Returns the last int marked"""
    result = ''
    clean_hash = convert_string(mess)
    for letter in ordered_letters:
        for x in xrange(clean_hash.get(letter, 0)):
            remove_from_hash(letters_to_numbers[letter][0], clean_hash)
            result += str(letters_to_numbers[letter][1])

    return ''.join(sorted(result))

    return mess


for i in xrange(number_of_cases):
    max_hit = solve_one(data[i + 1])
    print "Case #%s: %s" % (i + 1, max_hit)
