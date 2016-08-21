def get_answer():
    line = input()
    last = None
    count = 0
    for i in range(1, len(line)):
        if line[i-1] != line[i]:
            count += 1
    if line[-1] == '-':
        count += 1

    return count

n = int(input())
for r in range(1, n+1):
    print('Case #{}: {}'.format(r, get_answer()))
