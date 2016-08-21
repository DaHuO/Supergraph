o = open("C:\Users\ANTON\Downloads\B-large.in")
w = open("C:\Users\ANTON\PycharmProjects\CodeJam\Round1A\RankAndFile\Large-Out.txt", 'w')

input_lines = [i.strip('\n') for i in o]

cases = input_lines.pop(0)

for index in xrange(int(cases)):
    N = int(input_lines.pop(0))
    frame = []
    lst = [[int(j) for j in input_lines.pop(0).split(' ')] for i in xrange(2 * N - 1)]

    for i in lst:
        for j in i:
            frame.append(j)
    solution = []
    for k in set(frame):
        count = 0
        for h in frame:
            if k == h:
                count += 1

        if count % 2 == 1:
            solution.append(k)

    solution = sorted(solution)
    solution = [str(i) for i in solution]

    w.write("Case #" + str(index + 1) + ": " + ' '.join(solution) + '\n')
