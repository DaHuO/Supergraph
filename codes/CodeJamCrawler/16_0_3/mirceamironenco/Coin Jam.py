solutions = {}

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False

    if n == 2:
        return (True,-1)

    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return (False, x)

    return (True, -1)

def generate_jam(list_number):
    string_jam = ''.join(str(x) for x in list_number)
    if string_jam in solutions:
        return

    divs = []
    for i in range(2,11):
        is_prime, div = isprime(int(string_jam,i))
        if not is_prime:
            divs.append((i,div))
        else:
            break
    else:
        solutions[string_jam] = divs


def brute_force_noob_solution(number,index):
    if len(solutions) < 50:
        for i in range(index,15):
            number[i] = 1
            generate_jam(number)
            if len(solutions) >= 50:
                return
            brute_force_noob_solution(number,i+1)
            number[i] = 0

if __name__ == "__main__":
    start = list('1000000000000001')
    brute_force_noob_solution(start, 1)
    print("Case #1:")
    for key in solutions:
        to_print = '' + key
        for elem in solutions[key]:
            to_print += " " + str(elem[1])
        print(to_print)