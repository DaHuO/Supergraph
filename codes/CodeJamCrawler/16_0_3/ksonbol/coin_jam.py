file_name = "C-large.in"

def inc(binary):
    if binary.count("0") == 0:
        raise ValueError("This is largest binary of this length")
    if binary[-1] == "0": 
        return binary[:-1] + "1" 
    else:
        return inc(binary[:-1]) + "0"

def increment(new_coin):
    sliced = new_coin[1:-1]
    return "1" + inc(sliced) + "1"

def get_next_coin(n, coin):
    if not coin:
        return "1" + "0" * (n-2) + "1"
    return increment(coin)

def to_decimal(coin, base):
    decimal = 0
    length = len(coin)
    reverse = coin[::-1]
    for i in range(0, length):
        decimal += int(reverse[i]) * (base ** i)
    return decimal

def single_base_prime(coin, base):
    decmial_coin = to_decimal(coin, base)
    for divisor in range(2, 51):
        if decmial_coin % divisor == 0:
            return False, divisor
    # Otherwise, it's not worth it, we should just try another number
    return True, None
    
def all_base_not_prime(coin):
    # divisors > list of strings
    divisors = []
    for base in range(2, 11):
        is_prime, divisor = single_base_prime(coin, base)
        if is_prime: return False, None
        divisors.append(str(divisor))
    return True, divisors

with open(file_name, "r") as r:
    num_cases = r.readline()
    case = r.readline().strip().split()
    n, j = [int(x) for x in case]
    jam_coins = []
    answers = []
    new_coin = None
    for i in range(j):
        while True:
            new_coin = get_next_coin(n, new_coin)
            is_all_base_not_prime, divisors = all_base_not_prime(new_coin)
            if is_all_base_not_prime: 
                jam_coins.append(new_coin)
                answers.append((new_coin, divisors))
                break

with open("out.txt", "w") as w:
    w.write("Case #1:\n")
    for jam_coin, divisors in answers:
        # divisors must be a list of strings
        divisors_str = " ".join(divisors)
        w.write("{} {}\n".format(jam_coin, divisors_str))
