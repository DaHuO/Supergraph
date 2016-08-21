import collections

# Support choices with identical elements
def get_permutation(n, choices):
    if n > len(choices):
        return []
    all_permutation = []
    choices_count = collections.Counter()
    for choice in choices:
        choices_count[choice] += 1
    def get_perm_with_choices_count( cur_state, result, n, choices_count):
        if len(cur_state) >= n:
            result.append(cur_state[:])
            return True
        elif len(choices_count) == 0:
            return True
        choices = choices_count.keys()
        for choice in choices:
            cur_state.append(choice)
            choice_count = choices_count[choice]
            if choice_count <= 0:
                del choices_count[choice]
                continue
            elif choice_count <= 1:
                del choices_count[choice]
            else:
                choices_count[choice] -= 1
            get_perm_with_choices_count(cur_state, result, n, choices_count)
            choices_count[choice] += 1
            cur_state.pop()
        return True
    get_perm_with_choices_count([], all_permutation, n, choices_count)
    return all_permutation

# Get permutation with state checker. If state checker(cur_state) return false, we don't need to go deeper
# and can return directly
def get_permutation2(n, choices, state_checker=lambda x:True):
    if n > len(choices):
        return []
    all_permutation = []
    choices_count = collections.Counter()
    for choice in choices:
        choices_count[choice] += 1
    def get_perm_with_choices_count( cur_state, result, n, choices_count):
        if not state_checker(cur_state):
            return True
        if len(cur_state) >= n:
            result.append(cur_state[:])
            return True
        elif len(choices_count) == 0:
            return True
        choices = choices_count.keys()
        for choice in choices:
            cur_state.append(choice)
            choice_count = choices_count[choice]
            if choice_count <= 0:
                del choices_count[choice]
                continue
            elif choice_count <= 1:
                del choices_count[choice]
            else:
                choices_count[choice] -= 1
            get_perm_with_choices_count(cur_state, result, n, choices_count)
            choices_count[choice] += 1
            cur_state.pop()
        return True
    get_perm_with_choices_count([], all_permutation, n, choices_count)
    return all_permutation


def get_combination(n, choices):
    if n > len(choices):
        return []
    all_combination = []
    choices_count = collections.Counter()
    for choice in choices:
        choices_count[choice] += 1
    choices_count = choices_count.items()
    choices_count.sort()
    def get_comb_with_choices_count( cur_state, result, n, choices_count):
        if len(cur_state) >= n:
            result.append(cur_state[:])
            return True
        elif len(choices_count) == 0:
            return True
        for i, choice_count in enumerate(choices_count):
            choice, count = choice_count
            next_start_index = i
            if count <= 0:
                continue
            elif count <= 1:
                next_start_index = i+1
            cur_state.append(choice)
            choices_count[i] = (choice, count-1)
            get_comb_with_choices_count(cur_state, result, n, choices_count[next_start_index:])
            choices_count[i] = (choice, count)
            cur_state.pop()
        return True
    get_comb_with_choices_count([], all_combination, n, choices_count)
    return all_combination


if __name__ == '__main__':
    print(get_permutation(3,[1,2,2,2]))
    print(get_combination(3,[1,2,2,2]))

