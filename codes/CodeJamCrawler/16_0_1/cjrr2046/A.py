

filename_in  = "a.in"
filename_out = "a.out"

filename_in  = "A-small-attempt0.in"
filename_out = "A-small-attempt0.out"

filename_in  = "A-large.in"
filename_out = "A-large.out"


fileobj_in  = open (filename_in , "r")
fileobj_out = open (filename_out, "w")

t = int (fileobj_in.readline ().strip ())

idx_test_case = 0

while idx_test_case < t:

    n = int (fileobj_in.readline ().strip ())
    
    digit_dict    = {}
    number_dict   = {}
    n_step        = 1
    
    while True:
    
        sw_all_digits = True
        
        current_number = str (n * n_step)
        
        for digit_str in current_number:
            digit_dict[int (digit_str)] = True
        
        for digit_int in range (10):
            if digit_int not in digit_dict:
                sw_all_digits = False
                break

        if ((current_number in number_dict) and (not (sw_all_digits))) or (sw_all_digits):
            break
        
        number_dict[current_number] = True
        
        n_step = n_step + 1
    
    str_answer = "INSOMNIA"
    if sw_all_digits:
        str_answer = str (current_number)
    
    idx_test_case = idx_test_case + 1

#    print ("Case #%d: " + str_answer) % (idx_test_case, )
    fileobj_out.write (("Case #%d: " + str_answer + "\n") % (idx_test_case, ))
    


#a = {}
#
#a[1] = 10
#print a
#print 1 in a 
#print 10 in a

fileobj_in.close ()
fileobj_out.close ()
