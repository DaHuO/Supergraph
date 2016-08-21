

def do_a_flip(cake_stack, index):
    for i in range(0, index):
        if cake_stack[i] == '+':
            cake_stack[i] = '-'
        else:
            cake_stack[i] = '+'

def count_flips(cake_stack):
    num_flips = 0
    current = cake_stack[0]
    for i in range(1, len(cake_stack)):
        if cake_stack[i] != current:
            do_a_flip(cake_stack, i)
            num_flips += 1
            current = cake_stack[0]
    if current == '-':
        num_flips += 1
    return num_flips



if __name__ == '__main__':
    num_examples = int(input())
    for i in range(0, num_examples):
        cake_stack = list(input().strip())
        solution = count_flips(cake_stack)
        print("Case #%s: %s" % (i+1, solution))
