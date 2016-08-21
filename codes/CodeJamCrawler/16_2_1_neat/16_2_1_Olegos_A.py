def decode(s):
    if s[-1] == '\n':
        s = s[:-1]
    numbers = []
    i = 0
    for l in letters:
        while str.find(s, l) > -1:
            for letter in words[i]:
                pos = str.find(s, letter)
                s = s[:pos] + s[pos + 1:]
            numbers.append(nums[i])
        i += 1
    numbers.sort()
    result = ''
    for n in numbers:
        result += str(n)
    return result


input_file = open('in.txt', 'r')
lines = []
for line in input_file:
    lines.append(line)

nums = [0, 2, 4, 8, 6, 3, 1, 5, 7, 9]
letters = ['Z', 'W', 'U', 'G', 'X', 'H', 'O', 'F', 'S', 'I']
words = ['ZERO', 'TWO', 'FOUR', 'EIGHT', 'SIX', 'THREE', 'ONE', 'FIVE', 'SEVEN', 'NINE']

output_file = open('out.txt', 'w')
case = 1
for n in lines[1:]:
    output_file.write('Case #{}: {}\n'.format(case, decode(n)))
    case += 1
