__author__ = 'OleksandrKonstantinov'

if __name__ == "__main__":

    class Mask:
        def __init__(self):
            self.arr = [0] * 10
            self.size = 10

        def mark(self, num):
            if self.arr[num] == 0:
                self.arr[num] = 1
                self.size -= 1
                return self.size == 0

            return False


    with open("A-large.in", "r") as fRead, open("result.txt", "w") as fWrite:
        T = int(fRead.readline())
        for tc in range(1, T+1):
            currStr = fRead.readline()
            num = int(currStr)
            initNum = num
            currStr = str(num)

            if num == 0:
                fWrite.write("Case #" + str(tc) + ": INSOMNIA\n")
                continue

            m = Mask()

            bStop = False
            while(True):
                for ch in currStr:

                    digit = int(ch)
                    if m.mark(digit):
                        bStop = True
                        break

                if (bStop):
                    break

                num += initNum
                currStr = str(num)

            fWrite.write("Case #" + str(tc) + ": " + str(num) + '\n')
