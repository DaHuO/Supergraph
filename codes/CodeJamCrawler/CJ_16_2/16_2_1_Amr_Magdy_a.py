T = int(raw_input())
mapper = [
    ("z", 0, "zero"),
    ("g", 8, "eight"),
    ("w", 2, "two"),
    ("u", 4, "four"),
    ("x", 6, "six"),
    ("o", 1, "one"),
    ("h", 3, "three"),
    ("f", 5, "five"),
    ("s", 7, "seven"),
    ("i", 9, "nine")
]

for case in range(T):
    numbers = [0] * 10
    chars = {'q':0,'w':0,'e':0,'r':0,'t':0,'y':0,'u':0,'i':0,'o':0,'p':0,'a':0,'s':0,'d':0,'f':0,'g':0,'h':0,'j':0,'k':0,'l':0,'z':0,'x':0,'c':0,'v':0,'b':0,'n':0,'m':0}
    S = raw_input().strip()
    for char in S:
        chars[char.lower()] += 1

    for item in mapper:
        if chars[item[0]] > 0:
            temp = chars[item[0]]
            numbers[item[1]] += temp
            for char in item[2]:
                chars[char] -= temp

    final_number = ""
    for number, occ in enumerate(numbers):
        for _ in range(occ):
            final_number += str(number)

    print "Case #{case}: {answer}".format(case=case+1, answer=final_number)




