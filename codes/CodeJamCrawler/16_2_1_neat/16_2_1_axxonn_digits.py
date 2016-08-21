# Zero tWo foUr siX eiGht can be determined immediately
# then One tHree Five Seven
# then Ten nIne
t = int(raw_input())
for case in range(1, t+1):
    s = raw_input().lower()
    letters = {l : 0 for l in "abcdefghijklmnopqrstuvwxyz"}
    nums1 = { 0 : ("z", "zero"),
              2 : ("w", "two"),
              4 : ("u", "four"),
              6 : ("x", "six"),
              8 : ("g", "eight")
            }
    nums2 = { 1 : ("o", "one"),
              3 : ("h", "three"),
              5 : ("f", "five"),
              7 : ("s", "seven")
            }
    nums3 = { 9 : ("i", "nine")
            }
    nums = [nums1, nums2, nums3]
    for c in s:
        letters[c] += 1
    digits = {d : 0 for d in range(10)}
    for nums_ in nums:
        for n in nums_:
            count = letters[nums_[n][0]]
            digits[n] = count
            for c in nums_[n][1]:
                letters[c] -= count
    answer = ""
    for i in range(10):
        answer += str(i)*digits[i]
    print "Case #%d: %s" % (case, answer)
