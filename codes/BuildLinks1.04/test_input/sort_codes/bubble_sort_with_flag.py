
class BubbleSortWithFlag:
    
    def __init__(self):
        pass

    @staticmethod
    def sort(array):
        for i in range(0, len(array) - 1):
            changed = True
            for j in range(0, len(array) - 1 - i):
                if array[j] > array[j + 1]:
                    changed = False
                    array[j], array[j + 1] = array[j + 1], array[j]
            if changed:
                return array
        return array
