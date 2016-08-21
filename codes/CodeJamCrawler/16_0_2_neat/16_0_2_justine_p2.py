def reverse(l):
    return ''.join(map(lambda x:'-' if x == '+' else '+', l[::-1]))

def get_flip_count():
    n_flip = 0
    pancake = input()

    while '-' in pancake:
        pancake = pancake[:pancake.rfind('-') + 1]
        if pancake[0] == '+':
            idx = pancake.find('-')
            pancake = reverse(pancake[:idx]) + pancake[idx:]
        else:
            pancake = reverse(pancake)
        n_flip += 1
    return n_flip

for case in range(int(input())):
    print ('Case #{}: {}'.format(case+1, get_flip_count()))
