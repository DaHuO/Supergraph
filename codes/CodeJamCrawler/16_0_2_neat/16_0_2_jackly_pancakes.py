def get_flip_count(stack_of_pancakes):
    last = stack_of_pancakes[0]
    counter = 0
    for pancake in stack_of_pancakes:
        if pancake != last:
            last = pancake
            counter += 1
    if stack_of_pancakes[-1] == '-':
        counter += 1
    return counter

cases_number = int(input())
for case in range(1, cases_number + 1):
    pancakes = input()
    print('Case #' + str(case) + ":", get_flip_count(pancakes))

