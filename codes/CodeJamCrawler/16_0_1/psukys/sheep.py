import sys

N_cap = 1000000

def read_input(file):
    with open(file) as f:
        inputs = f.readlines()

    inputs = [int(i) for i in inputs]
    return inputs[1:]

def split_numbers(number):
    '''
    Splits numbers by single digit
    '''
    splitted = []
    while number:
        splitted.append(number % 10)
        number = number / 10

    return splitted

def count_sheep(N):
    digits = []
    n = N  #  Used as substitute for constant incrementation by N
    cap = N_cap
    while cap > 0 and len(set(digits)) < 10:
        #print(n, set(digits))
        digits.extend(split_numbers(n))
        n = n + N
        cap = cap - 1

    if len(digits) < 10:
        return 'INSOMNIA'
    else:
        # Just because last reiteration adds additional value
        return n - N



if __name__ == '__main__':
    inputs = read_input(sys.argv[1])
    counter = 1
    output = []
    for i in inputs:
        output.append("Case #{0}: {1}".format(counter, count_sheep(i)))
        counter = counter + 1

    with open(sys.argv[1] + 'output', 'w') as f:
        f.write('\n'.join(output))