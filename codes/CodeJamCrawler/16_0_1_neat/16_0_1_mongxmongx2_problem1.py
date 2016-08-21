import fileinput

def check_num(num):
    check = []
    N=1;
    
    for i in range(10):
        check.append(-1)

    while(True):
        
        temp = num * N;
        temp_str = str(temp)

        for j in range(len(temp_str)):
            if( check[int(temp_str[j])] == -1):
                    check[int(temp_str[j])] = temp;

        if(min(check) != -1):
            break;
        N += 1

    return max(check)

if __name__ == "__main__":

    input_file = open("A-large.in")
    output_file = open("A-large.out","w")

    T  = int(input_file.readline())
    result_array = []
    
    for i in range(T):
        Input = int(input_file.readline())

        if(Input != 0):
            result = check_num(Input)
        else:
            result = -1
        result_array.append(result)
            
    for i in range(T):
        if(result_array[i] != -1):
           output_file.write("Case #"+str(i+1)+": " + str(result_array[i]) + "\n")
        else:
            output_file.write("Case #"+str(i+1)+": INSOMNIA\n")
    
