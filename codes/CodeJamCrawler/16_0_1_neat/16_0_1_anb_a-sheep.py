from sys import stdin


def read_str(): return stdin.readline().rstrip('\n')
def read_strs(): return stdin.readline().rstrip('\n').split()
def read_int(): return int(stdin.readline())
def read_ints(): return map(int, stdin.readline().split())
def read_floats(): return map(float, stdin.readline().split())


def solve_case():
    n = read_int()
    
    if n == 0:
        return "INSOMNIA"
        
    digits = set([])
    current = 0
    while len(digits) < 10:
        current += n
        temp = current
        while temp > 0:
            digits.add(temp % 10)
            temp //= 10
        
    return current

    
def main():
    cases = read_int()
    for case in range(1, cases + 1):
        print('Case #{}: {}'.format(case, solve_case()))

        
main()
