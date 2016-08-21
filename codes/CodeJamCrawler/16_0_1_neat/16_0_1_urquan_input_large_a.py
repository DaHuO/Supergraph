def read_file():
    f = open("A-large.in", 'r')
    num_case = int(f.readline())
    limit = 10^6

    for n in range(num_case):
        row_input = int(f.readline())
        num_set = set()
        last_num = 0
        i=1
        if row_input <= 0: #or row_input > limit:
            print_result(n+1, 'INSOMNIA')
        else:
            while(len(num_set)<10):
                last_num = row_input*i
                num_set.update(split_num(last_num))  
                i+=1
            print_result(n+1, last_num)
            
def split_num(num):
    new_list = []
    while(num):
        n = num%10
        new_list.append(n)
        num = num/10
    return new_list

def print_result(case, last_num):
    print('Case #{}: {}'.format(case,last_num))    

read_file()