import math

class Jamcoin:

    def isPrime(self, number):
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    def getDivisor(self, number):
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return i
        return None

    def calculateBaseConvertions(self, number):
        base_numbers = []
        for i in range(2, 11):
            converted_number = int(str(number), i)
            if self.isPrime(converted_number):
                return None
            base_numbers.append(converted_number)
        return base_numbers

    def getProof(self, base_list):
        proof = []
        for base_num in base_list:
            divisor = self.getDivisor(base_num)
            if divisor is None:
                return None
            proof.append(divisor)
        return proof

    def generateJamCoins(self, size, quantity):
        jamcoins = {}
        for i in range(1, int(math.pow(2, size - 2))):
            bits = bin(i)[2:].zfill(size - 2)
            tmp_jamcoin = '1' + bits + '1'
            base_list = self.calculateBaseConvertions(tmp_jamcoin)
            if base_list is None:
                continue
            proofs = self.getProof(base_list)
            if proofs is None:
                continue
            jamcoins[tmp_jamcoin] = proofs
            string_proofs = ' '.join(map(str, proofs))
            print("%s %s" % (tmp_jamcoin, string_proofs))
            if len(jamcoins) == quantity:
                return jamcoins

    def __init__(self):
        file = open('input', 'r')
        T = int(file.readline())
        testcase_number = 1
        for line in file:
            print("Case #%s:" % testcase_number)
            N, J = line.split(' ')  # N size J numer of jamcoins
            result = self.generateJamCoins(int(N), int(J))
            # for k, v in result.items():
            #     print(k, v)
            testcase_number = testcase_number + 1

atm = Jamcoin()