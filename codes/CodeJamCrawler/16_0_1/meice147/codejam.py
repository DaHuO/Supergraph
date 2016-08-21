#!/usr/bin/env python

def main():
    number = int(input())
    j = 1
    i = 1
    num_list = [];
    for x in range(1,number+1):
        input_num = int(input())
        j=1
        if(input_num == 0):
            print("Case #{0}: INSOMNIA".format(i))
            i+=1
            continue
        while 1:
            num = j * input_num
            num_list2 = list(str(num))
            for x in num_list2:
                if(x not in num_list):
                    num_list.append(x)
            j+=1
            if(len(num_list) == 10):
                print("Case #{0}: {1}".format(i,num))
                i +=1
                num_list =[]
                num_list2 = []
                break  

if __name__ == '__main__':
    main()  