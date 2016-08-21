__author__ = 'Hunter'

f = open("B-large.in", "r")

pancakes = f.readlines()
pancakes.pop(0)
pancakes = [x.strip() for x in pancakes]
ncases = len(pancakes)

print(pancakes)
print(ncases)

f.close()

for i in range (len(pancakes)):
    flip_count = 0
    seeker = "+"
    changer = "-"
    if not "-" in pancakes[i]:
        print("CASE #" + str(i+1) + ": 0")
        continue
    if not "+" in pancakes[i]:
        print("CASE #" + str(i+1) + ": 1")
        continue
    j = 0
    max_idx = len(pancakes[i])
    while j < max_idx:
        if pancakes[i][j] == seeker or j == 0 or (j > 0 and pancakes[i][j-1] == "+"):
            for k in range (j, len(pancakes[i])):
                if pancakes[i][k] == changer or k == len(pancakes[i])-1:
                    pancakes[i] = pancakes[i][0:j] + changer*(k-j) + pancakes[i][k:len(pancakes[i])]
                    if k > 0:
                        flip_count += 1
                    for m in range (k, len(pancakes[i])):
                        if pancakes[i][m] == seeker or m == len(pancakes[i])-1:
                            pancakes[i] = pancakes[i][0:j] + seeker*(m-j) + pancakes[i][m:len(pancakes[i])]
                            flip_count += 1
                            j = m+1
                            break
                    break
        if "-" not in pancakes[i]:
            break
    print("CASE #" + str(i+1) + ": " + str(flip_count))
