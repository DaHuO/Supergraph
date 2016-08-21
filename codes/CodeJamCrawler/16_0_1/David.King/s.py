import sys

def load_info(f):
    line = f.readline()
    out = int(line)
    return out

def count_sheep(f, case_num):
    print_info = []
    line = f.readline()
    start_n = int(line)
    possible_or_not = False

    a = [0 for x in xrange(10)]
    i = 0
    if start_n == 0: pass
    else: 
        while True:
            if 0 not in a:
                possible_or_not = True
                break 
            i += start_n
            temp = set(str(i))
            for z in xrange(10):
                if a[z] == 0 and str(z) in temp:
                    a[z] += 1
                else: continue
    
    if possible_or_not:
        print_info.append('Case #' + str(case_num+1) + ': ' + str(i))
        print_info.append('\n')
    else:
        print_info.append('Case #' + str(case_num+1) + ': INSOMNIA\n')
    
    return print_info

if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('Counting Sheep > ')
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
                    f_out.writelines(count_sheep(f_in, x))
            except:
                print('something wrong')
            else:
                print('File is built successfully!!!!')
                print('---------------------------\n')
            finally: 
                f_in.close()
                f_out.close()
        
