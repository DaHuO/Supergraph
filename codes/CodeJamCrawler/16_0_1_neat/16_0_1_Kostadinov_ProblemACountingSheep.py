def solve(str_number):
    num = int(str_number)
    
    if num == 0:
        return "INSOMNIA" 
    
    result = num
    
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    
    while True:
        str_result = str(result)
        digits = [d for d in digits if d not in str_result]
        if len(digits) == 0:
            return str_result
        else:
            result += num


# Read file
with open('input.txt') as f:
    content = f.readlines()

f_output = open("output.txt", "wb")
for i in range(1, int(content[0]) +1):
    f_output.write("Case #" + str(i) + ": " +solve(content[i]) + "\r\n");
f_output.close()


