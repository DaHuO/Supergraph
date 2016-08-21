def findNum(inputstr):
    """
    >>> findNum("OZONETOWER")
    [0, 1, 2]
    >>> findNum("WEIGHFOXTOURIST")
    [2, 4, 6, 8]
    >>> findNum("OURNEONFOE")
    [1, 1, 4]
    >>> findNum("ETHER")
    [3]
    >>> findNum("SEITENVSWXO")
    [2, 6, 7]
    """
    result = []

    while len(inputstr) > 0:
        if "Z" in inputstr:
            result.append(0)
            inputstr = inputstr.replace("Z", "", 1)
            inputstr = inputstr.replace("E", "", 1)
            inputstr = inputstr.replace("R", "", 1)
            inputstr = inputstr.replace("O", "", 1)
            continue

        if "W" in inputstr:
            result.append(2)
            inputstr = inputstr.replace("T", "", 1)
            inputstr = inputstr.replace("W", "", 1)
            inputstr = inputstr.replace("O", "", 1)
            continue

        if "U" in inputstr:
            result.append(4)
            inputstr = inputstr.replace("F", "", 1)
            inputstr = inputstr.replace("O", "", 1)
            inputstr = inputstr.replace("U", "", 1)
            inputstr = inputstr.replace("R", "", 1)
            continue

        if "X" in inputstr:
            result.append(6)
            inputstr = inputstr.replace("S", "", 1)
            inputstr = inputstr.replace("I", "", 1)
            inputstr = inputstr.replace("X", "", 1)
            continue

        if "G" in inputstr:
            result.append(8)
            inputstr = inputstr.replace("E", "", 1)
            inputstr = inputstr.replace("I", "", 1)
            inputstr = inputstr.replace("G", "", 1)
            inputstr = inputstr.replace("H", "", 1)
            inputstr = inputstr.replace("T", "", 1)
            continue

        if "H" in inputstr:
            result.append(3)
            inputstr = inputstr.replace("T", "", 1)
            inputstr = inputstr.replace("H", "", 1)
            inputstr = inputstr.replace("R", "", 1)
            inputstr = inputstr.replace("E", "", 1)
            inputstr = inputstr.replace("E", "", 1)
            continue

        if "O" in inputstr:
            result.append(1)
            inputstr = inputstr.replace("O", "", 1)
            inputstr = inputstr.replace("N", "", 1)
            inputstr = inputstr.replace("E", "", 1)
            continue

        if "F" in inputstr:
            result.append(5)
            inputstr = inputstr.replace("F", "", 1)
            inputstr = inputstr.replace("I", "", 1)
            inputstr = inputstr.replace("V", "", 1)
            inputstr = inputstr.replace("E", "", 1)
            continue

        if "S" in inputstr:
            result.append(7)
            inputstr = inputstr.replace("S", "", 1)
            inputstr = inputstr.replace("E", "", 1)
            inputstr = inputstr.replace("V", "", 1)
            inputstr = inputstr.replace("E", "", 1)
            inputstr = inputstr.replace("N", "", 1)
            continue

        if "N" in inputstr:
            result.append(9)
            inputstr = inputstr.replace("N", "", 1)
            inputstr = inputstr.replace("I", "", 1)
            inputstr = inputstr.replace("N", "", 1)
            inputstr = inputstr.replace("E", "", 1)
            continue

    result.sort()
    return result


t = int(input())
for tI in range(0, t):
    n = str(input())
    print("Case #{}: {}".format(tI + 1, "".join(str(x) for x in findNum(n))))
