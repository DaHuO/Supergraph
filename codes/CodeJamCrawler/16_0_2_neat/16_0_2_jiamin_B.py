# returns index of beginning of last pancake '-' streak
# -1 if all +
def get_unhappy_ind(pancakes):
    i = len(pancakes) - 1
    if i == 0:
        return -1 if pancakes[0] == '+' else 0
    # first get rid of any bottom + streak
    while pancakes[i] == '+':
        if i == 0:
            return -1
        i -= 1
    while pancakes[i] == '-':
        if i == 0:
            return i
        i -= 1
    return i + 1

def flip(pancakes):
    new_pancakes = ''
    for i in range(len(pancakes)):
        new_pancakes += '-' if pancakes[i] == '+' else '+'
    return new_pancakes

def count_flips(pancakes):
    if pancakes == '-':
        return 1
    elif pancakes == '+-':
        return 2
    elif pancakes == '-+':
        return 1
    ind = get_unhappy_ind(pancakes)
    if ind == -1: # all '+'
        return 0
    elif ind == 0: # '-' streak to top
        return 1
    return 1 + count_flips(flip(pancakes[:ind]))

f = open('B.in', 'r')
f_ans = open('B.out', 'w')

num_cases = int(f.readline())

for i in range(num_cases):
    pancakes = f.readline()[:-1]
    ans = str(count_flips(pancakes))
    f_ans.write("Case #" + str(i+1) + ": " + ans + '\n')
