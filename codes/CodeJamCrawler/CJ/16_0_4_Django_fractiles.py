import sys, itertools

K = None #number of tiles
C = None #complexity
S = None #students
nrof_cases = None

with open(sys.argv[1], 'r') as f:
    nrof_cases = int(f.readline())
    case_number = 1

    for line in f:
        line = line.split()
        K = int(line[0])
        C = int(line[1])
        S = int(line[2])

        if S==K:
            indexes = " ".join([str(i) for i in range (1, K+1)])
            print("Case #%d: %s" % (case_number, indexes))
            case_number = case_number + 1
            continue

            

        original = itertools.product('LG',repeat=K)
        original = ["".join(list(o)) for o in original]

        number_of_sequences = len(original)
        d = {}

        for i in original:
            d[i] = i

        for i in range (C-1):
            for i, key in enumerate(d.keys()):
                d[key] = d[key].replace("G","%temp%").replace("L",key).replace("%temp%","G"*K)

        #skipping sequences with no gold
        remove = []
        remove = [k for k in d if "G" not in d[k]]
        for r in remove:
            del d[r]

        sequencesize = 0
        for v in d.values():
            sequencesize = len(v)
            break

        #initing setlist
        setlist = []
        for i in range (sequencesize):
            setlist.append(set())


        for v in d.values():
            for i, c in enumerate(v):
                if c == 'G':
                    setlist[i].add(v)
        
        searched_item = None
        for item in itertools.product(setlist,repeat=S):
            union_set = set()
            for i in item:
                union_set = union_set.union(i)

            #we need to consider the removed strings
            if len(union_set) + len(remove) == number_of_sequences:
                searched_item = item
                break
        
        indexes = []
        if searched_item:
            #print(searched_item)
            #print(line)
            for i, it in enumerate(searched_item):
                for j in setlist:
                    if it==j:                      
                        indexes.append(str(i+1))
                        break
        if indexes:
            indexes = " ".join(indexes)
        else:
            indexes = "IMPOSSIBLE"

        print("Case #%d: %s" % (case_number, indexes))
        case_number = case_number + 1
