import leapyear
import unittest



class test_leapyear(unittest.TestCase):
  def test_average1(self):
    year = 2016
    self.assertEqual(leapyear.leapyear(year), True)
  def test_average2(self):
    year = 2000
    self.assertEqual(leapyear.leapyear(year), True)
  def test_average3(self):
    year = 2001
    self.assertEqual(leapyear.leapyear(year), False)