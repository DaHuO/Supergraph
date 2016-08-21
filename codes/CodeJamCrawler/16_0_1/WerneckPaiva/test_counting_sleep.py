import unittest
from counting_seep.counting_sleep import counting_sheep

class TestCountingSleep(unittest.TestCase):
    
    def test_1692(self):
        r = counting_sheep(1692)
        self.assertEquals(5076, r)

    def test_0(self):
        r = counting_sheep(0)
        self.assertEquals("INSOMNIA", r)

    def test_1(self):
        r = counting_sheep(1)
        self.assertEquals(10, r)

    def test_2(self):
        r = counting_sheep(2)
        self.assertEquals(90, r)

    def test_11(self):
        r = counting_sheep(11)
        self.assertEquals(110, r)