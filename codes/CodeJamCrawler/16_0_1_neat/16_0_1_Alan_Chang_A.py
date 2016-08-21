# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

def compute():
    N = int(input())

    if N == 0:
        return "INSOMNIA"

    seen_digit = [False] * 10
    num_digits_seen = 0

    curr_multiple = 0
    
    while num_digits_seen < 10:
        curr_multiple += N
        digits = map(int, str(curr_multiple))
        for i in digits:
            if (not seen_digit[i]):
                seen_digit[i] = True
                num_digits_seen += 1


    return str(curr_multiple)

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + compute())
