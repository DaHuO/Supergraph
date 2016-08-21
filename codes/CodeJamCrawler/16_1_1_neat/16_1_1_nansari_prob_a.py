def funky_sort(s):
    temp = [s[0]]
    for character in s[1:]:
        if character >= temp[0]:
            temp = [character] + temp
        else:
            temp.append(character)
    return ''.join(temp)

for index, case in enumerate(xrange(int(raw_input()))):
    s = raw_input()
    print("Case #%d: %s" % (index + 1, funky_sort(s)))
