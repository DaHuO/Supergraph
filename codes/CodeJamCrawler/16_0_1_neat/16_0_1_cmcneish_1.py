def get_digits_in_number(integer):
    string = str(integer)
    ret = []
    for i in string:
        if i not in ret:
            ret.append(i)
    return ret

def last_number_to_get_all_digits(integer):
    numbers_seen = set()
    for i in range(100):
        a = get_digits_in_number((i+1)*integer)
        numbers_seen = numbers_seen.union(set(a))
        if len(numbers_seen) >= 10:
            return (i+1)*integer
    return "INSOMNIA"

test_case_count = int(input())
for i in range(test_case_count):
    print("Case #" + str(i+1) + ": " + str(last_number_to_get_all_digits(int(input()))))

