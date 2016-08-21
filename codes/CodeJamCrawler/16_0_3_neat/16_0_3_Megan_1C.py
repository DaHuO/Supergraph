import fileinput
import math

def interpret_num(num, base):
    value = 0
    n = len(num)
    for i in range(len(num)):
        value+= num[i] * math.pow(base, n - i - 1)
    return int(value)



i = 0
num_cases = -1
num_results = 0
for line in fileinput.input():
    if (i == 0):
        num_cases = int(line)
    else:
        nums = line.split()
        n = int(nums[0])
        j = int(nums[1])

        print "Case #" + str(i) + ":"


        num = [0 for o in range(n)]
        num[0] = 1
        num[n-1] = 1

        for m in range (int(math.pow(2, n -2))):
            is_jam = True
            result = [0 for l in range(9)]
            for k in range(2, 11):
                divisor = 2
                num_interpreted = interpret_num(num, k)
                found_divisor = False
                while(divisor < num_interpreted and divisor < 1000):
                    if num_interpreted % divisor == 0:
                        result[k-2] = divisor
                        found_divisor = True
                        break
                    divisor += 1
                if not found_divisor:
                    is_jam = False
                    break

            if is_jam:
                string_result = ""
                for value in num:
                    string_result += str(value)
                for value in result:
                    string_result += " " + str(value)
                print string_result
                num_results += 1
                if num_results >= j:
                    break


            increased = False
            index = n - 2
            while not increased:
                if (num[index] == 0):
                    num[index] = 1
                    increased = True
                else:
                    num[index] = 0
                index -= 1
                if index < 0:
                    break





           


    i+=1
    if (i > num_cases):
        break