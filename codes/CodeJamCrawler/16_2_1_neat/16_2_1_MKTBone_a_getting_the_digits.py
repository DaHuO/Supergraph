import fileinput
import math

# z: zero
# w: two
# u: four
# g: eight
#
# o: one
# t: three
# f: five
#
# v: seven
#
# s: six
# n: nine

nums = [[("0", "Z", "ZERO"),
         ("2", "W", "TWO"),
         ("4", "U", "FOUR"),
         ("8", "G", "EIGHT")],
        [("1", "O", "ONE"),
         ("3", "T", "THREE"),
         ("5", "F", "FIVE")],
        [("7", "V", "SEVEN")],
        [("6", "S", "SIX"),
         ("9", "N", "NINE")]]

cases = [list(s.rstrip()) for s in list(fileinput.input())[1:]]
for i, s in enumerate(cases):
    phone = ""
    for lvl in nums:
        for num in lvl:
            if len(s) == 0:
                break
            while num[1] in s:
                for d in num[2]:
                    s.remove(d)
                phone += num[0]
    assert(len(s) == 0)
    print("Case #{}: {}".format(i + 1, "".join(sorted(phone))))
