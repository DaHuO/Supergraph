import string

def count_sheeps(N):
    all_digits = []
    for dig in string.digits:
        all_digits.append(dig)
    tries_count=1    
    while len(all_digits) != 0:        
        current_number=tries_count*N
        for dig in str(current_number):
            try:
                all_digits.remove(dig)                
            except:
                pass
        tries_count+=1
        if tries_count>100:
            return 'INSOMNIA'

    return str(current_number)

def main():
    T=int(input('Enter number of test cases:'))
    dest_fd=open(r'C:\Users\Alon_3\Desktop\output.txt', 'w')
    for case in range(T):
        N=int(input())
        dest_fd.write('Case #'+str(case+1)+': '+count_sheeps(N)+'\r\n')
    

if __name__ == '__main__':
    main()