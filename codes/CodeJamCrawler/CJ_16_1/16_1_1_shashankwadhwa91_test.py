test_cases = int(raw_input().strip())
inputs = []
outputs = []

for t in xrange(test_cases):
    s = raw_input().strip()
    inputs.append(s)

for s in inputs:
    new_str = ''
    for char in s:
        try:
            highest_ord = ord(new_str[0])
        except IndexError:
            highest_ord = 0
        if ord(char) >= highest_ord:
            new_str = char + new_str
        else:
            new_str = new_str + char
    outputs.append(new_str)

text_file = open('/Users/mac/Downloads/output.txt', 'w')
for counter,o in enumerate(outputs):
    output_str = 'Case #%s: %s' % (counter+1, o)
    text_file.write(output_str)
    text_file.write('\n')
text_file.close()