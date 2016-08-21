

with open('A-large.in', 'r') as infile:
    count = 0
    N = []
    T = 0
    for line in infile:
        if count == 0:
            T = int(line)
        else:
            N.append(int(line))
        count += 1
with open ('output.txt', 'w+') as outfile:
    for idx, number in enumerate(N):
        complete = []
        iterations = 0
        multiply = 1
        insomnia = False
        while len(complete) < 10:
            if number == 0:
                insomnia = True
                break
            cur_num = number* multiply
            str_num = str(cur_num)
            for char in str_num:
                if char not in complete:
                    complete.append(char)
            iterations += 1
            multiply += 1
            if iterations == 10000:
                insomnia = True
                break
        if insomnia == True:
            outfile.write('Case #' + str(idx + 1) + ': INSOMNIA\n')
        else:
            outfile.write('Case #' + str(idx + 1) + ': ' + str(cur_num) + '\n')
