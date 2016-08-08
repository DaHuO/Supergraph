
class RadixSort:

    def __init__(self):
        pass

    @staticmethod
    def sort(array):

        radix = 10
        max_size = False
        temp, placement = -1, 1

        while not max_size:
            max_size = True
            buckets = [list() for _ in range(radix)]

            for i in array:
                temp = i // placement
                buckets[temp % radix].append(i)
                if max_size and temp > 0:
                    max_size = False

            a = 0

            for b in range(radix):
                bucket = buckets[b]
                for i in bucket:
                    array[a] = i
                    a += 1

            placement *= radix
        return array
