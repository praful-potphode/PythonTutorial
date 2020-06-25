# Python testing framework uses Python's built-in assert() function which tests a particular condition. If the assertion fails, an AssertionError will be raised. The testing framework will then identify the test as Failure. Other exceptions are treated as Error.
#
# The following three sets of assertion functions are defined in unittest module −
#
# Basic Boolean Asserts
# Comparative Asserts
# Asserts for Collections
#
# Basic     assert functions     evaluate     whether     the     result     of     an     operation is True or False.
# All     the     assert methods     accept     a     msg     argument     that,
# if specified, is used as the error message on failure.
#
# 1	assertEqual(arg1, arg2, msg = None)
# Test that arg1 and arg2 are equal. If the values do not compare equal, the test will fail.
#
# 2	assertNotEqual(arg1, arg2, msg = None)
# Test that arg1 and arg2 are not equal. If the values do compare equal, the test will fail.
#
# 3	assertTrue(expr, msg = None)
# Test that expr is true. If false, test fails
#
# 4	assertFalse(expr, msg = None)
# Test that expr is false. If true, test fails
#
# 5	assertIs(arg1, arg2, msg = None)
# Test that arg1 and arg2 evaluate to the same object.
#
# 6	assertIsNot(arg1, arg2, msg = None)
# Test that arg1 and arg2 don’t evaluate to the same object.
#
# 7	assertIsNone(expr, msg = None)
# Test that expr is None. If not None, test fails
#
# 8	assertIsNotNone(expr, msg = None)
# Test that expr is not None. If None, test fails
#
# 9	assertIn(arg1, arg2, msg = None)
# Test that arg1 is in arg2.
#
# 10	assertNotIn(arg1, arg2, msg = None)
# Test that arg1 is not in arg2.
#
# 11	assertIsInstance(obj, cls, msg = None)
# Test that obj is an instance of cls
#
# 12	assertNotIsInstance(obj, cls, msg = None)
# Test that obj is not an instance of cls


import unittest

class SimpleTest(unittest.TestCase):
    # Using   assertEqual   the   two   objects   need      not   be   of   the   same   type,   they   merely   need
    # to   be   the   same   value.   In   comparison,   using   assertIs   the   two   objects   need   to   be   the
    # same   object.assertEqual   tests       for   equality   like   the  = =   operator:
    # The   operators   <,   >,  = =,   >=,   <=,   and   !=   compare   the   values   of   two   objects.
    # The   objects   need      not   have   the   same   type.   If   both   are   numbers,
    # they   are   converted   to   a   common   type.
    # Otherwise,   objects   of   different   types   always   compare   unequal,   and   are   ordered   consistently
    # but   arbitrarily.
   
   def test1(self):
      self.assertEqual(4 + 5,9)
   def test2(self):
      self.assertNotEqual(5 * 2,11)
   def test3(self):
      self.assertTrue(4 + 5 == 9,"The result is False")
   def test4(self):
      self.assertFalse(4 + 5 == 10,"assertion fails")
   def test5(self):
      self.assertIn(3,[1,2,3])
   def test6(self):
      self.assertNotIn(3, range(5,10))

    # assertIs   test   for   object   identity   same   as   the   is   and   is   not   operators:
    # The   operators   is   and   is   not   test       for   object   identity:
    # x   is   y   is   true   if   and   only   if   x   and   y   are   the   same   object.
    #   x   is   not   y   yields   the   inverse   truth   value.
   def test7(self):
       self.assertIs(4,4,"assertion fails")

   def test8(self):
       self.assertIsNot(4, 5, " assertIsNot assertion fails")

   def test9(self):
       self.assertIsNone(None, " assertIsNone assertion fails")

   def test10(self):
        self.assertIsInstance(5,int, " assertIsNone assertion fails")

   def test11(self):
        self.assertNotIsInstance(4.0,int, " assertIsNone assertion fails")

   def test12(self):
        self.assertIsNotNone(4.0, " assertIsNone assertion fails")
if __name__ == '__main__':
   unittest.main()