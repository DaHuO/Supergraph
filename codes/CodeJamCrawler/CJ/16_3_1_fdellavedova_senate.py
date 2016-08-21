import string

def is_balanced(parlamient, members):
    if members == 0:
        return True
    for n_members in parlamient.values():
        if float(n_members) / members > 0.5:
            return False
    return True

def evacuate(parlamient, tot_members):
    evacuating = []

    while tot_members > 0:
        for pair in get_pair(parlamient):
            if is_balanced(parlamient, tot_members - len(pair)):
                tot_members -= len(pair)
                evacuating.append(''.join(pair))
                break

    return evacuating


def get_pair(parlamient):
    for a in [i for i in parlamient if parlamient[i] > 0]:
        parlamient[a] -= 1
        for b in [i for i in parlamient if parlamient[i] > 0]:
            parlamient[b] -= 1
            yield a, b
            parlamient[b] += 1
        parlamient[a] += 1

    for a in [i for i in parlamient if parlamient[i] > 0]:
        parlamient[a] -= 1
        yield a,
        parlamient[a] += 1


def main(parlamient, tot_members):
    return evacuate(parlamient, tot_members)


if __name__ == '__main__':
    from sys import stdin

    is_header = False
    case_num = 1
    for line in stdin.read().splitlines():
        if not is_header:
            is_header = True
            continue
        elif len(line) == 1:
            n_parties = line
            parlamient, tot_members = {}, 0
        else:
            for party, n_members in zip(string.ascii_uppercase, line.split(' ')):
                parlamient[party] = int(n_members)
                tot_members += int(n_members)
            result = ['Case #{}:'.format(case_num)] + main(parlamient, tot_members)
            case_num += 1
            print(' '.join(result))


