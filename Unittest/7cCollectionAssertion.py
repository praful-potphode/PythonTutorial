# This set of assert functions are meant to be used with collection data types in Python, such as List, Tuple, Dictionary and Set.
# 1 assertListEqual (list1, list2, msg = None)
# Tests that two lists are equal. If not, an error message is constructed that shows only the differences between the two.
#
# 2 assertTupleEqual (tuple1, tuple2, msg = None)
# Tests that two tuples are equal. If not, an error message is constructed that shows only the differences between the two.
#
# 3 assertSetEqual (set1, set2, msg = None)
# Tests that two sets are equal. If not, an error message is constructed that lists the differences between the sets.
#
# 4 assertDictEqual (expected, actual, msg = None)
# Test that two dictionaries are equal. If not, an error message is constructed that shows the differences in the dictionaries.
#
# The following example implements the above methods −

import unittest

class SimpleTest(unittest.TestCase):
   def test1(self):
      self.assertListEqual([2,3,4], [1,2,3,4,5])
   def test2(self):
      self.assertTupleEqual((1*2,2*2,3*2), (2,4,6))
   def test3(self):
      self.assertDictEqual({1:11,2:22},{3:33,2:22,1:11})
   def test4(self):
       self.assertSetEqual({1, 22}, {1,22})
if __name__ == '__main__':
   unittest.main()