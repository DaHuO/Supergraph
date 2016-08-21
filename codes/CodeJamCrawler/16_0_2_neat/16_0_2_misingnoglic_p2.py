reversal = {'+':'-', '-':'+'}

def flip(l, spot):
    return [reversal[x] for x in list(reversed(l[:spot]))]+l[spot:]

def last_minus(l):
    s = ''.join(l)
    return s.rfind('-')

def all_correct(l):
    return all([i=='+' for i in l])

def to_str(l):
    return ''.join(l)

with open('small.in') as f:
    cases = f.read().splitlines()[1:]
    case_num = 1
    for case in cases:


        case_list = list(case)
        previous_cases = {to_str(case_list)}
        possibilities = [case_list]
        flips = 0
        answer_found = all_correct(case)
        #import pdb;pdb.set_trace()

        while not answer_found:
            new_possibilities = []
            for p in possibilities:
                ind = last_minus(p)
                for i in range(1,ind+2): # yay 1 indexing
                    f = flip(p, i)
                    if to_str(f) not in previous_cases:
                        new_possibilities.append(f)
                        previous_cases.add(to_str(f))
                    if all_correct(f):
                        answer_found = True
                        break
            possibilities = new_possibilities
            flips += 1

        print "Case #{}: {}".format(case_num, flips)
        case_num+=1
