import string
def map_alphabet():
    lookup = dict()
    for idx, letter in enumerate(string.ascii_uppercase):
        lookup[letter] = idx + 1
    return lookup

def f(lookup, word):
    word = word.upper()
    last_word = []
    last_word.append(word[0])
    for i in range(1, len(word)):
        front = last_word[0]
        current = word[i]
        if lookup[front] > lookup[current]:

            last_word.append(current)
        else:
            last_word.insert(0, current)
    return ''.join(last_word)

lookup = map_alphabet()
with open("A-large.in", "r") as ins:
    array = []
    for line in ins:
        array.append(line.rstrip())
file = open('results_large.txt', 'w')
for i in range(1, len(array)):
    result = f(lookup, array[i])
    file.write("CASE #" + str(i)+ ": " + result + "\n")
file.close()
