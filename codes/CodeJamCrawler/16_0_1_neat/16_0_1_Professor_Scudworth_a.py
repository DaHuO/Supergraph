import sys

#   For the last digit in the number, we can easily see the
#   digits we will get by repeatedly multiplying that number against itself
#   until we return to the beginning.

#   For digits which are not the last, we can do the same, but take into
#   account that the previous digit will overflow.

#   We can generalise this by observing the cycle of each digit.

#   But lets just do it the naive way and see what happens.
round_count = int(sys.stdin.readline())
for i in range(round_count):
    number = int(sys.stdin.readline())
    if number == 0:
        print("Case #",i+1,": INSOMNIA",sep='')
        continue
    occurence = set()
    digits_seen = 0
    multiplier = 0
    while digits_seen < 10:
        multiplier += 1
        num_as_str = str(number*multiplier)
        for digit in num_as_str:
            if digit not in occurence:
                digits_seen += 1
                occurence.update(digit)
    print("Case #",i+1,": ",number*multiplier,sep='')
