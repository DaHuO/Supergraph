def evacuation_plan(n, people):
    plan = []
    remaining_people = sum(people)
    while remaining_people > 0:
        max_people = max(people)
        # total_people = sum(people)
        people_with_index = [(i, p) for i, p in enumerate(people)]
        # print "people_with_index", people_with_index
        people_with_max = filter(lambda x: x[1] == max_people, people_with_index)
        # print "people_with_max", people_with_max

        if len(people_with_max) > 1 and (max_people > 1 or len(people_with_max) == 2):
            case = chr(people_with_max[0][0] + 65) + chr(people_with_max[1][0] + 65)
            plan.append(case)

            people[people_with_max[0][0]] -= 1
            people[people_with_max[1][0]] -= 1
        else:
            case = chr(people_with_max[0][0] + 65) * min(max_people, 2)
            plan.append(case)

            people[people_with_max[0][0]] -= min(max_people, 2)

        remaining_people = sum(people)

    return " ".join(plan)

if __name__ == '__main__':
    case = 'A-sample'
    case = 'A-small-attempt0'
    case = 'A-large'
    
    inp = open('%s.in'%case)
    out = open('%s.out'%case, 'w')

    cases = int(inp.readline())
    for i in xrange(1, cases + 1):
        n = int(inp.readline())
        people = [int(x) for x in inp.readline().split()]

        o = "Case #%d: %s"%(i, str(evacuation_plan(n, people)))
        print o
        out.write('%s'%o)
        if i < cases:
            out.write('\n')
