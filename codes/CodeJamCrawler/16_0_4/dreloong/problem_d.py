# Fractiles

def find_tiles(K, C, S):
    return ' '.join(str(1 + i * K ** (C - 1)) for i in xrange(K))

def main():
    f_in = open('D-small-attempt1.in.txt', 'r')
    f_out = open('D-small-attempt1.out.txt', 'w')

    n_tests = int(f_in.readline())

    for i in range(n_tests):
        params = f_in.readline().split(' ')
        K = int(params[0])
        C = int(params[1])
        S = int(params[2])

        f_out.write('Case #{}: {}\n'.format(i + 1, find_tiles(K, C, S)))

    f_in.close()
    f_out.close()

if __name__ == "__main__":
    main()
