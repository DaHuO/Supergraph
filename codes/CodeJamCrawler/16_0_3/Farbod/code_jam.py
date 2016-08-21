def passes_prime_test(a):
    a = abs(int(a))
    if a < 2:
        return True
    if a == 2:
        return False, None
    for x in range(3, int(a**0.5)+1, 2):
        if a % x == 0:
            return True, x
    return False, None


def passes_tests(string):
    proofs = []

    for base in range(2, 11):
        base_vals = {}

        for d in range(0, n):
            base_vals[str(d)] = base ** d

        total_val = 0
        for c in range(len(string)-1, -1, -1):
            #print("[log] c = {0}".format(str(c)))
            if string[c] == "1":
                total_val += base_vals[str((len(string) - 1) - c)]
                #print("[log] total = {0}".format(str(total_val)))

        print("(in base {0} is {1})".format(str(base), str(total_val)))

        passes, nonprime_proof = passes_prime_test(total_val)
        if passes:
            proofs.append(nonprime_proof)
        else:
            return None

    return proofs


reading_filename = "C-small-attempt1.in"
writing_filename = "output-small-attempt1.txt"


with open(reading_filename, "r") as file:
    contents = file.readlines()


with open(writing_filename, "w+") as file:
    tests = "1"  # contents[0] will always be 1
    print("Number of tests: {0}".format(tests))
    file.write("Case #1:\n")

    line_two = contents[1].split(" ")
    n = int(line_two[0])
    j = int(line_two[1])

    print("N: {0}".format(str(n)))
    print("J: {0}".format(str(j)))

    smallest = int("1" + ("0" * (n-2)) + "1", 2)
    #print("Smallest : {0}".format(smallest))

    # jamcoins = []

    num_jamcoins = 0

    while True:
        print("Start: {0}".format(str(num_jamcoins)))
        binary = format(smallest, "b")
        #print("--- {0}".format(binary))

        if len(binary) > n:
            #print("Digits are now more than {0}".format(str(n)))
            break
        if num_jamcoins >= j:
            #print("Length of list is more than j")
            break

        if binary[0] == "1" and binary[n-1] == "1":
            test_result = passes_tests(binary)
            if test_result is not None:
                jamcoin = {"bin": binary, "proofs": test_result}
                # jamcoins.append(jamcoin)
                num_jamcoins += 1

                string = ""
                for proof in jamcoin["proofs"]:
                    string += str(proof) + " "

                print("### {0} {1}".format(jamcoin["bin"], string))
                file.write("{0} {1}\n".format(jamcoin["bin"], string.strip()))

        smallest += 1

    print("\nValue J: {0}\n".format(str(j)))
    print("Answers - " + str(num_jamcoins))
