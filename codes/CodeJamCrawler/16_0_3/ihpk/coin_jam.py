import math

def coin_jam(file_name):
    read_file_name = file_name
    write_file_name = file_name + ' - answer.txt'
    
    read_file = open(read_file_name)
    write_file = open(write_file_name, "w")
    
    cases = int(read_file.readline())
    output = "Case #1:\n"
    write_file.write(output)

    test_case = read_file.readline().split()
    nums_and_divisors = find_coin_jam(int(test_case[0]), int(test_case[1]))
    for result in nums_and_divisors:
        output = " ".join(map(str, result)) + "\n"
        write_file.write(output)
    
def find_coin_jam(n, j):
    #return list
    #each element in list is a list
    #each sublist contains 10 elements
    #jamcoin followed by nine divisors
    
    nums_and_divisors = []
    results = 0
    curr_j_num_list_mid = [0] * (n - 2)
    
    while results < j:
        curr_j_num_list = [1] + curr_j_num_list_mid + [1]
        divisors = []
        i = 2
        while i < 11:
            divisor = find_divisor_in_base_i(i, curr_j_num_list)
            if divisor == 0:
                i = 11
            else:
                divisors.append(divisor)
                i += 1
        if len(divisors) == 9:
            curr_j_num = int("".join(map(str, curr_j_num_list)))
            nums_and_divisors.append([curr_j_num] + divisors)
            results += 1
            print(results)
            print([curr_j_num] + divisors)
            
        increment_j_num_list(curr_j_num_list_mid)
        
    return nums_and_divisors

def increment_j_num_list(j_num_list_mid):
    i = len(j_num_list_mid) - 1
    carry = 1
    
    while carry != 0:
        if j_num_list_mid[i] == 0:
            j_num_list_mid[i] = 1
            carry = 0
        else:
            j_num_list_mid[i] = 0
        i -= 1

def find_divisor_in_base_i(i, j_num_list):
    j_num_in_base_i = convert_to_base_i(i, j_num_list)
    
    if j_num_in_base_i % 2 == 0:
        return 2
    else:
        counter = 3
        while counter < math.sqrt(j_num_in_base_i) + 1:
            if j_num_in_base_i % counter == 0:
                return counter
            counter += 2
        return 0

def convert_to_base_i(i, j_num_list):
    num = 0
    
    i_exp = i ** (len(j_num_list) - 1)
    for digit in j_num_list:
        num += digit * i_exp
        i_exp /= i
    
    return num
        
    
if __name__ == "__main__":
    #coin_jam("test.in")
    #coin_jam("C-small-attempt1.in")
    coin_jam("C-large.in")