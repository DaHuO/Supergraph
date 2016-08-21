

with open('A-large.in') as f:
    f.readline()  # ignored
    test_cases = map(lambda x: x[:-1], f.readlines())

outputs = []
i = 0
for case in test_cases:
    i += 1
    case = list(case)
    output = case.pop(0)
    while case:
        letter = case.pop(0)
        if letter >= output[0]:
            output = letter + output
        else:
            output = output + letter

    outputs.append('Case #' + str(i) + ': ' + output + '\n')

with open('round1_a.out', mode='r+') as f:
    f.writelines(outputs)
