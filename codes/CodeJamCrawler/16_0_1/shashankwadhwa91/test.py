test_cases = int(raw_input().strip())
inputs = []
outputs = []

for t in xrange(test_cases):
    n = int(raw_input().strip())
    inputs.append(n)

total_digits = range(0, 10)
for n in inputs:
    if n == 0:
        outputs.append('INSOMNIA')
        continue

    counter = 1
    seen_all_digits = False
    digits_seen = []
    while seen_all_digits == False:
        number = counter * n
        digits = map(int, list(str(number)))
        digits_seen += digits
        digits_seen = list(set(digits_seen))
        seen_all_digits = (digits_seen == total_digits)
        counter += 1
    outputs.append(number)

text_file = open('/Users/mac/Downloads/output.txt', 'w')
for counter,o in enumerate(outputs):
    output_str = 'Case #%s: %s' % (counter+1, o)
    text_file.write(output_str)
    text_file.write('\n')
text_file.close()