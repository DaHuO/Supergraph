import fileinput

small_data_set = 200
large_data_set = pow(10, 6)


def main():
    test_case = input()

    t = int(test_case)
    if not 1 <= t or not t <= 100:
        print('1 <= T <= 100')
        return

    for i in range(t):
        input_n = input()
        n = int(input_n)

        sheep_list, index = [], 1
        # counting sheep!
        while True:
            calc_sheep = str(n * index)
            for sheep in calc_sheep:
                if sheep not in sheep_list:
                    sheep_list.append(sheep)

            # check asleep
            if len(sheep_list) == 10:
                break

            # check small data set
            if len(sheep_list) < 5 and index > small_data_set:
                calc_sheep = 'INSOMNIA'
                break

            if len(sheep_list) >= 5 and index > large_data_set:
                calc_sheep = 'INSOMNIA'
                break

            # increase index
            index += 1

        print('Case #{}: {}'.format(i+1, calc_sheep))

main()

