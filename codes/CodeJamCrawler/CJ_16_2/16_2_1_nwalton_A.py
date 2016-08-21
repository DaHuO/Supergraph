from pefuncs import digits_to_number

def list_subtract(l1, l2):
    for elem in l2:
        l1.remove(elem)
    return l1

def digits(letters):
    if "Z" in letters:
        list_subtract(letters, list("ZERO"))
        return [0] + digits(letters)
    if "G" in letters:
        list_subtract(letters, list("EIGHT"))
        return [8] + digits(letters)
    if "X" in letters:
        list_subtract(letters, list("SIX"))
        return [6] + digits(letters)
    if "W" in letters:
        list_subtract(letters, list("TWO"))
        return [2] + digits(letters)
    if "U" in letters:
        list_subtract(letters, list("FOUR"))
        return [4] + digits(letters)
    if "F" in letters:
        list_subtract(letters, list("FIVE"))
        return [5] + digits(letters)
    if "H" in letters:
        list_subtract(letters, list("THREE"))
        return [3] + digits(letters)
    if "V" in letters:
        list_subtract(letters, list("SEVEN"))
        return [7] + digits(letters)
    if "O" in letters:
        list_subtract(letters, list("ONE"))
        return [1] + digits(letters)
    if "I" in letters:
        list_subtract(letters, list("NINE"))
        return [9] + digits(letters)
    else:
        return []

def sorted_digits(letters):
    return reduce(lambda x, y: x+y, map(lambda x: str(x), sorted(digits(letters))))

i = open("input.txt", "r")
o = open("output.txt", "w")

num_cases = int(i.readline().strip())
for case in range(1, num_cases+1):
    word = i.readline().strip()
    o.write("Case #" + str(case) + ": " + sorted_digits(list(word)) + "\n")
