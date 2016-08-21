def flip(string, i):
    """
        -- string will be partially ordered e.g.
            ---+--+- or +++-++-+
        -- i is the break point index
        -- e.g. i is 3 in ---+--+-
    """
    first = string[0:i]
    rest = string[i:]
    mult = len(first)
    return mult*string[i] + rest
def flipper(file):
    L = [line.strip() for line in open(file, "r")]
    pancake_stacks = L[1: int(L[0])+1]
    rstring = ""
    for i in range(len(pancake_stacks)):
        # some pancakes' string e.g. "---+-+-+"
        flips = 0
        pancakes = pancake_stacks[i]
        case = i+1
        happy = "+"*len(pancakes)
        sad = "-"*len(pancakes)
        while pancakes != happy:
            if pancakes == sad:
                pancakes = happy
                flips +=1
            else:
                start = pancakes[0]
                point = None
                if start == "-":
                    point = pancakes.index("+")
                else:
                    point = pancakes. index("-")
                pancakes = flip(pancakes, point)
                flips += 1
        rstring += "Case #{0}: {1}\n".format(case, flips)
    return rstring

if __name__ == "__main__":
    file = "B-large.in"
    print(flipper(file))

