
def solve(n):
    def num_to_arr(num):
        arr = []
        while num > 0:
            arr.append(num % 10)
            num /= 10
        arr.reverse()
        return arr

    def hash_arr(arr):
        return hash(arr.__str__())

    if n == 0: return 'INSOMNIA'

    curr = num_to_arr(n)
    next = []
    visited = set([hash_arr(curr)])
    numbers = set(curr)
    k = 2

    while True:
        next.extend(num_to_arr(n * k))
        hashcode = hash_arr(next)

        if hashcode in visited:
            return 'INSOMNIA'
        
        visited.add(hashcode)
        
        for elem in next:
            numbers.add(elem)

        if len(numbers) == 10:
            return ''.join([str(elem) for elem in next])

        next = []
        k += 1


if __name__ == "__main__":
    FILENAME = 'A-large.in'
    lines = open(FILENAME, 'r').read().split('\n')
    T = int(lines[0])

    for case in range(1, T+1):
        data = lines[case]

        answer = solve(int(data))
        print "Case #{0}: {1}".format(case, answer)
