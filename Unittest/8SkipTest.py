# Support for skipping tests has been added since Python 2.7.
# It is possible to skip individual test method or TestCase class, conditionally as well as unconditionally.
# The framework allows a certain test to be marked as an 'expected failure'.
# This test will 'fail' but will not be counted as failed in TestResult.
# To skip a method unconditionally, the following unittest.skip() class method can be used −
#
#
# Since   skip()   is   a  class  method,   it   is   prefixed   by   @   token.
# The   method   takes   one   argument: a   log   message   describing   the   reason  for   the   skip.
# 1	unittest.skip(reason)
# Unconditionally skip the decorated test. reason should describe why the test is being skipped.
#
# 2	unittest.skipIf(condition, reason)
# Skip the decorated test if condition is true.
#
# 3	unittest.skipUnless(condition, reason)
# Skip the decorated test unless condition is true.
#
# 4	unittest.expectedFailure()
# Mark the test as an expected failure. If the test fails when run, the test is not counted as a failure.

import unittest


class suiteTest(unittest.TestCase):
    a = 50
    b = 40

    def testadd(self):
        """Add"""
        result = self.a + self.b
        self.assertEqual(result, 100)

    @unittest.skipIf(a > b, "Skip over this routine")
    def testsub(self):
        """sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)

    @unittest.skipUnless(b == 0, "Skip over this routine")
    def testdiv(self):
        """div"""
        result = self.a / self.b
        self.assertTrue(result ==1)

    @unittest.expectedFailure
    def testmul(self):
        """mul"""
        result = self.a * self.b
        self.assertEqual(result , 0)

    @unittest.skip("Skipping Mod Functions")
    def testmod(self):
        """mod"""
        result = self.a % self.b
        self.assertEqual(result , 0)

if __name__ == '__main__':
    unittest.main()