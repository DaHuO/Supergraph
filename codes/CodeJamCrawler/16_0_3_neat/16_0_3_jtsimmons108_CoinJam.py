import sympy
def convert(base, coinjam):
    sum_ = 0
    for pos in range(len(coinjam)):
        sum_ += base**pos * int(coinjam[-1-pos])
    return sum_ 
    
def first_coinjam_possible(length):
    return 2**(length-1) + 1
    
def all_numbers(coinjam):
    all_nums = []
    for base in range(2,10):
        all_nums += [convert(base, coinjam)]
    all_nums += [int(coinjam)]
    return all_nums
    
def nontrivial_divisors(nums):
    divisors = []
    for num in nums:
        div = sympy.divisors(num)
        if len(div) != 2:
            divisors += [div[1]]
    return divisors
        
def is_coinjam(coinjam):
    bases = all_numbers(coinjam)
    return len(bases) == len(nontrivial_divisors(bases))
    
def find_coinjams(length, number, out_file):
    possible = first_coinjam_possible(length)
    found = 0
    while found < number:
        coinjam = bin(possible)[2:]
        if is_coinjam(coinjam):
            out_file.write(coinjam + " " +  " ".join([str(x) for x in nontrivial_divisors(all_numbers(coinjam))]) + '\n')
            found += 1
        possible += 2
        

directory = '/Users/jeremiahsimmons/Desktop/'
in_file = open(directory + 'input.txt')
out_file = open(directory + 'output.txt', 'w')

num = int(in_file.readline())

for times in range(1, num + 1):
    out_file.write('Case #' + str(times) + ':\n' )
    inputs = in_file.readline().split(' ')
    find_coinjams(int(inputs[0]), int(inputs[1]), out_file)
    
in_file.close()
out_file.close()