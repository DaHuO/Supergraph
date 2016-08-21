
def get_soln(pancakes):
    # Convert to booleans
    up_pancakes = ['+' == cake for cake in pancakes]
    if all(up_pancakes):
        return 0
    else:
        top_is_up = up_pancakes[0]
        groups = 0
        down_group = False
        for cake in up_pancakes:
            if not cake:
                down_group = True
            if cake and down_group:
                groups += 1
                down_group = False

        if down_group:
            groups += 1

        return groups * 2 - 1 + (1 if top_is_up else 0)

num_problems = int(input())

for i in range(num_problems):
    pancakes = list(raw_input())
    soln = get_soln(pancakes)
    print('Case #{}: {}'.format(i + 1, soln))