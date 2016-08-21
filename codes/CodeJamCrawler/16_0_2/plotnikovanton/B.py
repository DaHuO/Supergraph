number_of_cases = int(input())

for i in range(number_of_cases):
    print('Case #{}: '.format(i+1), end='')
    data = input()
    last_minus = data.rfind('-')
    if last_minus == -1:
        print(0)
    else:
        data = data[:last_minus + 1]
        num_of_clust = 1
        prev = data[0]
        for c in data:
            if c != prev:
                num_of_clust += 1
            prev = c
        print(num_of_clust)
