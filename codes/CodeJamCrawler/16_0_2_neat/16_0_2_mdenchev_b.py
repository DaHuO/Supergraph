fin = open('b.in', 'r')
fout = open('b.out', 'w')

fin.readline()
cases = fin.readlines()

for i, case in enumerate(cases):
    start_with_happy = case[0] == '+'
    boundaries = 0
    for idx, pancake in enumerate(case.strip()):
        if idx == 0: continue
        if case[idx-1] != case[idx]:
            boundaries += 1
    print(boundaries)
    if boundaries % 2 == 0 and not start_with_happy:
        boundaries += 1
    elif boundaries % 2 == 1 and start_with_happy:
        boundaries += 1
    fout.write('Case #' + str(i+1) + ': ' + str(boundaries) +'\n')
