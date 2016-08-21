from collections import Counter

digits = [Counter(x) for x in ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]]

def get_digits(s):
    def impl(chars):
        if not chars:
            return []
        for i, digit in enumerate(digits):
            if digit - chars:
                continue
            ret = impl(chars - digit)
            if ret is not None:
                return [i] + ret
        return None
    number = impl(Counter(s))
    number.sort()
    return ''.join(str(n) for n in number)


for case in range(int(input())):
    print("Case #{}: {}".format(case+1, get_digits(input())))
