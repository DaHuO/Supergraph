import sys, math

def interpret(number, base):
    digits = list(number)
    acc = 0
    i = len(number) - 1
    for digit in digits:
        acc = acc + (int(digit) * (base ** i))
        i = i - 1
    return acc

def next_number(number):
    acc = number[1:-1]
    acc_n = interpret(acc, 2) + 1
    new_component = "{0:0b}".format(acc_n)
    new_component = new_component.rjust(len(acc), '0')
    number = number[0] + new_component + number[-1]
    return number

def return_divisor(number):
    root = int(math.sqrt(number)) + 1
    test_divisors = [2] + range(3, root, 2)
    for i in test_divisors:
        if (number % i) == 0:
            return i
    return -1

def gather_divisors(number):
    divisors = []
    for base in range(2,11):
        num = interpret(number, base)
        divisor = return_divisor(num)
        divisors.append(str(divisor))
        if divisor == -1:
            break
    
    return divisors

def generate_coinjams(n,j):
    end_str = '1' * n
    num_str = '1' + (n-2) * '0' + '1'
    
    coinjams = []
    while True:       
        divisors = gather_divisors(num_str)
        
        #print num_str, divisors        
        
        if len(divisors) != 0 and divisors[-1] != '-1':        
            coinjams.append([num_str, divisors])
            
        if num_str == end_str or len(coinjams) >= j:
            break
        
        num_str = next_number(num_str)
    
    return coinjams
    

def Solve(case):
    input_string = case.split()
    n = int(input_string[0])
    j = int(input_string[1])
    coinjams = generate_coinjams(n,j)
    
    output_str = '\n'
    for coinjam in coinjams:
        div_str = ' '.join(coinjam[1])
        output_str = output_str + coinjam[0] + ' ' + div_str + '\n'
    
    return output_str
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "No input file given. Exiting..."
        sys.exit()    
    
    with open(sys.argv[1], 'r') as inputFile:        
        numCases = int(inputFile.readline())

        if numCases <= 0:
            print "No cases"
            sys.exit()
    
        with open('output', 'w') as outputFile:
                
            for i in range(0, numCases):
                case = inputFile.readline()
                print "Input: ", case
                case.split()
                output = Solve(case)
                print "Output: ", output
                outputFile.writelines(["Case #", str(i+1), ": ", output, "\n"])