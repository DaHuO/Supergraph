import fileinput
from itertools import count

lines = list(fileinput.input())

for case, line in enumerate(lines[1:], 1):
    n = int(line.strip())
    seen = set()
    call = n
    for i in count(2):
        if call == 0:
            call = 'INSOMNIA'
            break

        seen |= set(str(call))

        if len(seen) == 10:
            break
        call = i * n
    print('Case #{}: {}'.format(case, call))
