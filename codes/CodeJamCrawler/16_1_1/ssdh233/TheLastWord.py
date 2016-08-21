# when input is too large
#f = open("txt","r")
#def input():
#   return f.readline().strip()

def cal(word):
    last = ""
    for letter in word:
        if not last or letter >= last[0]:
            last = letter + last
        else:
            last = last + letter
    return last

T = int(input())
O = []

for index in range(T):
    S = input()
    O.append("Case #"+str(index+1)+": "+str(cal(S)))

for o in O:
    print(o)