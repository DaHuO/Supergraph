def counting_sheep(file_name):
    read_file_name = file_name
    write_file_name = file_name + ' - answer.txt'
    
    read_file = open(read_file_name)
    write_file = open(write_file_name, "w")
    
    cases = int(read_file.readline())
    
    current_case = 1
    
    while current_case <= cases:
        num = int(read_file.readline())
        sleep_num = find_sleep_num(num)
        output = "Case #{0}: {1}\n".format(current_case, sleep_num)
        write_file.write(output)
        current_case += 1
        
def find_sleep_num(num):
    num_set = set(range(0, 10))
    
    i = 1
    while i < 100:
        num_str = str(num * i)
        for digit in num_str:
            num_set.discard(int(digit))
        if len(num_set) == 0:
            return num_str
        i += 1
        
    return "INSOMNIA"
        

if __name__ == "__main__":
    
    counting_sheep("A-large.in")