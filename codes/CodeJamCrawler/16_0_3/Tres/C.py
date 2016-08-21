import fileinput

def not_prime ( n ) :
    return next(( i for i in range(2, 1000) if not n%i ), None)

if __name__ == "__main__" :
    test_case = 1
    num_found = 0
    for line in fileinput.input() :
        if fileinput.isfirstline() :
            continue
        inp = line.split()
        n = int(inp[0])
        j = int(inp[1])

        nums = [ i**(n-1) + 1 for i in range(11) ]

        print("Case #{}:".format(test_case))

        while num_found < j :

            factors = [ not_prime(i) for i in nums[2:] ]
            if all(factors) :
                print(format(nums[2], 'b'), end=' ')
                print(' '.join(list(map(str, factors))))
                num_found += 1

            nums[2] += 2
            for i in range(3, 11) :
                nums[i] = int(format(nums[2], 'b'), i)


        test_case += 1