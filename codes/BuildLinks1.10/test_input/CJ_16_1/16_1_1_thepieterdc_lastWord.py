def lastWord(inpt):

    result = list()
    for letter in inpt:
        if len(result) == 0:
            result.append(ord(letter))
        elif len(result) == 1:
            c = ord(letter)
            if c > result[0]:
                result.insert(0, c)
            else:
                result.append(c)
        else:
            c = ord(letter)
            if c >= result[0]:
                result.insert(0, c)
            else:
                result.append(c)

    return "".join([chr(i) for i in result])

t = int(input())
for tI in range(0, t):
    n = str(input())
    print("Case  #{}: {}".format(tI + 1, lastWord(n)))