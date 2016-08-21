##input = open('A-sample-input.txt', 'r')
##output = open('A-sample-output.txt', 'w')

##input = open('A-small-attempt0.in', 'r')
##output = open('A-small.out', 'w')

input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(n):
    if n == 0:
        return "INSOMNIA"
    num = n
    nums = ""
    while len(nums) < 10:
        nstring = str(num)
        for char in nstring:
            if char not in nums:
                nums += char
        num += n
    return int(nstring)

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        n = read_int()
##        if case == 1:
        solution = solve(n)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        




main()
input.close()
output.close()
    
