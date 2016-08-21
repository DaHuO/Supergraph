#!python3

def factor(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        else:
            d += 1
    if n > 1:
        return n

def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def generate_sets(N):
    max_len = N - 2
    return ['1' + str(bin(x)[2:].rjust(max_len, '0')) + '1' for x in range(2 ** max_len)]


def jamset_is_valid(jamset):
    for base in list(range(2, 11)):
        desirialize_jamset = int(jamset, base)
        if (is_prime(desirialize_jamset)):
            return False
    return True


def get_all_valid_jamsets(N, J):
    jamsets = []
    for jamset in generate_sets(N):
        if jamset_is_valid(jamset):
            jamsets.append(jamset)
        if len(jamsets) == J:
            return jamsets

def verifying_line(jamset):
    response_line = []
    for base in list(range(2, 11)):
        desirialize_jamset = int(jamset, base)
        response_line.append(factor((desirialize_jamset)))
    return ' '.join([str(x) for x in response_line])




if __name__ == "__main__":
    import fileinput

    f = fileinput.input()

    T = int(f.readline())
    for case in range(1, T + 1):
        N, J = f.readline().split()
        N = int(N)
        J = int(J)
        jamsets = get_all_valid_jamsets(N, J)
        print("Case #{0}:".format(case))
        for jamset in jamsets[:J]:
            print("{0} {1}".format(jamset, verifying_line(jamset)))
