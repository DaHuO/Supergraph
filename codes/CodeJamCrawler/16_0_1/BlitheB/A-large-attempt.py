def counting_sheep(n):
    result = []
    i = 1
    if result is None:
        result = []
    if n == 0:
        return "INSOMNIA"

    while len(result) < 10:

        num_to_check = n * i

        for c in str(num_to_check):
            if c not in result:
                result.append(c)

        i += 1

    return num_to_check

test_cases = int(input())
for tc in range(test_cases):
    result_txt = "Case #" + str(tc+1) + ": "
    print(result_txt, counting_sheep(int(input())),sep="")
