# left = top
# right = bottom

def calculate(s):
    """
    >>> calculate("-")
    1
    >>> calculate("-+")
    1
    >>> calculate("+-")
    2
    >>> calculate("+++")
    0
    >>> calculate("--+-")
    3
    """
    s = str(s)
    i = 0
    while "-" in s:
        laatstemin = s.rfind("-")
        substr = list(s[0:laatstemin + 1])
        rest = s[laatstemin + 1:]
        for c in range(0, len(substr)):
            substr[c] = "-" if substr[c] == "+" else "+"
        s = "".join(substr) + rest
        i += 1
    return i


t = int(input())
for tI in range(0, t):
    n = str(input())
    print("Case  #{}: {}".format(tI + 1, calculate(n)))
