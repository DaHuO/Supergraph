def countSheeps(start_number):
    if start_number == 0:
        return 'INSOMNIA'

    digits = set([int(x) for x in str(start_number)])
    current_number = start_number
    while len(digits) < 10:
        current_number += start_number
        digits = digits.union(set(map(int, str(current_number))))

    return current_number

def main():
    cases_number = int(input())
    for case_number in range(1, cases_number + 1):
        start = int(input())
        print('Case #' + str(case_number) + ':', countSheeps(start))

if __name__ == '__main__':
    main()