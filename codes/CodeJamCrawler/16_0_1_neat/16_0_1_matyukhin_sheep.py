def markDigits(number, digits):
  while number:
    digit = number % 10
    digits[digit] = True
    number //= 10

def isTimeToSleep(digits):
  for marked in digits:
    if not marked:
      return False
  return True

numbers = []

with open("input.txt", "r") as inputFile:
  inputFile.readline()
  for line in inputFile:
    numbers.append(int(line))

with open("output.txt", "w") as outputFile:
  case = 1
  for number in numbers:
    if number == 0:
      outputFile.write("Case #{}: {}\n".format(case, "INSOMNIA"))
    else:
      digits = [False for i in range(1, 10 + 1)]
      N = 0
      while not isTimeToSleep(digits):
        N += 1
        markDigits(number * N, digits)
      outputFile.write("Case #{}: {}\n".format(case, number * N))
    case += 1
