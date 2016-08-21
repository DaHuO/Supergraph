import math
def main():
    with open('A-large.in', 'r') as f:
        T = int(f.readline())
        for i in range(0,T):
            print("Case #{0}: {1}".format(i+1, counter(int(f.readline()))))

def counter(n):
    if n == 0:
        return "INSOMNIA";
    values = {}
    count = 0;
    while len(values)<10:
        count = count + 1

        num = n * count
        inner_count = 0
        while num > 0:
            x = num % 10
            num = int(num/10)
            values[x] = True
    return str(n*count)

if __name__ == '__main__':
    main()
