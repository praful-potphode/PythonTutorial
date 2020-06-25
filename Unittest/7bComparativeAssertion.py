# The second set of assertion functions are comparative asserts −
#
# 1.assertAlmostEqual (first, second, places = 7, msg = None, delta = None)
# Test that first and second are approximately (or not approximately) equal by computing the difference, rounding to the given number of decimal places (default 7),
#
# 2.assertNotAlmostEqual (first, second, places, msg, delta)
# Test that first and second are not approximately equal by computing the difference, rounding to the given number of decimal places (default 7), and comparing to zero.
#
# In both the above functions, if delta is supplied instead of places then the difference between first and second must be less or equal to (or greater than) delta.
# Supplying both delta and places raises a TypeError.
#
# 3.assertGreater (first, second, msg = None)
# Test that first is greater than second depending on the method name. If not, the test will fail.
#
# 4.assertGreaterEqual (first, second, msg = None)
# Test that first is greater than or equal to second depending on the method name. If not, the test will fail
#
# 5.assertLess (first, second, msg = None)
# Test that first is less than second depending on the method name. If not, the test will fail
#
# 6.assertLessEqual (first, second, msg = None)
# Test that first is less than or equal to second depending upon the method name. If not, the test will fail.
#
# 7.assertRegexpMatches (text, regexp, msg = None)
# Test that a regexp search matches the text. In case of failure, the error message will include the pattern and the text. regexp may be a regular expression object or a string containing a regular expression suitable for use by re.search().
#
# 8.assertNotRegexpMatches (text, regexp, msg = None)
# Verifies that a regexp search does not match text. Fails with an error message including the pattern and the part of text that matches. regexp may be a regular expression object or a string containing a regular expression suitable for use by re.search() .

import unittest
import math
import re

class SimpleTest(unittest.TestCase):
   def test1(self):
      self.assertAlmostEqual(22.0/7,3.14,places=2)
   def test2(self):
      self.assertNotAlmostEqual(10.0/3,3)
   def test3(self):
      self.assertGreater(math.pi,3)
   def test4(self):
      self.assertNotRegexpMatches("Tutorials Point (I) Private Limited","CPoint")

   def test5(self):
       self.assertGreaterEqual(9.8, 3)
   def test6(self):
      self.assertRegexpMatches("Tutorials Point (I) Private Limited","Point")

   def test7(self):
       self.assertLess(math.pi, 5)

   def test8(self):
        self.assertLessEqual(math.pi, 8)
if __name__ == '__main__':
   unittest.main()