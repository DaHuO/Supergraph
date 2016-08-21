class CoinJam(object):

    def __init__(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        outfile = open(filename + "_out", "w")
        N = int(lines[1].split(" ")[0])
        J = int(lines[1].split(" ")[1])
        result = CoinJam.find_all(N, J)
        output = "Case #1:\n" + result
        outfile.write(output + "\n")

    @staticmethod
    def find_all(N, J):
        result_string = ""
        candidate = CoinJam.get_candidate(N)
        count = 0
        for i in range(1, len(candidate) - 1):
            candidate = CoinJam.get_candidate(N)
            for j in range(i, len(candidate) - 1):
                candidate[j] = "1"
                candidate_string = "".join(candidate)
                result = CoinJam.calculate(candidate_string)
                if result is not None:
                    count += 1
                    result_string += candidate_string + " " + " ".join(result) + "\n"
                    print(candidate_string + " " + str(result))
                if count >= J:
                    return result_string

        return 0

    @staticmethod
    def get_candidate(N):
        candidate = ["0"] * N
        candidate[0] = "1"
        candidate[len(candidate) - 1] = "1"
        return candidate

    @staticmethod
    def calculate(input_str):
        divisors = []
        for base in range(2, 10 + 1):
            number = int(input_str, base)
            divisor = CoinJam.find_divisor(number)
            if divisor is None:
                return None
            else:
                divisors.append(str(divisor))
        return divisors

    @staticmethod
    def find_divisor(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i
        return None

if __name__ == '__main__':
    count = CoinJam("input")