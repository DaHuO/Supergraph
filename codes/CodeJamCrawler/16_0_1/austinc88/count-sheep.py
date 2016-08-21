if __name__ == "__main__":

    import fileinput
    input_file = fileinput.input()

    T = int(input_file.readline())
    output_f = open('A-large.out','w+')
    for case in range(1,T+1):
        val = int(input_file.readline())
        answer_key = set([0, 1, 2, 3 ,4, 5, 6, 7, 8, 9])
        working_val_array = []
        working_val = val
        for ch in str(val):
            working_val_array.append(int(ch))
        compare_key = set(working_val_array)
        for index in range(2,1000001):
            diff_set = answer_key.difference(compare_key)
            if len(diff_set) is 0:
                output_f.write("Case #{0}: {1}\n".format(case, working_val))
                break
            working_val = val * index
            working_val_array = []
            for ch in str(working_val):
                working_val_array.append(int(ch))
            compare_key = compare_key | set(working_val_array)
            print compare_key
        if len(diff_set) is not 0:
            output_f.write("Case #{0}: INSOMNIA\n".format(case))
    output_f.close()