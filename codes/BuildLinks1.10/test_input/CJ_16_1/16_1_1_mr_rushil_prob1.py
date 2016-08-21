import sys
input_data = sys.stdin.readlines()

num_cases = input_data[0]

for case in range(1, len(input_data)):
    s = input_data[case].replace("\n","")
    answer = s[0]
    for letter in range(1,len(s)):
        if s[letter] >= answer[0]:
          answer = s[letter] + answer
        else:
          answer = answer + s[letter]
    print "Case #"+str(case)+": "+answer