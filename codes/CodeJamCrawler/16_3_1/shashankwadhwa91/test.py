from math import ceil

test_cases = int(raw_input().strip())
inputs = []
outputs = []

for t in xrange(test_cases):
    n = int(raw_input().strip())
    senators_count = map(int, raw_input().strip().split())
    inputs.append(senators_count)

for senators_count in inputs:
    d = {}
    removed = []
    total_count = 0
    for ctr,elem in enumerate(senators_count):
        d[chr(65+ctr)] = elem
        total_count += elem

    cond = False
    while not cond:
        to_be_removed = []
        if all(value == 1 for value in d.values()) and len(d) == 3:
            key = d.keys()[0]
            to_be_removed.append(key)
            d[key] -= 1
            total_count -= 1
        else:
            threshold_value = max(d.values())
            for key,value in d.iteritems():
                if value == threshold_value:
                    to_be_removed.append(key)
                    d[key] -= 1
                    total_count -= 1
                    if len(to_be_removed) == 2:
                        break

        removed.append(''.join(to_be_removed))
        cond = all(value == 0 for value in d.values())

    outputs.append(' '.join(removed))

text_file = open('/Users/mac/Work/google_code_jam/output.txt', 'w')
for counter,o in enumerate(outputs):
    output_str = 'Case #%s: %s' % (counter+1, o)
    text_file.write(output_str)
    text_file.write('\n')
text_file.close()