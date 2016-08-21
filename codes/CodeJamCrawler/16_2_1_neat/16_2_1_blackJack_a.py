c = int(raw_input())

order = [(0, 'Z', 'ZERO'),
         (2, 'W', 'TWO'),
         (6, 'X', 'SIX'),
         (8, 'G', 'EIGHT'),
         (4, 'U', 'FOUR'),
         (5, 'F', 'FIVE'),
         (7, 'V', 'SEVEN'),
         (3, 'H', 'THREE'),
         (9, 'I', 'NINE'),
         (1, 'O', 'ONE')]

for idx in range(c):
    string = str(raw_input())
    dic = {}
    count = [0]*10
    for char in string:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    for i, letter, digit in (order):
        freq = dic.get(letter, 0)
        if not freq:
            continue
        count[i] = freq
        for char in digit:
            dic[char] -= freq
    res = ''.join(sorted([str(i)*frq for i, frq in enumerate(count) if frq != 0]))
    print "Case #{0}: {1}".format(idx+1, res)
