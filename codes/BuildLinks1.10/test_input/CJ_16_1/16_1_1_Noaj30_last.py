# Google Code Jam 2016 Round 1A
# Problem A. The Last Word

def game(word):
    s = word[0]
    for i in word[1:]:
        if ord(i) < ord(s[0]):
            s += i
        else:
            s = i + s
    return s

def last():
    f = open('commands.txt', 'r')
    g = open('last.txt', 'w')
    line = 0
    for i in f:
        if line == 0:
            T = int(i)
            line = 1
        else:
            g.write('Case #' + str(line) + ': ')
            g.write(game(i[:-1]))
            g.write((T != line)*'\n')
            line += 1
    f.close()
    g.close()
