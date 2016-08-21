import configLoader
import loadFile

def main():
    loader_config = configLoader.configLoader()
    config = loader_config.load_config("config.yml")

    file_reader = loadFile.fileLoader(config['input_file'])
    dataset = file_reader.load("input.txt")
    with open("output.txt", "w") as out_file:
        for i, data in enumerate(dataset):
            answer = s(data[0])
            answer_string = "case #{0}: {1}\n".format(str(i+1), answer)
            out_file.write(answer_string)


def s(n):
    if n == 0:
        return "INSOMNIA"
    else:
        seen = {}
        i = 1
        itn = n
        while True:
            for d in str(itn):
                seen[d] = True
            if len(seen) == 10: return str(itn)
            i += 1
            itn += n


if __name__ == "__main__":
    main()
