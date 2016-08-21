import unittest
from revenge_pancakes import revenge_pancakes


class TestRevengePancakes(unittest.TestCase):
    
    def test_d(self):
        n = revenge_pancakes("-")
        self.assertEquals(1, n)

    def test_u(self):
        n = revenge_pancakes("+")
        self.assertEquals(0, n)

    def test_uuu(self):
        n = revenge_pancakes("+++")
        self.assertEquals(0, n)

    def test_ddd(self):
        n = revenge_pancakes("---")
        self.assertEquals(1, n)

    def test_ud(self):
        n = revenge_pancakes("-+")
        self.assertEquals(1, n)

    def test_ddddddud(self):
        n = revenge_pancakes("------+-")
        self.assertEquals(3, n)

    def test_dudududu(self):
        n = revenge_pancakes("-+-+-+-")
        self.assertEquals(7, n)

