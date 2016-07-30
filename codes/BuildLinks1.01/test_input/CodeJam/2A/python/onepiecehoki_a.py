import itertools


T = int(raw_input())

Trees = {}

def generate_match(winner, N):
    def get_next_level_element(el):
        if el == 'R':
            return ['S', 'R']
        elif el == 'S':
            return ['S', 'P']
        elif el == 'P':
            return ['P', 'R']
    def get_next_level(cur_level):
        next_level = [get_next_level_element(x) for x in cur_level]
        return list(itertools.chain.from_iterable(next_level))

    cur_level = [winner]
    for i in xrange(0, N):
        cur_level = get_next_level(cur_level)

    return cur_level

def count_match(match):
    counter = {}
    for x in match:
        if not x in counter:
            counter[x] = 0
        counter[x] += 1
    return counter

def special_sort(match):
    smatch = match[:]
    while len(smatch) > 1:
        for i in xrange(0, len(smatch), 2):
            if smatch[i] > smatch[i+1]:
                temp = smatch[i]
                smatch[i] = smatch[i+1]
                smatch[i+1] = temp
        smatch = [smatch[i] + smatch[i+1] for i in xrange(0, len(smatch), 2)]
    return [x for x in smatch[0]]



for t in xrange(1, T+1):
    NRPS = raw_input().strip().split()
    N,R,P,S = tuple([int(x) for x in NRPS])

    solution_match = None

    #Case where last winner is R
    match = generate_match('R', N)
    match_counter = count_match(match)
    if match_counter.get('R',0) == R and match_counter.get('P',0) == P and match_counter.get('S',0) == S:
        if solution_match == None or solution_match > match:
            solution_match = match
    #Case where last winner is S
    match = generate_match('S', N)
    match_counter = count_match(match)
    if match_counter.get('R',0) == R and match_counter.get('P',0) == P and match_counter.get('S',0) == S:
        if solution_match == None or solution_match > match:
            solution_match = match
    #Case where last winner is P
    match = generate_match('P', N)
    match_counter = count_match(match)
    if match_counter.get('R',0) == R and match_counter.get('P',0) == P and match_counter.get('S',0) == S:
        if solution_match == None or solution_match > match:
            solution_match = match



    if solution_match != None:
        solution_match = special_sort(solution_match)
        print('Case #%d: %s' %(t, ''.join(solution_match)))
    else:
        print('Case #%d: IMPOSSIBLE' %(t))




    

