import configLoader
import loadFile
import math
import itertools

def main():
    loader_config = configLoader.configLoader()
    config = loader_config.load_config("config.yml")

    file_reader = loadFile.fileLoader(config['input_file'])
    dataset = file_reader.load("input.txt")
    with open("output.txt", "w") as out_file:
        for i, data in enumerate(dataset):
            print "data: ", data
            answer = create_answer(data[0][0], data[0][2])
            answer_str = "case #{0}: {1}\n".format(i+1, answer)
            out_file.write(answer_str)


def create_answer(k, s):
   return " ".join([str(x) for x in xrange(1,k+1)])

if __name__ == "__main__":
    main()
