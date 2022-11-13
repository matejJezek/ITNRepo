from unittest import TestCase
from kalkulacka import Kalkulacka

class Test_Kalkulacka(TestCase):

    def setUp(self):
       self.kalkulacka = Kalkulacka()

    def test_mocni(self):
        self.assertEqual(4, self.kalkulacka.mocni(2, 2))
        self.assertNotEqual(5, self.kalkulacka.mocni(2, 2))

    def test_vydel(self):
        self.assertEqual(1, self.kalkulacka.vydel(2, 2))
        self.assertNotEqual(5, self.kalkulacka.vydel(2, 2))

    def test_secti(self):
        self.assertEqual(4, self.kalkulacka.secti(2, 2))
        self.assertNotEqual(5, self.kalkulacka.secti(2, 2))

    def test_odecti(self):
        self.assertEqual(0, self.kalkulacka.odecti(2, 2))
        self.assertNotEqual(5, self.kalkulacka.odecti(2, 2))
