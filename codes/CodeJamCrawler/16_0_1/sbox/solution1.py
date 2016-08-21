#!/bin/python 

def get_last_number(number):
    psuedo_bit_field = [0,1,2,3,4,5,6,7,8,9]
    multi = 1
    multnum = None
    while len(psuedo_bit_field):
        multnum = multi * number
        for digit in str(multnum):
            try:
                psuedo_bit_field.remove(int(digit)) #psuedo_bit_field &= ~(1<<digit) 
            except Exception as e:
                pass
        multi+=1
    return multnum 

def what_is_num(number):
    if number == 0:
        return "INSOMNIA"
    #try:
    number = get_last_number(number)
    return number
    #except:
    #    number = "INSOMNIA"

    return number
if __name__ == "__main__":
    line_count = int(input())
    for line_number in range(line_count):
        number = int(input())
        result = what_is_num(number) # baby dont hurt me
        print("Case #{}: {}".format(line_number+1,result))
