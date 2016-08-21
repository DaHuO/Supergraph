import sys, math
inp = open("in.txt")
out = open("out.txt","w+")
sys.stdout = out
tc = 0

class ImpossibleError(Exception):
	pass

t = int(inp.readline())

def print_case(case, result):
    debug("Case #%d: %s" % (case, str(result)))
    print "Case #%d: %s" % (case, str(result))

def debug(message):
	if len(sys.argv) > 1 and sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out

UNIQUE_DIGITS = [
    ("X", "SIX", 6),
    ("U", "FOUR", 4),
    ("Z", "ZERO", 0),
    ("W", "TWO", 2),
    ("G", "EIGHT", 8)
]
DIGITS = [
    ("ONE", 1),
    ("THREE", 3),
    ("FIVE", 5),
    ("SEVEN", 7),
    ("NINE", 9),
]

def remove_uniques(a):
    result = []
    for unique_letter, word, digit in UNIQUE_DIGITS:
        while(unique_letter in a):
            for letter in word:
                a.remove(letter)
            result.append(digit)
    return result


def get_result(original_word):
    for wdigit, digit in DIGITS:
        word = list(original_word)
        if not all([letter in word for letter in wdigit]):
            continue
        for letter in wdigit:
            word.remove(letter)
        if len(word) == 0:
            result = []
        else:
            result = get_result(word)
        if result != -1:
            return [digit] + result
    return -1

for tc in xrange(t):
    word = list(inp.readline().strip())
    
    result = remove_uniques(word)
    if len(word) != 0:
        result += get_result(word)
    
    print_case(tc+1, "".join([str(x) for x in sorted(result)]))