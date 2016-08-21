file = open("C:\Users\Luca\Downloads\A-large.in", "r")
file2 = open("ans.txt", "w")
times = file.readline()

def check(alist):
    for number in range(0, 10):
        if number not in alist:
            return False
    return True

for time in range(0, int(times)):

    n = file.readline().rstrip()
    numbers = []

    if n == '0':
        a =  "Case #" + str(time + 1) + ": INSOMNIA\n"
        file2.write(a)
    else:
        i = 1
        fin_num = 0
        while not check(numbers):
            num = int(n) * i
            num_str = str(num)
            for char in range(0, len(num_str)):
                if int(num_str[char]) not in numbers:
                    numbers.append(int(num_str[char]))
                else:
                    pass
            if check(numbers):
                fin_num = num
            i += 1

        a = "Case #" + str(time + 1) + ": " + str(fin_num) + "\n"
        file2.write(a)