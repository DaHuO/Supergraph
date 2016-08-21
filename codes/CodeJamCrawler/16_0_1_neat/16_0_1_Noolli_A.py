def solve(num,num_str):
    original_num = num
    if num == 0:
        return "INSOMNIA"

    seen = []
    counter = 1
    while len(seen) != 10:
        for i in num_str:
            if i not in seen:
                seen.append(i)
                if len(seen) == 10:
                    return num_str
        counter +=1
        num += original_num
        num_str = str(num)


def main():
    input_file = open('A-large.in', 'r')
    output_file = open('A-large.out', 'w')
    number_of_cases = int(input_file.readline().strip())
    for i in range(1,number_of_cases+1):
        num = input_file.readline().strip()
        result = solve(int(num),num)
        output_file.write("Case #"+str(i)+": " + result + "\n")

    input_file.close()
    output_file.close()

if __name__ == "__main__":
    main()