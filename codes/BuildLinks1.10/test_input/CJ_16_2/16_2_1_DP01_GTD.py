_name = "A-large"

# Load the file in a list
with open("{}.in".format(_name)) as f:
    data_set = [line.rstrip() for line in f]

# Remove the first entry since we don't really need it.
no_of_tests = data_set.pop(0)
current_test_no = 1

mapping = {"ZERO": "0",
           "ONE": "1",
           "TWO": "2",
           "THREE": "3",
           "FOUR": "4",
           "FIVE": "5",
           "SIX": "6",
           "SEVEN": "7",
           "EIGHT": "8",
           "NINE": "9"
           }

def find_unique_number(no):
    _number = []

    if "Z" in no:
        while "Z" in no:
            _temp = []
            _temp.append(no.pop(no.index("Z")))
            _temp.append(no.pop(no.index("E")))
            _temp.append(no.pop(no.index("R")))
            _temp.append(no.pop(no.index("O")))
            _number.append(''.join(_temp))

    if "W" in no:
        while "W" in no:
            _temp = []
            _temp.append(no.pop(no.index("T")))
            _temp.append(no.pop(no.index("W")))
            _temp.append(no.pop(no.index("O")))
            _number.append(''.join(_temp))

    if "U" in no:
        while "U" in no:
            _temp = []
            _temp.append(no.pop(no.index("F")))
            _temp.append(no.pop(no.index("O")))
            _temp.append(no.pop(no.index("U")))
            _temp.append(no.pop(no.index("R")))
            _number.append(''.join(_temp))

    if "F" in no:
        while "F" in no:
            _temp = []
            _temp.append(no.pop(no.index("F")))
            _temp.append(no.pop(no.index("I")))
            _temp.append(no.pop(no.index("V")))
            _temp.append(no.pop(no.index("E")))
            _number.append(''.join(_temp))

    if "X" in no:
        while "X" in no:
            _temp = []
            _temp.append(no.pop(no.index("S")))
            _temp.append(no.pop(no.index("I")))
            _temp.append(no.pop(no.index("X")))
            _number.append(''.join(_temp))

    if "O" in no:
        while "O" in no:
            _temp = []
            _temp.append(no.pop(no.index("O")))
            _temp.append(no.pop(no.index("N")))
            _temp.append(no.pop(no.index("E")))
            _number.append(''.join(_temp))

    if "G" in no:
        while "G" in no:
            _temp = []
            _temp.append(no.pop(no.index("E")))
            _temp.append(no.pop(no.index("I")))
            _temp.append(no.pop(no.index("G")))
            _temp.append(no.pop(no.index("H")))
            _temp.append(no.pop(no.index("T")))
            _number.append(''.join(_temp))

    if "V" in no:
        while "V" in no:
            _temp = []
            _temp.append(no.pop(no.index("S")))
            _temp.append(no.pop(no.index("E")))
            _temp.append(no.pop(no.index("V")))
            _temp.append(no.pop(no.index("E")))
            _temp.append(no.pop(no.index("N")))
            _number.append(''.join(_temp))

    if "N" in no:
        while "N" in no:
            _temp = []
            _temp.append(no.pop(no.index("N")))
            _temp.append(no.pop(no.index("I")))
            _temp.append(no.pop(no.index("N")))
            _temp.append(no.pop(no.index("E")))
            _number.append(''.join(_temp))

    if "H" in no:
        while "H" in no:
            _temp = []
            _temp.append(no.pop(no.index("T")))
            _temp.append(no.pop(no.index("H")))
            _temp.append(no.pop(no.index("R")))
            _temp.append(no.pop(no.index("E")))
            _temp.append(no.pop(no.index("E")))
            _number.append(''.join(_temp))

    return _number

for s in data_set:
    _solved = False
    phone_number = []

    s  = list(s)

    _number = find_unique_number(s)

    for i in _number:
        phone_number.append(mapping[i])

    phone_number.sort()
    phone_number = "".join(phone_number)

    with open("{}.out".format(_name), 'a') as f:
        f.write("Case #{0}: {1}\n".format(current_test_no, phone_number))

    current_test_no += 1
