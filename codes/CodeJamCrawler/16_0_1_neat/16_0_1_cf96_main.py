def count_sheep(number):
    bucket = {}
    if number == 0:
        return -1

    last_number = number
    n = 1

    while bucket.__len__() < 10:
        last_number = number * n
        for char in str(last_number):
            bucket[char] = True

        n+=1

    return last_number

def main():
    with open('data.in', "r") as data:

        out_file = open("data.out", "w")

        num_cases = int(data.readline())
        for i in range(num_cases):
            result = count_sheep(int(data.readline()))
            out_file.writelines("Case #%d: %s\n" % (i+1, "INSOMNIA" if result == -1 else str(result)))

if __name__ == "__main__":
    main()
