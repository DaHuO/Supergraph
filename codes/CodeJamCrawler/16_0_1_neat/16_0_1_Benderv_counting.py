import itertools

all_numbers = {
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
}

def sheeps(n):
    if n == 0:
        return "INSOMNIA"
    i = 0
    viewed = set()
    while viewed != all_numbers:
        i += 1
        viewed |= set(str(i*n))
    return i*n

t = int(input())

for i in range(t):
  line = int(input().strip())
  print("Case #{}: {}".format(i + 1, sheeps(line)))