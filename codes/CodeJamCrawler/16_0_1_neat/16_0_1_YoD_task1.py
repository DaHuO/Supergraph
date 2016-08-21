t = int(input())  
test_num = []

digit_sheep_see = [0,0,0,0,0,0,0,0,0,0]

def print_result(test,result):
    print("Case #{}: {}".format(test, result))
    
    
def see_all_digits():
    s = 0
    for i in digit_sheep_see:
        s+=i
    if s == 10:
        return True
    else:
        return False
    
def solve_problem(start_element):
    i = 1
    element = start_element
    while 1:
        # print("New el {}".format(element))
        # print(digit_sheep_see)
        for digit in str(element):
            digit_sheep_see[int(digit)]=1
        if see_all_digits():
            return element
        else:
            i += 1
            element = start_element*i

            # if i > 12:
            #     return "INSOMNIA"
        
    
for i in range(1, t + 1):
    test_num.append(int(input()))
    
# print(test_num)
for i in range(0,len(test_num)):
    if test_num[i] == 0:
        print_result(i+1,"INSOMNIA")
    else:
        res = solve_problem(test_num[i])
        print_result(i+1,res)
        for i in range(0,10):
            digit_sheep_see[i]=0
    