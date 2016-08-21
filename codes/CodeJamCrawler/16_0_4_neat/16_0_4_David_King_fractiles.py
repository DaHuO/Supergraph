import sys        

def load_info(f):
    line = f.readline()
    out = int(line)
    return out   
        
def clean_tiles(f, case_num):
    print_info = []
    line = f.readline()
    num_of_tiles, complexities, num_of_students = [int(y) for y in line.split(' ')]
    possible_or_not = False
    if num_of_tiles == 1:
        positions = [1]
        possible_or_not = True
    elif complexities == 1:
        if num_of_students == num_of_tiles:
            positions = [x+1 for x in xrange(num_of_tiles)]
            possible_or_not = True
    else:
        minimum_num_of_students = num_of_tiles%2 + num_of_tiles/2
        if num_of_students >= minimum_num_of_students:
            positions = [0 for x in xrange(minimum_num_of_students)]
            possible_or_not = True
            if num_of_tiles%2 == 1:
                positions[minimum_num_of_students - 1] = num_of_tiles**2
            i = 0
            while i < num_of_tiles/2:
                if i == 0:
                    positions[i] = 2
                else:
                    positions[i] = (2*i + 1) * num_of_tiles + 2*i + 1 
                i += 1
            
    if possible_or_not:
        print_info.append('Case #' + str(case_num + 1) + ':')
        for position in positions:
            print_info.append(' ' + str(position))
        print_info.append('\n')
    else:
        print_info.append('Case #' + str(case_num + 1) + ': IMPOSSIBLE\n')

    return print_info

if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('Fractiles > ')
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
                    f_out.writelines(clean_tiles(f_in, x))
##            except:
##                print('something wrong')
##            else:
##                print('File is built successfully!!!!')
##                print('---------------------------\n')
            finally: 
                f_in.close()
                f_out.close()
        
        
