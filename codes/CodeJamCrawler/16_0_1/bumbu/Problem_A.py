import string

_file = open("./A-large.in")
# _file = open("./A-small-attempt0.in")
_result = open("./result.txt", "w")

datasetSize = int(_file.readline())

for i in range(datasetSize):
  number = int(_file.readline())
  digits_set = set()

  for j in range(1, 1000):
    digits = set(map(int,str(number * j)))
    digits_set = digits_set | digits

    if len(digits_set) == 10:
      break

  if j == 999:
    result = "Case #" + str(i + 1) + ": INSOMNIA"
  else:
    result = "Case #" + str(i + 1) + ": " + str(number * j)

  print result
  _result.write(result + "\n")

_file.close()
_result.close()
