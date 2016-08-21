def fermat(n):
	if n == 2:
		return True
	if not n & 1:
		return False
	return pow(2, n-1, n) == 1

def get_factor(n):    
    for i in range(1, 1000 + 1):
        div, mod = divmod(n, i)
        if mod == 0 and i != 1:
            return i

def get_proof(n):
    ns = []
    for base in range(2, 11):
        interp = int(n, base)
        factor = get_factor(interp)
        ns.append(factor)
    return ns

def solve(test_case):
    N, J = test_case
    count = 0
    for x in range(2**(N - 2)):
        middle = bin(x)[2:].zfill(N - 2)
        candidate = '1' + middle + '1'
        is_good = True
        for base in range(2, 11):
            interp = int(candidate, base)
            if fermat(interp):
                is_good = False
                break
        if is_good:
            fs = get_proof(candidate)
            if None in fs:
                continue
            count += 1
            print(candidate, *fs, sep=' ')
            if count == J:
                break

def read_data(filename):
    with open(filename) as f:
        num_test_cases = int(next(f))
        test_cases = []
        for _ in range(num_test_cases):
            N, J = [int(n) for n in next(f).split()]
            test_case = (N, J)
            test_cases.append(test_case)
    return num_test_cases, test_cases

if __name__ == "__main__":
    num_test_cases, test_cases = read_data("input.in")
    for it in range(num_test_cases):
        test_case = test_cases[it]
        print("Case #{}:".format(it + 1))
        solve(test_case)
