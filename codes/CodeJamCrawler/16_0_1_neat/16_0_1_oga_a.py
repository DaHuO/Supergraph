digits = set()

def main():
  num_of_input = int(input())
  ns = [int(input()) for i in range(0, num_of_input)]
  result = [""] * num_of_input
  for index, n in enumerate(ns):
    digits.clear()
    for i in range(1, 1000000):
      val = str(i * n)
      for c in val:
        digits.add(c)
      if len(digits) == 10:
        result[index] = "Case #%i: %s\n" %(index + 1, val)
        break
    else:
      result[index] = "Case #%i: %s\n" %(index + 1, 'INSOMNIA')
  print("".join(result))

main()
