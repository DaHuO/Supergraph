def _strip_data(data):
    return [x.strip() for x in data.readlines()[1:]]


def _write_output(completed_data, out_file):
    out_lines = ['Case #{}: {}\n'.format(i+1, line) for i, line in enumerate(completed_data)]
    out_file.writelines(out_lines)


def coding_challenge_specific_io(challenge_function):
    with open('input') as in_file:
        parsed_data = _parse_data(_strip_data(in_file))
        completed_data = [challenge_function(data) for data in parsed_data]
    with open('output', 'w') as out_file:
        _write_output(completed_data, out_file)


def _parse_header(header_line):
    header = {}
    header['end_line'] = int(header_line.split()[0])
    return header


def _parse_line(line):
    return [int(x) for x in line.split()]


def _parse_data(in_lines):
    if in_lines: 
        header = _parse_header(in_lines[0])
        end = header['end_line']
        single_test = [] #[_parse_line(line) for line in in_lines[1:end+1]]
        remaining_parsed_data = _parse_data(in_lines[1:])
        return [{'header':header, 'data':single_test}] + remaining_parsed_data
    else:
        return []


def solution(data):
    n = data['header']['end_line']
    original = n
    print(n)
    seen_numbers = set()
    wanted_numbers = set(range(10))
    if n == 0:
        return "INSOMNIA"
    else:
        while seen_numbers != wanted_numbers:
            cur_nums = [int(x) for x in str(n)]
            seen_numbers = seen_numbers.union(cur_nums)
            n = n + original
        return n - original


if __name__ == '__main__':
    coding_challenge_specific_io(solution)
