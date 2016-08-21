# -*- coding:Utf-8 -*-
from sys import argv

def test_value(n,d) :
    multiple = 0
    value_to_test=n
    while d != [] :
        multiple += 1
        value_to_test = n * multiple
        n_in_str = str(value_to_test)
        for i in range(len(n_in_str)) :
            if d == [] :
                break
            else :
                if int(n_in_str[i]) in d :
                    #print n_in_str[i],
                    d.remove(int(n_in_str[i]))
    return(value_to_test)
        
    #print
        
def main() :
    f_input=argv[1:][0]
    f_output= open("counting_sheep_large_0.txt",'w')
    read_input = open(f_input,'r')
    nb_of_case = read_input.readline()
    nb_of_case = int(nb_of_case)
    d_solved = {}
    for i in range(nb_of_case) :
        start_value = int(read_input.readline())
        if start_value == 0 :
            f_output.writelines("Case #"+str(i+1)+": INSOMNIA\n")
        elif d_solved.has_key(start_value) :
            result = d_solved[start_value]
            f_output.writelines("Case #"+str(i+1)+": "+str(result)+'\n')
        else :
            d=range(10)
            result=test_value(start_value,d)
            f_output.writelines("Case #"+str(i+1)+": "+str(result)+'\n')
            d_solved[start_value] = result
        
    f_output.close()

    
    
if __name__ == "__main__" :
    main()