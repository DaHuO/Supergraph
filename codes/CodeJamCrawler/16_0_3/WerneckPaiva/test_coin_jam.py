import unittest
from coin_jam import first_divisor, coin_jam, toBase


class TestCoinJam(unittest.TestCase):
    def test_is_prime_1(self):
        self.assertEquals(0, first_divisor(1))

    def test_is_prime_0(self):
        self.assertEquals(0, first_divisor(0))

    def test_is_prime_2(self):
        self.assertEquals(0, first_divisor(2))

    def test_is_prime_3(self):
        self.assertEquals(0, first_divisor(3))

    def test_is_prime_4(self):
        self.assertEquals(2, first_divisor(4))

    def test_is_prime_10(self):
        self.assertEquals(2, first_divisor(10))
        
    def test_is_prime_9(self):
        self.assertEquals(3, first_divisor(9))

    def test_is_prime_11(self):
        self.assertEquals(0, first_divisor(11))

    def test_toBase_1_2(self):
        self.assertEquals(1, toBase('1', 2))

    def test_toBase_10_2(self):
        self.assertEquals(2, toBase('10', 2))

    def test_toBase_1001_2(self):
        self.assertEquals(9, toBase('1001', 2))

    def test_toBase_1001_3(self):
        self.assertEquals(28, toBase('1001', 3))

    def test_toBase_10_7(self):
        self.assertEquals(7, toBase('10', 7))

    def test_coin_jam(self):
        result = coin_jam(4, 1)
        self.assertTrue('1001' in result)

    def test_coin_jam_6_3(self):
        result = coin_jam(6, 3)
        self.assertTrue('100001' in result)
        self.assertTrue('100111' in result)
        self.assertTrue('100111' in result)

    def test_coin_jam_16_50(self):
        result = coin_jam(16, 50)
        self.assertEquals(50, len(result))
