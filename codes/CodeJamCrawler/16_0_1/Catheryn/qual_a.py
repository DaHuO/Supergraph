T = int(raw_input())
inputs = []
outputs = []
for i in range(T):
  inputs.append(int(raw_input()))

for inp in inputs:
  if inp == 0:
    ans = "INSOMNIA"
  else:
    arr = [0] * 10
    curr = 0
    while sum(arr) < 10:
      curr += inp
      digits = str(curr)
      for dig in digits:
        arr[int(dig)] = 1
    ans = curr
  outputs.append(str(ans))

for i in range(T):
  output = "Case #" + str(i + 1) + ": " + outputs[i]
  print output