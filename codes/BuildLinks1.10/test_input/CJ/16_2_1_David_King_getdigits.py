import sys


def load_info(f):
    line = f.readline()
    out = int(line)
    return out    

def get_digits(f, case_num):
    res = []
    print_info = []
    line = f.readline().strip('\n')
    num_pool = list(line)
    check_pool = [['ZERO', 0],
                  ['WTO', 2],
                  ['XSI', 6],
                  ['SEVEN', 7],
                  ['VFIE', 5],
                  ['FOUR', 4],
                  ['RTHEE', 3],
                  ['ONE', 1],
                  ['TEIGH', 8],
                  ['NINE', 9]
                 ]
##    print(check_pool)
    for num in check_pool:
        while True:
            if num[0][0] in num_pool:
                res.append(num[1])
                for l in num[0]:
                    num_pool.remove(l)
            else:
                break
        
    print_info.append('Case #' + str(case_num+1) + ': ')
    for num in sorted(res):
        print_info.append(str(num))
    print_info.append('\n')
    return print_info
    
if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('Get Phone # > ')
        input_args = str(raw_input())
        try:
            if input_args == 'exit':
                break
            elif input_args == '':
                continue
            else:
                args = input_args.split(' ')
                input_file = args[0]
                output_file = args[1]
        except:
            print('Invalid input. Please try again.')
        else:
            f_in = open(input_file)
            f_out = open(output_file, 'w')
            
            num_of_tests = load_info(f_in)
            try:
                for x in xrange(num_of_tests):
                    f_out.writelines(get_digits(f_in, x))
##            except:
##                print('something wrong')
##            else:
##                print('File is built successfully!!!!')
##                print('---------------------------\n')
            finally: 
                f_in.close()
                f_out.close()
