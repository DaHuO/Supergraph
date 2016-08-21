def epilogue(result, num):
    out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('A-large.in', 'r'), open('A-large.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
    num_parties = int(in_file.readline())
    counts = [int(x) for x in in_file.readline().split()]
    benchmark = [0 for _ in range(len(counts))]
    output = ''
    while counts != benchmark:
        total = sum(counts)
        if counts[0] > counts[1]:
            max1, max2, idx1, idx2 = counts[0], counts[1], 0, 1
        else:
            max1, max2, idx1, idx2 = counts[1], counts[0], 1, 0

        for i in range(2, len(counts)):
            if counts[i] > max1:
                max1, max2 = counts[i], max1
                idx1, idx2 = i, idx1
            elif counts[i] > max2:
                max2 = counts[i]
                idx2 = i
        print(counts)
        print(idx1, idx2)
        if total == 3:
            counts[idx1] -= 1
            output += chr(idx1 + 65) + ' '
        elif total == 2:
            counts[idx1] -= 1
            counts[idx2] -= 1
            output += chr(idx1 + 65) + chr(idx2 + 65)
            break
        else:
            counts[idx1] -= 1
            counts[idx2] -= 1
            output += chr(idx1 + 65) + chr(idx2 + 65) + ' '
    print()
    epilogue(output, case_num)