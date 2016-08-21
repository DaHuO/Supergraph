def main():
    file = open("/home/aidan/Documents/codejam16/D-small-attempt2.in")
    outFile = open("/home/aidan/Documents/codejam16/D-small.out", "w")
    file.readline()
    for num, line in enumerate(file):
        print(line.strip())
        k, c, s = [int(x) for x in line.split()]
        outFile.write("Case #{}: {}\n".format(num + 1, " ".join([str(x) for x in range(1, k+1)])))

if __name__ == "__main__":
    main()