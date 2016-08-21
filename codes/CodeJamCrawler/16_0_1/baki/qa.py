
def get_digits(x):
    digit_string = str(x)
    digits = set()
    for digit in digit_string:
        digits.add(int(digit))
    return digits

def main():
    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        if n == 0:
            print ("Case #"+str(t)+": INSOMNIA")
            continue

        x = 0
        digits = list(range(0,10))
        while digits:
            x += n
            # get the digits of x
            for d in get_digits(x):
                if d in digits:
                    digits.remove(d)
        print ("Case #"+str(t)+": "+str(x))


main()