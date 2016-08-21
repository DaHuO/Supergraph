# Revenge of the Pancakes

from Queue import Queue

def min_flips(pattern):
    count = 0
    for i in range(1, len(pattern)):
        if pattern[i] != pattern[i - 1]:
            count += 1
    if pattern[-1] == '-':
        count += 1
    return count

def main():
    f_in = open('B-large.in.txt', 'r')
    f_out = open('B-large.out.txt', 'w')

    n_tests = int(f_in.readline())
    for i in range(n_tests):
        pattern = f_in.readline().strip('\n')
        f_out.write('Case #{}: {}\n'.format(i + 1, min_flips(pattern)))

    f_in.close()
    f_out.close()

if __name__ == "__main__":
    main()
