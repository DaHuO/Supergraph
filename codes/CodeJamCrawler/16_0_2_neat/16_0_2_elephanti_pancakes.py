__author__ = 'avital'


def flip(pancakes_to_flip):
    for index, pancake in enumerate(pancakes_to_flip):
        if pancake == "+":
            pancakes_to_flip[index] = '-'
        else:
            pancakes_to_flip[index] = '+'

    pancakes_to_flip.reverse()
    return pancakes_to_flip



def flip_pancakes(pancake_stack):
    i = 0
    for index, pancake in enumerate(pancake_stack):
        print pancake_stack
        while pancake_stack[index] == '-':
            j = -1
            while True:
                if pancake_stack[j] == '+':
                    pancake_stack[j] = '-'
                    j -= 1
                else:
                    break
            if j != -1:
                print pancake_stack
                i += 1
            good_pancakes = pancake_stack[:index]
            pancakes_to_flip = pancake_stack[index:]
            flipped_pancakes = flip(pancakes_to_flip)
            good_pancakes.extend(flipped_pancakes)
            pancake_stack = good_pancakes
            i += 1

    print pancake_stack
    return i

def main():

    input_file = open('pancakes_large.in', 'r')
    input = input_file.readlines()

    output = open('pancakes_large_result.txt', 'w')

    cases = input.pop(0)

    for case in range(0, int(cases)):
        pancake_stack = list(input[int(case)])
        try:
            pancake_stack.remove('\n')
        except:
            pass
        pancake_stack.reverse()

        result = flip_pancakes(pancake_stack)

        if case == int(cases)-1:
            output.write('Case #{case}: {result}'.format(case=case+1,
                                                           result=result)
            )

        else:
            output.write('Case #{case}: {result}\n'.format(case=case+1,
                                                           result=result)
            )

    input_file.close()
    output.close()

if __name__ == "__main__":
    main()