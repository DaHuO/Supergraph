

letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

with open('a_large.in') as f:
    with open('o1', 'w+') as fOut:
        cases = f.readline()
        print cases
        for case in range(int(cases)):
            str = f.readline().replace('\n','')
            initStr = ''
            for char in list(str):
                if len(initStr) == 0:
                    initStr = char
                elif letters.index(char) < letters.index(list(initStr)[0]):
                    initStr += char
                else:
                    tmp = list(initStr)
                    tmp.insert(0, char)
                    initStr = ''.join(tmp)
            fOut.write('Case #{0}: {1}\n'.format(case + 1, initStr))
