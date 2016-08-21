def cgj_frame():
  CASE_N = int(input())
  for i in range(CASE_N):
    row = input()
    print("Case #%d: %s" % (i+1, sol(row)))

def sol(row):
  mask = 0
  count = len(row)
  for face in row[::-1]:
    if (ord(face) ^ mask == ord('+')):
      count -= 1
    else:
      mask ^= 0x6

  return count

cgj_frame()