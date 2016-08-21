def solve(s):
    pre_all_words = [""]
    for letter in s:
        new_all_words = []
        for word in pre_all_words:
            new_all_words.append(word + letter)
            new_all_words.append(letter + word)
        pre_all_words = new_all_words

    return sorted(pre_all_words)[-1]



def main():
    input_file = open('A-small-attempt0.in', 'r')
    output_file = open('A-small.out', 'w')
    number_of_cases = int(input_file.readline().strip())
    for i in range(1,number_of_cases+1):
        s = input_file.readline().strip()
        result = solve(s)
        print result
        output_file.write("Case #"+str(i)+": " + result + "\n")

    input_file.close()
    output_file.close()
    # print solve("ZXCASDQWE") == "ZXCASDQWE"


if __name__ == "__main__":
    main()