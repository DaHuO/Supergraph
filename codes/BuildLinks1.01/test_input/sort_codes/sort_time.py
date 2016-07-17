
from caller import Caller

class SortTime:
    
    def __init__(self):
        pass

    @staticmethod
    def times(array):
        return [ 
            Caller.bubble_sort(array=array), 
            Caller.bubble_sort_with_flag(array=array), 
            Caller.insertion_sort(array=array),
            Caller.selection_sort(array=array),
            Caller.shell_sort(array=array),
            Caller.merge_sort(array=array),
            Caller.quick_sort(array=array),
            Caller.counting_sort(array=array),
            Caller.radix_sort(array=array)
        ]
