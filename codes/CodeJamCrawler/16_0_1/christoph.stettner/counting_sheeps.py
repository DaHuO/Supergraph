

def calc(testcase, chosen_number):
  i = 0
  return_value = 0
  numbers_found = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  # print chosen_number
  if chosen_number == 0:
    output =  "Case #" + str(testcase) + ": INSOMNIA\n"
    output_file.write(output)
    return

  while numbers_found[1:] != numbers_found[:-1]:
    i += 1
    # print "i: " + str(i)
    return_value = x = chosen_number * i
    while x:
      digit = x % 10
      numbers_found[digit] = "x"
      x //= 10
    # print numbers_found


  output =  "Case #" + str(testcase) + ": " + str(return_value) + "\n"
  output_file.write(output)


input_file = open('/Users/cstettner/Projects/code-jam/2016/counting_sheeps_large.in', 'r')
output_file = open('/Users/cstettner/Projects/code-jam/2016/counting_sheeps_large.out', 'w')

no_test_cases = input_file.readline()
testcase = 1

for tc in range(1, int(no_test_cases) + 1):
  chosen_number = int(input_file.readline())

  calc(testcase, chosen_number)
  testcase += 1
