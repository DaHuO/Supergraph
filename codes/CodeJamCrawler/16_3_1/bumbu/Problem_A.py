import string

_file = open("./A-large.in")
# _file = open("./A-small-attempt0.in")
_result = open("./result.txt", "w")


datasetSize = int(_file.readline())

def decrease(tuples, letter):
  count = -1
  for l, c in tuples:
    if l is letter:
      count = c

  if count <= 1:
    return filter(lambda (l, c): l is not letter, tuples)
  else:
    return map(lambda (l, c): (l, c-1) if l is letter else (l, c), tuples)

for i in range(datasetSize):
  results = []
  number = int(_file.readline())
  senators = map(int, _file.readline().replace("\n", "").split(" "))
  total = sum(senators)

  # Create tuples
  tuples = map(lambda (x, y): (chr(65 + x), y), enumerate(senators))
  print senators
  print tuples

  # Find 2 top parties
  max1 = ''
  max1Count = -1
  for letter, count in tuples:
    if max1Count < count:
      max1Count = count
      max1 = letter

  max2 = ''
  max2Count = -1
  for letter, count in tuples:
    if letter != max1 and max2Count < count:
      max2Count = count
      max2 = letter

  # Balance top 2 parties to have the same amount of senators
  while max1Count > max2Count:
    result = max1
    results.append(result)
    max1Count -= 1
    tuples = decrease(tuples, max1)

  # Evacuate all others
  while len(tuples) > 2:
    for j in range(len(tuples) - 1, -1, -1):
      if tuples[j][0] != max1 and tuples[j][0] != max2:
        results.append(tuples[j][0])
        tuples = decrease(tuples, tuples[j][0])

  # Evacuate these 2 parties in parallel
  while len(tuples) > 0:
    results.append(tuples[0][0] + tuples[1][0])
    tuples = decrease(tuples, tuples[1][0])
    tuples = decrease(tuples, tuples[0][0])

  result = "Case #" + str(i + 1) + ": " + " ".join(results)

  print result
  _result.write(result + "\n")

_file.close()
_result.close()
