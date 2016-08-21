glob_dict = {}
def estimate(pc):
    print_num = 0
    if len(pc) != 0:
       if pc[0] == '-':
            print_num += 1
            pc = pc.lstrip('-')
    while True:
        pc = pc.lstrip('+')
        if len(pc) == 0:
            break
        print_num += 2
        pc = pc.lstrip('-')
    return print_num

def all_happy(pancakes):
    return sum((1 for char in pancakes if char == "+")) == len(pancakes)


def min_flips(pancakes):
    if all_happy(pancakes):
        return 0
    plus = False
    done = False
    if pancakes[0] == '+':
        plus = True
    new_pc = []
    for char in pancakes:
        if done:
            new_pc.append(char)
            continue
        if plus:
            if char == '+':
                new_pc.append('-')
            else:
                done = True
                new_pc.append('-')
        else:
            if char == '-':
                new_pc.append('+')
            else:
                done = True
                new_pc.append('+')
    return 1 + min_flips(''.join(new_pc))

def flip(pancakes , index):
    flip_me = pancakes[:index+1]
    remaining = pancakes[index+1:]
    flip_me = list(flip_me[::-1])
    for i in range(len(flip_me)):
        if flip_me[i] == '+':
          flip_me[i] = '-'
        else:
            flip_me[i] = '+'
    flip_me.extend(list(remaining))
    ret = ''.join(flip_me)
    return ret

def main():
    cases = int(raw_input())
    for i in range(1,cases+1):
        pancakes = raw_input()
        est = estimate(pancakes)
        brut = min_flips(pancakes)
        if brut != est:
            print (pancakes + "est : " + str(est) + " brut : " + str(brut))
        print("CASE #" + str(i) + ": " + str(est))

main()