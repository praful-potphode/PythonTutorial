# Running pytest without mentioning a filename will run all files of format test_*.py or *_test.py in the current directory and
# # subdirectories. Pytest automatically identifies those files as test files.
# # We can make pytest run other filenames by explicitly mentioning them.
# # Pytest requires the test function names to start with test.
# # Function names which are not of format test* are not considered as test functions by pytest.
# # We cannot explicitly make pytest consider any function not starting with test as a test function.

# Note − pytest command will execute all the files of format test_* or *_test in the current directory and subdirectories.

import math
import pytest
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def tesequality():
   assert 10 == 11

def test_greater():
   num = 100
   assert num > 100

def test_greater_equal():
   num = 100
   assert num >= 100

def test_less():
   num = 100
   assert num < 200

# To execute the tests containing a string in its name we can use the following syntax −
#
# pytest -k <substring> -v
# -k <substring> represents the substring to search for in the test names.
#
# Now, run the following command −
#
# pytest -k great -v
# This will execute all the test names having the word ‘great’ in its name.
# In this case, they are test_greater() and test_greater_equal().
# Note − The name of the test function should still start with ‘test’.