import sys
import time

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        str_number = raw_input()
        if (int(str_number) is 0):
            print ("Case #{}: {}".format(i, "Insomnia"))
        else:
            a = set([])
            b = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            j = 1
            
            while(a != b):
                
                
                str_mult_number = str(int(str_number)*j)
                for c in str_mult_number:
                    a.add(int(c))
                j=j+1
                  
                    
                

            print ("Case #{}: {}".format(i, str_mult_number))


                                         
main()

