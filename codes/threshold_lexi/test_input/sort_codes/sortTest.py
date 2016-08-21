from Sort import *
import jarray
import java.lang.Integer
import unittest
import random
import inspect

METHODS = [insertSort, shellSort, mergeSort]#, quickSort]

class SortTest(unittest.TestCase):
    '''Unit tests for Sort.java class'''

    def _helper(self, array):
        '''Runs all of the algorithms with the given array'''
        sortedArray = array[:]
        sortedArray.sort()
        jArray = jarray.array(sortedArray, java.lang.Integer)
        for method in METHODS:
            arrayCopy = jarray.array(array, java.lang.Integer)
            method(arrayCopy)
            self.assertEqual(jArray, arrayCopy, "Failed method %s during %s" % 
                             (method.__name__, inspect.stack()[1][3]))
    
    def testEmpty(self):
        '''Tests algorithms for empty list'''
        self._helper(list())
        
    def testSorted(self):
        '''Tests algorithms for sorted list'''
        self._helper([i for i in range(10)])
     
    def testReverse(self):
        '''Tests algorithms for list in reverse order'''
        self._helper([i for i in range(10,0,-1)])        
        
    def testRandom(self):
        '''Tests algorithms for list in random order'''
        self._helper([random.randint(java.lang.Integer.MIN_VALUE, java.lang.Integer.MAX_VALUE) for x in range(1000)])
        
            
        