#!/usr/bin/python3

def get_lines(filename):
    lines = []
    try:
        with open(filename, 'r') as f:
            while True:
                line = f.readline().rstrip('\n')
                if line == '':
                    break
                lines.append(line)
    except EOFError:
        pass
    return lines

def get_line(f):
    return f.readline().rstrip('\n')

def solve(line):
    c = {}
    res = []
    a = [('Z', 0), ('W', 2), ('U', 4), ('X', 6), ('S', 7), ('V', 5), ('G', 8), ('O', 1), ('H', 3), ('I', 9)]
    numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    for letter, number in a:
        #print(line)
        c[letter] = line.count(letter)

    #print(c)
    for letter, number in a:
        #print(c[letter])
        temp = c[letter]
        res.append(str(number) * temp)
        for character in numbers[number]:
            #print(character)
            if character in c.keys():
                c[character] -= temp
        #print(c)
    #print(res)
    return ''.join(sorted(res))
    return ''.join(l)


if __name__ == '__main__':
    filename = 'input/A-test.in'
    filename = 'input/A-small-attempt1.in'
    filename = 'input/A-large.in'
    lines = (get_lines(filename))
    cases = int(lines[0])
    with open("output/outputA.txt", "w") as f:
        for case in range(0, cases):
            out = ("Case #%d: " % (case+1)) + solve(lines[case+1])
            print(out)
            f.write(out + '\n')


