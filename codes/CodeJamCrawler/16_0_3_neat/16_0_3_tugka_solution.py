import sys

"""
def stupid_is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return i, False
    return None, True

def all_bases_not_prime(n):
    return not any([stupid_is_prime(int(str(n), base))[1] for base in range(2, 10+1)])
"""

def read_case(line):
    line = line.strip().split()
    return int(line[0]), int(line[1])

factor = {2: 3, 3: 2, 4: 5, 5: 2, 6: 7, 7: 2, 8: 3, 9: 2, 10: 11}


def divisible_by_base_factor(n):
    for base in range(2, 10+1):
        number_in_base = int(str(n), base)
        if number_in_base % factor[base] != 0:
            return False
    return True


def make_solution(case):
    length, coun = case

    solution = []
    i = 0
    for number in range(2**(length-1)+1, 2**length, 2):
        number = bin(number)[2:]

        if divisible_by_base_factor(number):
            solution.append(str(number)+" " + " ".join([str(factor[b]) for b in range(2, 10+1)]))
            i += 1

        if i>=coun:
            break

    return "\n".join(solution)


if __name__ == "__main__":
    #f = sys.stdin
    f = open("samples.text")
    count = int(f.readline())
    for c in range(count):
        case = read_case(f.readline())
        solution = make_solution(case)
        print("Case #{}:\n{}".format(c+1, solution))