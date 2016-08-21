def get_digits(num):
    return [int(n) for n in str(num)]

def check_all_digits(lst):
    for n in range(10):
        if (n not in lst):
            return False;
    return True

def process_num(num):
    multiply = 1
    stored = []
    if (num == 0):
        return "INSOMNIA"
    while True:
        new = num * multiply;
        
        digits = get_digits(new)
        multiply += 1
        for n in digits:
            if (n not in stored):
                stored.append(n)
        if (check_all_digits(stored)):
            return new
           


if __name__ == "__main__":
    x = int(input().strip())
    for i in range(x):
        n = int(input()) 
        print("Case #" + str(i+1) + ": " + str(process_num(n)))
