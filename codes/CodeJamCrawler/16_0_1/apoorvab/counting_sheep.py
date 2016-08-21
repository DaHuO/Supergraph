__author__ = 'apoorvab'


def get_parsed_line():
    return list(map(int, input().split()))


def get_case():
    number = get_parsed_line()[0]

    return number

if __name__ == '__main__':
    num_cases = get_parsed_line()[0]

    for case_num in range(0, num_cases):

        number = get_case()
        has_seen = set(list('0123456789'))
        abort = False
        iter_count = 0
        cur_number = number

        while(abort is False):

            to_subtract = set(list(str(cur_number)))
            has_seen -= to_subtract

            if number == 0:
                print('Case #%s: INSOMNIA' % (case_num + 1))
                abort = True
            elif len(has_seen) == 0:
                print('Case #%s: %s' % (case_num + 1, cur_number))
                abort = True
            else:
                iter_count += 1
                cur_number += number
