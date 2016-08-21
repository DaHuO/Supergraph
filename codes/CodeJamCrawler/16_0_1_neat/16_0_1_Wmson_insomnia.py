glob_table = [0] * 10
def all_completed():
    return sum(glob_table) == 10

def insert_num(number):
    global glob_table
    for digit in str(number):
        glob_table[int(digit)] = 1

def count_to_sleep(starting_num):
    global glob_table
    glob_table = [0] * 10
    if (starting_num == 0):
        return "INSOMNIA"
    for i in range(1, 9000000):
        insert_num(starting_num * i)
        if all_completed():
            return i*starting_num
    return "INSOMNIA"


def main():
    cases = int(raw_input())
    for i in range(1,cases+1):
        print("CASE #" + str(i) + ": " + str(count_to_sleep(int(raw_input()))))

main()


