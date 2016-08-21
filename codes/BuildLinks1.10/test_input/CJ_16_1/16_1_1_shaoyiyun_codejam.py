f = open("A-large.in", "rb")
lines = []

for line in f:
    lines.append(line)

for i in range(1, len(lines)):
    s = lines[i]
    word = [s[0]]

    for j in range(1, len(s)):
        if ord(s[j]) >= ord(word[0]):
            word.insert(0, s[j])
        else:
            word.append(s[j])

    win = "".join(word)  
    print "Case #" + str(i) + ": " + win,
