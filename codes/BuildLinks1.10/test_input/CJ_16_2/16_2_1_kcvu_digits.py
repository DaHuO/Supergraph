from collections import Counter

WORDS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
UNIQUES = [{'Z':0,'W':2,'U':4,'X':6,'G':8},
           {'H':3,'F':5,'S':7},
           {'O':1,'I':9}]

def find_numbers(char_counter, total):
    numbers = []
    cnt = 0
    for unique_chars in UNIQUES:
        u_chars = unique_chars.keys()
        for c in u_chars:
            if c in char_counter and char_counter[c] > 0:
                occurences = char_counter[c]
                for i in range(occurences):
                    v = unique_chars[c]
                    numbers.append(v)
                    for word_c in WORDS[v]:
                        char_counter[word_c] -= 1
                        cnt += 1
                if cnt >= total:
                    numbers.sort()
                    return numbers
    numbers.sort()
    return numbers



if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as infile:
        _ = infile.readline()
        line_index = 0
        for line in infile:
            line_index += 1
            line = line.strip()
            char_counter = Counter(line)
            print "Case #%d: %s" % (line_index, ''.join([str(d) for d in find_numbers(char_counter, len(line))]))