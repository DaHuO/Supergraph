def scan_pancakes(pancakes, start):
    count = 0
    while True:
        if pancakes[start] == "+":
            count += 1
            pancakes = flip(pancakes, start)
        if start == 0:
            count += 1
            pancakes = flip(pancakes, len(pancakes)-1)
            break
        start = start - 1
    return count

def flip(pancakes, start):
    for i in range(0, start+1):
        if pancakes[i] == "-":
            pancakes[i] = "+"
        else:
            pancakes[i] = "-"
    return pancakes

def main(pancakes):
    pancakes = list(pancakes)
    start = 0
    for i in range(len(pancakes)-1,-1,-1):
        if pancakes[i] == "-":
            start = i
            break
        elif i == 0:
            return 0
    count = scan_pancakes(pancakes, start)
    return count

with open("B-large.in", "r") as f:
    array = []
    for line in f:
        array.append(line)

output = open("result_large.txt", "w")
for i in range(1, len(array)):
    result = str(main(array[i]))
    output.write("CASE #" +  str(i) +  ": " + result + "\n")


