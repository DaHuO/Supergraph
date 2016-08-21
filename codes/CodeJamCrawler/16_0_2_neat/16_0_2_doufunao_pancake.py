
def flip(s):
  if s[0] == "+":
    # no start cries
    start_smile = 0
    while s[start_smile] == "+":
      start_smile += 1
    start_smile -= 1
    return "-" * start_smile + s[start_smile+1:]
    
  last_cry = len(s) - 1
  while s[last_cry] == "+":
    last_cry -= 1
  flipped = s[:last_cry+1][::-1]
  reverse = ""
  for c in flipped:
    if c == "+":
      reverse += "-"
    else:
      reverse += "+"
  return reverse + s[last_cry+1:]


def is_good(s):
  return s == '+'*len(s)


def main():
  num_of_test = int(input())

  for test_id in range(1, num_of_test + 1):
    s = raw_input()
    n = 0
    while not is_good(s):
      s = flip(s)
      n += 1
    print("Case #" + str(test_id) + ": " + str(n))

if __name__ == "__main__":
  main()

