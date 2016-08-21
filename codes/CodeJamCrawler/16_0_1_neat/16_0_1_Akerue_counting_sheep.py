in_file = open('in.txt', 'rt')
number_of_cases = int(in_file.readline().strip())
results = []

for i in range(number_of_cases):
    N = int(in_file.readline().strip())
    if N == 0:
        results.append('INSOMNIA')
        continue

    digit_set = set()
    i = 1
    found_flag = False

    while True:
        current_N = N * i
        while current_N != 0:
            digit = current_N % 10
            current_N = current_N / 10
            digit_set.add(digit)
            if len(digit_set) == 10:
                found_flag = True
                break

        if found_flag is True:
            current_N = N * i
            results.append(str(current_N))
            break

        i = i + 1

for j in range(number_of_cases):
    print "Case #" + str(j+1) + ": " + results[j]