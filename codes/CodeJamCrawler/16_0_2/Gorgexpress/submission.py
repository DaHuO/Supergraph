out = open("B-small.out", "a")
with open("B-small-attempt2.in") as f:
    case_num = 1
    num_cases = int(f.readline())
    for line in f:
        pancakes = line[:-1]
        count = 0;
        char = pancakes[0]
        for pancake in pancakes:
            if pancake != char:
                char = pancake
                count += 1
        if char == '-':
            count += 1
        out.write("Case #{}: {}\n".format(case_num, count))
        case_num += 1
out.close()