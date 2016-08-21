import sys 


def main():

    T = int(sys.stdin.readline().strip())

    for i in range(0,T):
        N = int(sys.stdin.readline().strip())
        num = count_sheep(N)
        print ("Case #%d: %s" % (i+1, num))



#counts sheep - returns a string
def count_sheep(N):
    
    digit = dict()

    for i in range(0,10):
        digit[i] = 1

    i=0
    done=False
    current_num = N

    while not done:

        if current_num == 0:
            if digit.keys()!=[]:
                return "INSOMNIA"
            else:
                return str(current_num)

        last_seen_num = current_num

        while current_num>0:
            d = current_num%10
            current_num = current_num/10
            
            if digit.has_key(d):
                del digit[d]

        if digit.keys()==[]:
            return str(last_seen_num)

        i+=1
        current_num = i*N

        

        
#calling main program
main()





