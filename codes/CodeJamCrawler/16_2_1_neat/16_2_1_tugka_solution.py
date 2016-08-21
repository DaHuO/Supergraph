import sys

def read_case(line):
    return list(line.strip())


def make_solution(letters):
    numbers = [(0, "ZERO", "Z"), (2, "TWO", "W"),(6, "SIX", "X"),(7, "SEVEN", "S"), (5, "FIVE", "V"),
               (4, "FOUR", "F"),(1, "ONE", "O"),(9, "NINE", "N"), (3, "THREE", "R"), (8, "EIGHT", "H"),]

    def delete_first_occurrence(list_of_letters, letters_to_delete):
        for w in letters_to_delete:
            first_index = [i for i, l in enumerate(list_of_letters) if l == w][0]
            list_of_letters = [l for i, l in enumerate(list_of_letters) if i != first_index]
        return list_of_letters

    numbers_found = []
    for num, word, id in numbers:
        while(True):
            if id not in letters:
                break
            numbers_found.append(num)
            letters = delete_first_occurrence(letters, word)

    numbers_found = sorted(numbers_found)
    return "".join([str(n) for n in numbers_found])


if __name__ == "__main__":
    f = sys.stdin
    #f = open("samples.text")
    count = int(f.readline())
    for c in range(count):
        case = read_case(f.readline())
        solution = make_solution(case)
        print("Case #{}: {}".format(c+1, solution))
