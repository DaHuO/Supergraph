import sys

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')
    T = int(fin.readline())
    for k in range(T):
        N = int(fin.readline())
        digits = [0 for i in range(10)]
        all_digits = 0
        last_digit = 0
        d = 0
        for i in range (1, 400):
            sheep_counter = N*i
            last_digit = sheep_counter
            d_array = map(int, str(sheep_counter))  
            for j in range(len(d_array)):
                d = int(d_array[j])
                if digits[d] == 0:
                    digits[d] = 1
                    all_digits += 1
            if all_digits == 10:  
                break

        if all_digits == 10:
            fout.write ("Case #" + str(k+1) + ": " + str(last_digit) + "\n")
        else:
            fout.write ("Case #" + str(k+1) + ": INSOMNIA\n")
    fin.close()
    fout.close()