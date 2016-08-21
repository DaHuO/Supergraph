

with open('B-large.in') as f:
    n = int(f.readline())  # ignored
    test_cases = []
    for i in range(n):
        test_cases.append(list(map(int, ' '.join([f.readline()[:-1] for i in range(int(f.readline()[:-1])*2 - 1)]).split())))

outputs = []
i = 0
for case in test_cases:
    i += 1
    output = [case.pop(0), ]
    while case:
        number = case.pop(0)
        if number in output:
            output.remove(number)
        else:
            output.append(number)
    output = ' '.join(list(map(str, sorted(output))))

    outputs.append('Case #' + str(i) + ': ' + output + '\n')

with open('round1_B.out', mode='r+') as f:
    f.writelines(outputs)
