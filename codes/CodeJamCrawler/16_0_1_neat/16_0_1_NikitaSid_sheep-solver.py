import pickle

with open('cache.out', 'rb') as f:
    cache = pickle.load(f)

with open('sheep-large-out', 'w') as o:

    with open('A-large.in', 'r') as i:
        num_cases = i.readline()

        case_number = 1

        for line in i.readlines():
            value = int(line.strip())
            print("Case #%s: %s" % (case_number,
                                    cache[value]),
                  file=o)
            case_number += 1

