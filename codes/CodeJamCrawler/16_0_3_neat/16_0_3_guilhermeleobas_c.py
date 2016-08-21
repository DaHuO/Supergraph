import sys;

def sieve(n):
    m = (n-1) // 2
    b = [True]*m
    i,p,ps = 0,3,[2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            ps.append(p)
        i+=1; p+=2
    return ps

primes = sieve (65536 + 100)

def find_divisor (num_on_base_i):
    for prime in primes:
        if num_on_base_i % prime == 0 and prime != 1 and prime != num_on_base_i:
            return prime;
    return -1;

def get_divisors (num):
    v = [];
    for i in range (2, 11):
        aux = str(bin(num));
        num_on_base_i = int(aux[2:len(aux)], i)
        d = find_divisor (num_on_base_i);
        if (d == -1):
            continue;
        else:
            v.append (d);
    return v;

def solver (n, j, lb, ub):
    for i in range (j):
        while (lb < ub):
            if (1 & lb == 0):
                lb += 1;
                continue;
            num = lb;
            divisors = get_divisors (num);
            if (len(divisors) != 9):
                lb += 1
                continue;
            else:
                for k in range (n-1, -1, -1):
                    if ((1 << k) & num):
                        sys.stdout.write ('1')
                    else:
                        sys.stdout.write ('0');
                sys.stdout.write(' ');
                
                sys.stdout.write (str(divisors[0]));
                for i in range (1, 9):
                    sys.stdout.write (' ' + str(divisors[i]));
                lb += 1;
                print
                # for i in range (2, 11):
                #    aux = str(bin(num))
                #    num_on_base_i = int(aux[2:len(aux)], i)
                #    print num_on_base_i,
                #print
                break;

if __name__ == '__main__':
    t = map(int, raw_input().split())[0];
    n, j = map(int, raw_input().split());
    
    print "Case #1:"
    lb = (1 << (n-1));
    ub = (1 << n);
    
    solver (n, j, lb, ub);
