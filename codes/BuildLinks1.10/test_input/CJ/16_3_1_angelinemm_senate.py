from math import floor

def is_majority(senate):
    total_senators = sum(senate.values())
    majority = floor(total_senators/2) + 1
    for nb_senators in senate.values():
        if nb_senators >= majority:
            return True
    return False

def evacuate(senate, evacuation):
    new_senate = senate.copy()
    party, other_party = evacuation
    new_senate[party] -= 1
    if other_party:
        new_senate[other_party] -= 1
    return new_senate

def possible_evacuations(senate):
    possible = []
    for party, nb_senators in senate.iteritems():
        if nb_senators == 0:
            continue
        # First possibility is to evacuate only one senator
        new_possible_senate = evacuate(senate, (party, ''))
        if not is_majority(new_possible_senate):
            possible.append((party, ''))
        # Second possibility is two of this party
        if nb_senators >= 2:
            new_possible_senate = evacuate(senate, (party, party))
            if not is_majority(new_possible_senate):
                possible.append((party, party))
        # Other possibility is this party plus all others
        for other_party, other_nb_senators in senate.iteritems():
            if other_party <= party:
                continue
            if other_nb_senators == 0:
                continue
            new_possible_senate = evacuate(senate, (party, other_party))
            if not is_majority(new_possible_senate):
                possible.append((party, other_party))
    return possible

def build_evacuation(senate):
    if sum(senate.values()) == 2:
        remaining_senators = []
        for party, nb_senators in senate.iteritems():
            if nb_senators == 1:
                remaining_senators += party
        return [tuple(remaining_senators)]

    possibles = possible_evacuations(senate)
    for evacuation in possibles:
        new_senate = evacuate(senate, evacuation)
        suite = build_evacuation(new_senate)
        if not suite:
            continue
        return [evacuation] + suite
    return False

f_in = open('input.txt', 'r')
f_out = open('output.txt', 'w')

T = int(f_in.readline())
for test_case in range(1, T+1):
    N = int(f_in.readline())
    raw_senate = f_in.readline().rstrip('\n').split(' ')
    senate = {}
    for idx, senators in enumerate(raw_senate):
        party = chr(ord('A') + idx)
        senate[party] = int(senators)

    f_out.write('Case #{}: {}\n'.format(test_case, ' '.join([''.join(evacuation) for evacuation in build_evacuation(senate)])))
