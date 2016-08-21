file = 'A-large.in'

with open(file) as f:
    inputs = f.readlines()

total_cases = int(inputs[0])
results = []
for i in range(0, total_cases):
    test_case = int(inputs[i+1])
    print 'Evaluating: ' + str(test_case)
    digits = [None] * 10

    if test_case == 0:
        results.append('INSOMNIA')
        continue

    idx = 1
    while True:
        aux = test_case * idx
        print aux
        idx += 1

        for j in range(0, 10):
            if str(j) in str(aux):
                digits[j] = 1

        if None not in digits:
            results.append(str(aux))
            break



f = open(file + '.out','w')
for i in range(0, len(results)):
    output = 'Case #' + str(i + 1) + ': ' + results[i]
    f.write(output + '\n')
    print output
f.close()