def all_happy(pancakes):
    return all(c == '+' for c in pancakes)

def flip(pancakes):
    return ''.join('+' if c == '-' else '-' for c in pancakes)

def flip_top(pancakes, n):
    return flip(pancakes[:n]) + pancakes[n:]

def find_unhappy(pancakes):
    for i, c in list(enumerate(pancakes))[::-1]:
        if c == '-':
            return i+1

def num_flips(pancakes):
    for flips in range(9999999999):
        if all_happy(pancakes):
            return flips

        bottom_unhappy = find_unhappy(pancakes)
        pancakes = flip_top(pancakes, bottom_unhappy)

print(num_flips('+') == 0)
print(num_flips('-') == 1)
print(num_flips('-+') == 1)
print(num_flips('+-') == 2)
print(num_flips('+++') == 0)
print(num_flips('--+-') == 3)

with open('B-large.in.txt') as f, open('B-large.out.txt', 'w') as g:
    n = int(f.readline())
    for case_num in range(1, n+1):
        inp = f.readline().strip()
        ans = num_flips(inp)
        g.write("Case #{}: {}\n".format(case_num, ans))
