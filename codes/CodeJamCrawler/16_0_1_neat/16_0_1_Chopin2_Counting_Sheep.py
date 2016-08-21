import sys

def reading_the_file(input_file):
    f = open(input_file, 'r+')
    return f

def getting_test_cases(f):
    y0 = []
    for counter, line in enumerate(f):
        case = counter + 1
        if counter == 0:
            number_of_test_cases = line
            continue
        if counter > 0:
            y0.append(int(line[:-1]))
    return {'C': y0, 'cases' : int(number_of_test_cases) }

def going_through_the_cases(C,cases):
    output_file_name = sys.argv[1][:-2]+'out'
    with open(output_file_name, 'w') as f:
        for i in range(cases):
            result = algorithm(C[i])
            f.write('Case #{}'.format(i+1)+': '+ str(result) + '\n')

def algorithm(N):
    i = 1
    solved = 0
    digits_encountered = []
    if N == 0:
        return "INSOMNIA"
    while solved == 0:
        last_number_seen = N*i
        digits_encountered.extend(list(str(last_number_seen)))
        digits_encountered = remove_duplicates(digits_encountered)
        i += 1
        if len(digits_encountered) == 10:
            solved += 1
            return last_number_seen


def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

def main():
    input_file = sys.argv[1]
    going_through_the_cases(**getting_test_cases(reading_the_file(input_file)))

if __name__ == '__main__':
    main()

