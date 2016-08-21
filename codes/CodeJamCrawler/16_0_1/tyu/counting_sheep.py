import math

input_file = "A-large.in"
output_file = "A-large.out"

def main():
    results = []
    
    f = open(input_file, 'r')
    T = int(f.readline())
    for t in range(T):
        N = int(f.readline())
        last_number = count_sheep(N)
        results.append(last_number)
    f.close()

    f_out = open(output_file, 'w')
    for t in range(T):
        f_out.write('Case #%d: %s\n' % (t+1, results[t]))
    f_out.close()

def count_sheep(N):
    magnitude = 0
    digits = set()
    i = 1
    num = N
    while (not len(digits) == 10) and i < 10**2:
        num = int(i*N)
        while num >= 10**(magnitude+1):
            magnitude += 1
        rem = num
        for j in range(magnitude+1):
            power = int(10**(magnitude-j))
            digit = rem / power
            digits.add(digit)
            rem -= digit * power
        i += 1
    if len(digits) == 10:
        return str(num)
    else:
        return "INSOMNIA"

if __name__ == "__main__":
    main()
