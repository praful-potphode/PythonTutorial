import pytest

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0

def test_divisible_by_13(input_value):
   assert input_value % 13 == 0

# Run the tests by executing the following command −
#
# pytest -k divisible -v
# The tests will look for fixture in the same file. As the fixture is not found in the file, it will check for fixture in
# conftest.py file. On finding it, the fixture method is invoked and the result is returned to the input argument of the
# test.
# pytest -k divisible -v conftestdemo.py
#