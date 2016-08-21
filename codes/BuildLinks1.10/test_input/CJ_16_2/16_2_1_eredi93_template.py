import sys

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#numbers = dic

def contains(a,b):
    a, b = list(a), list(b)
    for char in a:
        if char not in b:
            return False
        b.remove(char)
    return True

def a(number, line):
    #print(number)
    #print("found {}".format(number))
    for n in number.upper():
        i = line.index(n)
        line = line[:i] + line[i+1:]
         #   print(new_line)
    return line


def solve_algo(n, line):
    if not line:
        return True, []

    if not n:
        return False, []

    for number in n:
        if contains(number.upper(), line):
            new_line = a(number, line)
            taken_succ, seen_taken = solve_algo(n, new_line)
            # or maybe it's better not to consider it
            not_taken_succ, seen_not_taken = solve_algo(n[1:], line)
            # take the best
            if taken_succ:
                return True, seen_taken + [numbers.index(number)]
            elif not_taken_succ:
                return True, seen_not_taken
            else:
                return False, []
        else:
            return solve_algo(n[1:], line)

def algo(line):
    success, seen = solve_algo(numbers, line)
    assert(success)
    r =""
    for n in sorted(seen):
        r += str(n)
    return r


filename = sys.argv[1]
with open(filename) as f:
    f.readline()
    i = 1
    for line in f:
        line = line.strip()
        print("Case #{}: {}".format(i, algo(line)))
        i += 1
