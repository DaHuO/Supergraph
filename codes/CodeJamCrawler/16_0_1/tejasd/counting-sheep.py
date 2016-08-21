# Google Code Jam 2016
# Qualification - Counting Sheep
# Tejas Deshpande - tejasd
# 04/09/2016

def get_last_number(initial_number):
    if initial_number == 0:
        return 'INSOMNIA'
    else:
        current_number = initial_number
        visited_numbers = [0] * 10
        multiplier = 2
        while(True):
            for number in list_of_digits(current_number):
                visited_numbers[number] = 1
            if did_fall_asleep(visited_numbers):
                return str(current_number)
            else:
                current_number = initial_number * multiplier
                multiplier = multiplier + 1


def list_of_digits(number):
    return map(int, list(str(number)))

def did_fall_asleep(visited_numbers):
    for result in visited_numbers:
        if result == 0:
            return False
    return True


if __name__ == "__main__":
    num_test_cases = input()
    for i in range(int(num_test_cases)):
        number = input()
        print('Case #' + str(i+1) + ': ' + get_last_number(int(number)))
