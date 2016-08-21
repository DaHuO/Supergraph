def int_to_bin(n):
    answer = ""
    while n>0:
        answer=str(n%2)+answer
        n//=2
    return answer
   
def first_divisor(n):
    if n%2==0:
        return 2
    for divisor in range(3,n,2):
        if divisor>100000:
            return 0
        if n%divisor == 0:
            return divisor
    return 0
 
def main():
    cases = int(input())
    row = input().split()
    N = int(row[0])
    J = int(row[1])
    print("Case #1:")
    start = 2**(N-1)+1
    stop = 2**(N)
    for candidate in range(start, stop, 2):
        current = int_to_bin(candidate)
        divisors = list()
        not_prime = True
        banned = [int(current, base) for base in range(2,11)]
        for representation in banned:
            divisor = first_divisor(representation)
            if divisor == 0:
                not_prime = False
                break
            divisors.append(divisor)
        if not_prime:
            print(current," ".join([str(x) for x in divisors]))
            J-=1
            if J==0:
                return
               
main()
