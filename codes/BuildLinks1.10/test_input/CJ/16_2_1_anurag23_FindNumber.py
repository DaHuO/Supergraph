words = {}
words[0] = ['Z', 'E', 'R', 'O']
words[1] = ['O','N','E']
words[2] = ['T','W','O']
words[3] = ['T','H','R','E','E']
words[4] = ['F','O','U','R']
words[5] = ['F','I','V','E']
words[6] = ['S','I','X']
words[7] = ['S','E','V','E','N']
words[8] = ['E','I','G','H','T']
words[9] = ['N','I','N','E']

mapping = [''] * 10
mapping[0] = 'Z'
mapping[6] = 'X'
mapping[4] = 'U'
mapping[2] = 'W'
mapping[8] = 'G'
mapping[5] = 'F'
mapping[7] = 'V'
mapping[3] = 'H'
mapping[9] = 'I'
mapping[1] = 'N'



def findNum(words, mapping , s):
    order = [0, 6, 4, 2, 8, 5, 7, 3, 9, 1]
    dix = {}
    p = [0] * 10

    for c in s:
        if c not in dix:
            dix[c] = 0
        dix[c] = dix[c] + 1
    for index in order:
        while mapping[index] in dix:
            p[index] += 1
            for val in words[index]:
                dix[val] -= 1
                if dix[val] == 0:
                    dix.__delitem__(val)
    t = 0
    s = ""
    for index in range(0,10):
        t = p[index]
        while t > 0:
            s += str(index)
            t -= 1
    return s

t = int(input())
for i in range(1, t+1):
    print("Case #"+str(i)+": " + findNum(words, mapping, input()))