
DIGITS = {0: "ZERO",
          1: "ONE",
          2: "TWO",
          3: "THREE",
          4: "FOUR",
          5: "FIVE",
          6: "SIX",
          7: "SEVEN",
          8: "EIGHT",
          9:"NINE"}

def digits(s):
    stack = [(s, [])]
    while stack:
        cur, soln = stack.pop()

        for num, digit in DIGITS.items():
            ret = can_find(cur, digit)
            if ret is not None:
                if ret == "":
                    return "".join(map(str, sorted(soln + [num])))
                else:
                    new_node = (ret, soln + [num])
                    stack.append(new_node)
    raise IndexError("we shouldn't get here if a soln exists")



def can_find(s, substr):
    """Returns the cut substring if we can find it, otherwise None."""
    tmp = s
    for char in substr:
        idx = tmp.find(char)
        if idx > -1:
            tmp = tmp[:idx] + tmp[idx + 1:]
        else:
            return None
    return tmp


if __name__ == "__main__":
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        s = raw_input()
        print "Case #{}: {}".format(i, digits(s))
        # check out .format's specification for more formatting options
