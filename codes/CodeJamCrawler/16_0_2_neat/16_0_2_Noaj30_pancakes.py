# Google Code Jam Qualification Round 2016
# Problem B. Revenge of the Pancakes

def flips(string):
    moves = 0
    while '-' in string:
        while string[-1] == '+':
            string = string[:-1]
        if string[0] == '+':
            new = []
            k = 0
            for i in string:
                if i == '+':
                    k += 1
                else:
                    break
            if k != 0:
                string = k*['-'] + string[k:]
                moves += 1
        new = []
        for i in string[::-1]:
            if i == '+':
                new += ['-']
            else:
                new += ['+']
        string = new
        moves += 1
    return moves

def pancakes():
    f = open('commands.txt', 'r')
    g = open('pancakes.txt', 'w')
    line = 0
    for i in f:
        if line == 0:
            T = int(i)
            line = 1
        else:
            string = []
            for j in i:
                if j not in [' ', '\n']:
                    string += [j]
            g.write('Case #' + str(line) + ': ')
            g.write(str(flips(string)))
            g.write((T != line)*'\n')
            line += 1
    f.close()
    g.close()
