fin = open('1a.in', 'r')
fout = open('1a.out', 'w')

no_cases = fin.readline()

cases = map(str.strip, fin.readlines())

for i, case in enumerate(cases):
    result = case[0]
    for ch in case[1:]:
        if ch >= result[0]:
            result = ch + result
        else:
            result = result + ch
    fout.write('Case #' + str(i+1) + ': ' + result + '\n')
