with open('A-large.in') as f:
    for i, s in enumerate(f.readlines()[1:], start=1):
        word = [s[0]]
        for x in list(s.strip()[1:]):
            if x < word[0]:
                word.append(x)
            else:
                word.insert(0, x)

        print("Case #{}: {}".format(str(i), ''.join(word)))
