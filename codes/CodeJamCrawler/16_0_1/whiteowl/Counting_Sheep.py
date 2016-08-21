__author__ = 'trieu_000'


def main():
    test_case = input()
    for i in range(int(test_case)):
        n = input()
        seen_number = []
        n = int(n)
        if n > 0:
            boundary = 10
            j = 1
            while j <= boundary:
                result_list = [int(c) for c in str(j * n)]
                for item in result_list:
                    if item not in seen_number:
                        seen_number.append(item)
                        # print(seen_number)
                if len(seen_number) == 10:
                    print("Case #" + str(i + 1) +": " + str(j * n))
                    break
                elif len(seen_number) != 10 and j == boundary:
                    boundary += 10
                j += 1
        else:
            print("Case #" + str(i + 1)  +": INSOMNIA")


if __name__ == '__main__':
    main()