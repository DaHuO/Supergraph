import sys

def AddIfMissing(num_list, num):
    add = True
    for elm in num_list:
        add = add and (elm != num)
    
    if add == True:
        num_list.append(num)
        
    return num_list
            

def Solve(case):
    base = int(case)

    if base == 0:
        return "INSOMNIA"
    
    present_num = []
    i = 1
    while True:
        acc = base * i
        acc_str = str(acc)
        digits = list(acc_str)
        for digit in digits:
            AddIfMissing(present_num, int(digit))
        
        if(len(present_num) == 10):
            return str(acc)
        
        i = i +1
        

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "No input file given. Exiting..."
        sys.exit()    
    
    with open(sys.argv[1], 'r') as input_file:        
        n_cases = int(input_file.readline())

        if n_cases <= 0:
            print "No cases"
            sys.exit()
    
        with open('output', 'w') as output_file:
                
            for i in range(0, n_cases):
                case = input_file.readline()
                # print "Input: ", case
                case.split()
                output = Solve(case)
                #print "Output: ", output
                output_file.writelines(["Case #", str(i+1), ": ", output, "\n"])