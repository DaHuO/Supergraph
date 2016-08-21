import time

def count_sheep(t, start):
    digits = [0,1,2,3,4,5,6,7,8,9]
    max_exec = 0.1
    
    i = 1
    start_time = time.time()
    while(len(digits) and (time.time() - start_time < max_exec)):
        cur = (start * i)
        for digit in str(cur):
            if int(digit) in digits:
                digits.remove(int(digit))
        i += 1

    if (time.time() - start_time) > max_exec: 
        print('Case #{}: INSOMNIA'.format(t))
    else:
        print('Case #{}: {}'.format(t, cur))

def main():
    with open('A-large.in', 'r') as f:
        for line_num, line in enumerate(f):
            if(line_num != 0):
                count_sheep(line_num, int(line))
        pass

if __name__ == '__main__':
    main()
