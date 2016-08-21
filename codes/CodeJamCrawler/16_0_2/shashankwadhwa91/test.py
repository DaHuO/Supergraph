test_cases = int(raw_input().strip())
inputs = []
outputs = []

def reverse_negate(s):
    reversed_string = s[::-1]
    new_str = ''
    for char in reversed_string:
        if char == '+':
            new_str += '-'
        elif char == '-':
            new_str += '+'
    return new_str

for t in xrange(test_cases):
    s = raw_input().strip()
    inputs.append(s)

for s in inputs:
    if s == len(s) * s[0]:
        if s[0] == '+':
            outputs.append(0)
        else:
            outputs.append(1)
        continue

    last_index = s.rfind('-')
    s = s[:last_index+1]
    all_same = False
    counter = 0
    while all_same == False:
        if s[:1] == '+':
            for ctr,char in enumerate(s):
                if char == '-':
                    break
            s = s.replace('+', '-', ctr)
            counter += 1

        s = reverse_negate(s)
        last_index = s.rfind('-')
        if last_index != -1:
            s = s[:last_index+1]
        counter += 1
        all_same = ((s == len(s) * s[0]) and s[0] == '+')
    outputs.append(counter)

text_file = open('/Users/mac/Downloads/output.txt', 'w')
for counter,o in enumerate(outputs):
    output_str = 'Case #%s: %s' % (counter+1, o)
    text_file.write(output_str)
    text_file.write('\n')
text_file.close()

