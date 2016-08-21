def answer(pancakes, desired='+'):
    if len(pancakes) == 0:
        return 0
    bottom = pancakes[-1]
    i = len(pancakes) - 1
    while i >= 0:
        if bottom != pancakes[i]:
            break
        i -= 1
    if bottom == '+' and desired == '+':
        return answer(pancakes[:i+1], '+')
    if bottom == '-' and desired == '-':
        return answer(pancakes[:i + 1], '-') + 1
    if bottom == '-' and desired == '+':
        return answer(pancakes[:i + 1], '-') + 1
    if bottom == '+' and desired == '-':
        return answer(pancakes[:i + 1], '+') + 1

input_file = open('b-large.txt')
input_file.readline()
for input_num, pancakes in enumerate(input_file):
    pancakes = pancakes.strip()
    print "Case #{}: {}".format(input_num + 1, answer(pancakes))
