import sys


def load_info(f):
    line = f.readline()
    out = int(line)
    return out    

def evacuate_sanators(f, case_num):
    print_info = []
    line = f.readline()
    N = int(line)
    
    senate = [int(x) for x in f.readline().split(' ')]
    ev_plan = []
    if N == 2:
        i = 0
        while i < senate[0]:
            ev_plan.append('AB')
            i += 1
    if N > 2:
        
        new_senate= []
        i = 65
        for x in senate:
            new_senate.append([chr(i),x])
            i += 1
        new_senate.sort(key = lambda party: -party[1])

        i = 0
        while i < len(senate) - 1:
            if new_senate[i][1] > new_senate[i+1][1] >= 1:
                diff = new_senate[i][1] - new_senate[i+1][1]
                j = 0
                
                while j < diff:
                    k = 0
                    while k < i+1:
                        new_senate[k][1] -= 1
                        ev_plan.append(new_senate[k][0])
                        k += 1
                    j += 1
            i += 1
            
        if new_senate[0][1] == 1:
            if len(new_senate)%2 == 1:
                ev_plan.append(new_senate[0][0])
                i = 1
                while i < len(senate):
                    ev_plan.append(new_senate[i][0]+new_senate[i+1][0])
                    i += 2
            else:
                i = 0
                while i < len(senate):
                    ev_plan.append(new_senate[i][0]+new_senate[i+1][0])
                    i += 2
        else:
            diff = new_senate[0][1] - 1
            i = 0
            j = 0
            while j < diff:
                i = 0
                while i < len(senate):
                    ev_plan.append(new_senate[i][0])
                    i += 1
                j += 1
            if len(new_senate)%2 == 1:
                ev_plan.append(new_senate[0][0])
                i = 1
                while i < len(senate):
                    ev_plan.append(new_senate[i][0]+new_senate[i+1][0])
                    i += 2
            else:
                i = 0
                while i < len(senate):
                    ev_plan.append(new_senate[i][0]+new_senate[i+1][0])
                    i += 2        
    print_info.append('Case #' + str(case_num+1) + ':')
    for x in ev_plan:
        print_info.append(' ' + x)
    print_info.append('\n')

    return print_info
    
if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('Problem Name > ')
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
                    f_out.writelines(evacuate_sanators(f_in, x))
##            except:
##                print('something wrong')
##            else:
##                print('File is built successfully!!!!')
##                print('---------------------------\n')
            finally: 
                f_in.close()
                f_out.close()
