import copy
numbermap = {
    1: {'O': 1, 'N': 1, 'E': 1},
    2: {'T': 1, 'W': 1, 'O': 1},
    3: {'T': 1, 'H': 1, 'R': 1, 'E': 2},
    4: {'F': 1, 'O': 1, 'U': 1, 'R': 1},
    5: {'F': 1, 'I': 1, 'V': 1, 'E': 1},
    6: {'S': 1, 'I': 1, 'X': 1},
    7: {'S': 1, 'E': 2, 'V': 1, 'N': 1},
    8: {'E': 1, 'I': 1, 'G': 1, 'H': 1, 'T': 1},
    9: {'N': 2, 'I': 1, 'E': 1},
    0: {'Z': 1, 'E': 1, 'R': 1, 'O': 1}
}

def print_solution(trial, sol):
    formatted_sol = ''
    for i, digit in enumerate(sol):
        formatted_sol += str(i) * sol[digit]
    print "Case #{}: {}".format(trial, formatted_sol)

def digit_exists(digit, letters):
    digit_chars = numbermap[digit]
    for c in digit_chars:
         new_letters[c] 

def readd_digit(d, letters):
    for c in numbermap[d]:
        letters[c] += numbermap[d][c]
    
def get_digit_count(d, letters):
    digit_count = 0
    while True:
        #print 'd: ', d, 'letters: ', letters
        for c in numbermap[d]:
            if c not in letters:
                #print 'c not in letters: ', c
                return (digit_count, letters)
            if letters[c] < 0:
                readd_digit(d, letters)
                return (digit_count - 1, letters)
        for c in numbermap[d]:
            letters[c] -= numbermap[d][c]
        digit_count += 1
    
def handle_case(trial):
    x = raw_input()
    letters = {}
    for l in x:
        letters[l] = letters.get(l, 0) + 1
    digit_counts = {}
    for digit in [0, 8, 6, 2, 3, 4, 5, 7, 9, 1]:
        digit_count, letters = get_digit_count(digit, letters)
        digit_counts[digit] = digit_count
    
    print_solution(trial, digit_counts)
    
    
def main():
    n = int(raw_input())
    for i in range(n):
        handle_case(i+1)

if __name__ == "__main__":
    main()
    
