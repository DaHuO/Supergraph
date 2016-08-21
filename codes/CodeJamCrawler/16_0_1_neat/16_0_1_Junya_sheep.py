def print_result(i, x):
    print 'Case #{}: {}'.format(i, x)

def handle_test(i):
    N = raw_input()
    if N == '0':
        print_result(i, "INSOMNIA")
        return
    
    digits = set()
    iteration = 1
    while True:
        x = str(iteration * int(N))
        for c in x:
            digits.add(c)
        if all([y in digits for y in ('0', '1', '2', '3', '4', '5', '6', '7', '8' ,'9')]):
            print_result(i, x)
            return
        iteration += 1

def main():
    n = int(raw_input())
    for index in range(n):
        handle_test(index + 1)
        
if __name__ == "__main__":
    main()
    
