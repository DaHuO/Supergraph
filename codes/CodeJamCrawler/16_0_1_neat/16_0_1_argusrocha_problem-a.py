def count_digits(number, res):
  digits = str(number)
  for digit in digits:
    res[int(digit)] |= 1

def break_condition(res):
  return all(res)

if __name__ == "__main__":
  import fileinput
  f = fileinput.input()

  total_test_cases = int(f.readline())
  for tc in range(1, total_test_cases+1):
    number = int(f.readline())
    res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if (number == 0):
      print 'Case #%d: INSOMNIA' % tc
    else:
      factor = 2
      count_digits(number, res)
      new_number = 1
      while not break_condition(res):
        new_number = number * factor
        factor += 1
        count_digits(new_number, res)

      print 'Case #%d: %d' % (tc, new_number)

