
max_tries = 500

def sheep(inst):
    initial = int(inst)
    current_nbr = initial

    solutions = [False for i in range(0,10)]
    tries = 0

    while tries < max_tries:
        found_number = False
        units = [int(s) for s in str(current_nbr)]

        for unit in units:
            if solutions[unit] is False:
                solutions[unit] = True
                found_number = True
        if not found_number:
            tries += 1
        else:
            tries = 0

        if(sum(solutions) == 10):
            break
        else:
            current_nbr += initial
    if tries == max_tries:
        return -1 #INSOMNIA
    else:
        return current_nbr

output = {}
input = None

with open('input.txt', 'rU') as input:
    input = input.readlines()

with open('output.txt', 'w') as output:
    case = 1
    for instance in input[1:]:
        result = sheep(instance)
        output.write("Case #{}: {} \n".format(
            case,
            'INSOMNIA' if result == -1 else result
        ))
        case += 1
