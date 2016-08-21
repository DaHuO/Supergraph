file = 'B-large.in'

with open(file) as f:
    inputs = f.readlines()

total_cases = int(inputs[0])
results = []
for i in range(0, total_cases):
    test_case = inputs[i+1].strip()
    print 'Evaluating: ' + test_case
    
    current = test_case[0]
    changes = 0
    for character in test_case:
        if character != current:
            current = character
            changes += 1

    if test_case[len(test_case) - 1] == '-':
        changes += 1
    results.append(str(changes))

f = open(file + '.out','w')
for i in range(0, len(results)):
    output = 'Case #' + str(i + 1) + ': ' + results[i]
    f.write(output + '\n')
    print output
f.close()