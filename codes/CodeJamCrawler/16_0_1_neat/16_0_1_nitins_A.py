tests = int(input())

def check(counter):
    for i in range(10):
        if counter[i] == 0:
            return False
    return True

test_count = 0
while test_count < tests:
    test_count += 1

    it_num = int(input())

    counter = [0 for i in range(10)]

    i = 1
    curr_val = it_num
    while((i < 900)):
        if(it_num == curr_val and i > 1):
            break

        while(curr_val > 0):
            digit = int(curr_val%10)
            curr_val = int(curr_val/10)
            counter[digit] = 1

        if check(counter):
            break
        i += 1
        curr_val = i * it_num

    if check(counter):
        print("Case #{}: {}".format(test_count,(i) * it_num))
    else:
        print("Case #{}: INSOMNIA".format(test_count))
