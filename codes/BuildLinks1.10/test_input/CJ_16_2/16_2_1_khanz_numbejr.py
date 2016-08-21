NUMBERS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT"\
           ,"NINE"]
def find_num(string, remaining, contain):
    if string == '':
        return contain
    elif not remaining:
        return False
    elif test(remaining[0])(string):
        guess = find_num(remove(string, remaining[0]), remaining, contain + (remaining[0],))
        if guess:
            return guess
        else:
            return find_num(string, remaining[1:], contain)
    else:
        return find_num(string, remaining[1:], contain)

def test(n):
    return TEST[n]

TEST = {}
def put(test, n):
    TEST[n] = test

def generic_test(n):
    def helper(string):
        for c in NUMBERS[n]:
            if c not in string:
                return False
        return True
    return helper

def with_duplicate(n, chars):
    def helper(string):
        if string.count(chars) < 2:
            return False
        return generic_test(n)(string)
    return helper

def remove(string, n):
    for c in NUMBERS[n]:
        string = string.replace(c, '', 1)
    return string

def init():
    for i in (0, 1, 2, 4, 5, 6, 8):
        put(generic_test(i), i)
    put(with_duplicate(3, 'E'), 3)
    put(with_duplicate(7, 'E'), 7)
    put(with_duplicate(9, 'N'), 9)

def main():
    init()
    n = int(input())
    start = list(range(10))
    for i in range(n):
        result = list(map(str, sorted(find_num(input(), start, ()))))
        print('Case #{}: {}'.format(str(i+1), ''.join(result)))

main()

