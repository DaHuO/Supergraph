def sequency(input_str, test_counter):
    current = input_str[0]
    count = 0

    for each in input_str[1:]:
        if each is not current:
            count += 1
            current = each

    if input_str[::-1][0] == '-':
        count += 1

    print("Case #%s: %s" % (str(test_counter+1), str(count)))

test_cases = int(input())

for t in range(test_cases):
    S = str(input())
    sequency(S, t)